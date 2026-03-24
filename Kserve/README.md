# Kserve

KServe (often what people mean by “kserver”) is an open-source platform used to deploy and manage machine learning models on Kubernetes. KServe uses Kubernetes as its foundation instead of replacing it.

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/13bc2519-52b8-40b8-b42f-cbf0adc820f6" />


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


 ### Model server
 The model server is a component that KServe uses to actually run your model
  [Client Request] --> [KServe] --> [Model Server] --> [Your Model] --> [Response]


<img width="1118" height="744" alt="image" src="https://github.com/user-attachments/assets/ab42e09a-1714-4802-9148-5bd353fcf6e0" />
