# Kserve

KServe (often what people mean by “kserver”) is an open-source platform used to deploy and manage machine learning models on Kubernetes. KServe uses Kubernetes as its foundation instead of replacing it.

<img src="https://github.com/user-attachments/assets/13bc2519-52b8-40b8-b42f-cbf0adc820f6" alt="image" width="50%">


Kubernetes does not know anything about ML models:
  * It doesn’t know how to expose a /predict API automatically
  * It doesn’t know which framework your model uses (TensorFlow, PyTorch, sklearn)
  * It doesn’t automatically handle model versioning, canary updates, or A/B testing
  * It doesn’t scale based on inference requests or GPU usage, only generic CPU/memory metrics
  * It doesn't know Latency, error rates, batch sizes, GPU utilization, prediction counts — these aren’t automatically tracked.

With KServe:
* You can deploy models with one simple resource definition (InferenceService)
  * Chooses the right model server (TensorFlow Serving, TorchServe, or custom)
* Automatically exposes your model as a REST/gRPC API like /predict
* Scales model servers up/down based on traffic (support GPU)
* Supports multiple versions of the same model
* Allows you to write custom logic if the built-in model servers aren’t enough (preprocess and postprocess)


 ## Model server
 The model server is a component that KServe uses to actually run your model
  [Client Request] --> [KServe] --> [Model Server] --> [Your Model] --> [Response]
  Responsiblities: Load the model, Serve predictions, Manage resources, Monitoring & logging
  | Framework    | Model Server                         |
| ------------ | ------------------------------------ |
| TensorFlow   | **TensorFlow Serving**               |
| PyTorch      | **TorchServe**                       |
| ONNX         | **ONNX Runtime Server**              |
| XGBoost      | **KServe’s built-in XGBoost server** |
| Scikit-learn | **KServe’s built-in SKLearn server** |

Note: Each model server is containerized and KServe automatically handles the orchestration, scaling, and routing through Kubernetes.

<img src="https://github.com/user-attachments/assets/ab42e09a-1714-4802-9148-5bd353fcf6e0" alt="image" width="50%">


## inference protocol
* inference protocol defines the standardized way that a client communicates with a deployed machine learning model to request predictions.
* It works over REST (JSON) and gRPC (Protobuf)

KServe primarily supports two inference protocols:
* V1 Protocol (v1) 
* V2 Protocol (v2) Supports structured inputs, batches, and multi-output models. It can handle more complex data types, like images or tensors. (more production-ready)

In Yaml, When you deploy a model in KServe, you can specify the protocol:
```
spec:
  predictor:
    protocolVersion: "v2"
```

## Run Kserve in AKS
1. Docker image
2. Write code for LLM model
3. Build docker image for LLM model
4. Push it in ACR
5. Create AKS through template
6. Install Kserve and Knative
7. Give AKS to access ACR
8. Apply yaml file to AKS
9. Test it

