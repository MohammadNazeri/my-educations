# Larg Language Model  
## NOTE: The .ipynb file is a lab assignment from the Coursera website
## List of contents  
## Week 1  
* Transformer Network
* Genitive AI Project Life Cycle
  * Scope: Define the use case
  * Select: Choose an existing model or pretrain your own
  * Adapt and align model:
    * Prompt engineering
    * Fine-tuning
    * Align with human feedback
    * Evaluate
  * Application integration
* Prompt Engineering
  
## Week 2
* ### Instruction fine-tunning
  * Increase performance of the existing model for specific use case > using fine-tuning > to further train a base model
  * fine-tuning with instruction prompt > fine-tune LLM = instruct LLM
  * use an existing dataset with [prompt, completion] > supervised learning instead of self supervised learning
  * full fine-tuning: every model weight is updated. The process results in a new version of the model with updated weights.
  * Evaluate performance
* ### Fine-tuning on a single task
  * drawbacks: catastrophic forgetting=forget other tasks(changed W and bad result on other tasks)
  * Solution: If you need a single task, the drawback is not a big deal. if not:
    * Multitask fine tuning
    * Perform parameter-efficient fine-tuning(PEFT)
* ### Multitask fine tuning
  * FLAN: is a specific set of instructions used to fine-tune different models. FLAN-T5, the FLAN instruct version of the T5 foundation model
* ### Model Evaluate
  * Rouge > text summarization
  * Bleu score > text translation
* ### Benchmark
  * Using pre-existing datasets and associated benchmarks
  * Benchmark: GLUE, SuperGLUE and HELM
  * 
* ### Parameter efficient fine-tuning (PEFT):
  * update a small set of subparameters > less prone to catastrophic forgetting: because original LLM slightly modified
  * update a small number of weights + small footprint overall + small adaptation to each task
  * Three main classes of PEFT method:
    * Selective: fine-tune only a subset of parameters. They could be specific layers of a certain component.
    * Reparametrization: it reduces the number of parameters to train by creating new low-rank transformations of the original network weights(LoRA).
    * Additive: It keeps all of the original LLM weights frozen and introduces new trainable components. there are two approches:
      *  Adapter methods add new trainable layers to the architecture of the model, typically inside the encoder or decoder components after the attention or feed-forward layers.
      *  Soft prompt methods keep the model architecture fixed and frozen, and focus on manipulating the input to achieve better performance. This can be done by adding trainable parameters to the prompt embeddings or keeping the input fixed and retraining the embedding weights. 
* ### Low-rank Adaptation(LoRA) is a parameter-efficient fine-tuning technique  
  * After the embedding vectors are created, they're fed into the self-attention layers where a series of weights are applied to calculate the attention scores. During full fine-tuning, every parameter in these layers is updated.
  * LoRA is a strategy that reduces the number of parameters to be trained during fine-tuning by freezing all of the original model parameters and then injecting a pair of rank decomposition matrices alongside the original weights.
  * The dimensions of the smaller matrices are set so that their product is a matrix with the same dimensions as the weights they're modifying. And then, we train the smaller matrices.
  * [original weights] + B*A
  * Applying LoRA to the self-attention layers of the model is often enough to fine-tune for a task and achieve performance gains. However, you can also use LoRA on other components like the feed-forward layers.
* ### Soft prompt ( prompt tuning not prompt engineering)
  * Prompt tuning: you add additional trainable tokens to your prompt and leave it up to the supervised learning process to determine their optimal values.
  * Softprompt: The set of trainable tokens is called a soft prompt. It gets prepended to embedding vectors that represent your input text.
  * The tokens that represent natural language are hard (fixed location in the embedding vector space). However, the soft prompts are not fixed discrete words of natural language.
* ### Summary:
  * full fine tuning:
    * The training data set consists of input prompts and output completions or labels.
    * The weights of the large language model are updated
    * It is supervised learning.
  * Prompt tuning:
    * The weights of the large language model are frozen
    * The embedding vectors of the soft prompt gets updated over time to optimize the model's completion of the prompt.
    * You can train a different set of soft prompts for each task and then easily swap them out at inference time. 
## Week 3
* RLHF: It helps to align the model with human values and uses reinforcement learning as an algorithm.
* LLMs as a reasoning engine and let it cause our own of routines to create an agent. They can take actions.
* responsible AI
* OMS as a reasoning engine
* These important human values, helpfulness, honesty, and harmlessness are sometimes collectively called HHH, and are a set of principles that guide developers in the responsible use of AI.
* RLHF uses reinforcement learning to finetune the LLM with human feedback data.
* Reinforcement learning is a type of machine learning in which an agent learns to make decisions related to a specific goal by taking actions in an environment, with the objective of maximizing some notion of a cumulative reward.
* The agent makes decisions by following a strategy known as the RL policy. 
* The goal of reinforcement learning is for the agent to learn the optimal policy for a given environment that maximizes their rewards. 
* The sequence of actions and states is called a rollout, instead of the term playout that's used in classic reinforcement learning.
* components:
  * Policy: the agent's policy that guides the actions is the LLM
  * Objectives: its objective is to generate text that is perceived as being aligned with human preferences (helpful, accurate, and non-toxic)
  * Agents: 
  * Environment: the context window of the model, the space in which text can be entered via a prompt. 
  * Actions: This could be a single word, a sentence, or a longer form text, depending on the task specified by the user. At any given moment, the action that the model will take, meaning which token it will choose next, depends on the prompt text in the context and the probability distribution over the vocabulary space.
  * Action state: The action space is the token vocabulary, meaning all the possible tokens that the model can choose from to generate the completion. 
  * States: The state that the model considers before taking an action is the current context.  That means any text currently contained in the context window.
  * Rewards: reward model, to classify the outputs of the LLM and evaluate the degree of alignment with human preferences.
* RLHF: Obtaining feedback from humans
  * The first step in fine-tuning an LLM with RLHF is to select a model to work with and use it to prepare a data set for human feedback.
  *  instruct model > fine tuned > generate a number of different responses for each prompt in prompt dataset > produce set of completion for each prompt > collect feedback from human labelers on the completions (decide what criterion to assess (helpfulness)) > rank completions could be number or F (non relevent)> convert the ranking data into a pairwise comparison of completions. > Now, you have  all the data you need to train the reward model Which you will use instead of humans to classify model completions during the reinforcement learning finetuning process. 
