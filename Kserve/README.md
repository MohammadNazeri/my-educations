# Kserve
KServe (often what people mean by “kserver”) is an open-source platform used to deploy and manage machine learning models on Kubernetes. KServe uses Kubernetes as its foundation instead of replacing it.

Kubernetes does not know anything about ML models:
  * It doesn’t know how to expose a /predict API automatically
  * It doesn’t know which framework your model uses (TensorFlow, PyTorch, sklearn)
  * It doesn’t automatically handle model versioning, canary updates, or A/B testing
  * It doesn’t scale based on inference requests or GPU usage, only generic CPU/memory metrics

With KServe:
* You define a simple custom resource like an InferenceService
* KServe automatically:
  * Creates the needed Kubernetes objects
  * Sets up autoscaling (even to zero)
  * Routes traffic to your model (via REST or gRPC APIs)
  * Manages revisions and updates

 ### Model server
 The model server is a component that KServe uses to actually run your model
  [Client Request] --> [KServe] --> [Model Server] --> [Your Model] --> [Response]
