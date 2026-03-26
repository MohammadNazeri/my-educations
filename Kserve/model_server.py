"""KServe custom predictor for LLM-based question answering."""

import argparse
from typing import Dict, List

import torch
from kserve import Model, ModelServer, model_server
from transformers import AutoModelForCausalLM, AutoTokenizer


class LLMModel(Model):
    def __init__(self, name: str, model_id: str):
        super().__init__(name)
        self.model_id = model_id
        self.tokenizer = None
        self.model = None
        self.ready = False

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.ready = True

    def predict(self, payload: Dict, headers: Dict = None) -> Dict:
        """Handle inference requests.

        Expected payload:
        {
            "instances": [
                {"question": "What is KServe?"}
            ],
            "parameters": {          # optional
                "max_new_tokens": 256,
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        """
        instances: List[Dict] = payload.get("instances", [])
        params = payload.get("parameters", {})
        max_new_tokens = params.get("max_new_tokens", 256)
        temperature = params.get("temperature", 0.7)
        top_p = params.get("top_p", 0.9)

        results = []
        for instance in instances:
            question = instance.get("question", "")
            prompt = f"Question: {question}\nAnswer:"

            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
            with torch.no_grad():
                output_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    do_sample=True,
                )
            answer = self.tokenizer.decode(
                output_ids[0][inputs["input_ids"].shape[-1]:],
                skip_special_tokens=True,
            )
            results.append({"question": question, "answer": answer.strip()})

        return {"predictions": results}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(parents=[model_server.parser])
    parser.add_argument(
        "--model_id",
        type=str,
        default="./llm",
        help="Local path to the model directory",
    )
    args, _ = parser.parse_known_args()

    model = LLMModel(name="llm-qa", model_id=args.model_id)
    model.load()
    ModelServer().start([model])
