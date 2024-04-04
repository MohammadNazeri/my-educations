Dear Saba,
I hope you are doing well.
I am Mohammad, a student at Polytechnique Montreal University and I have experience in the ML field. I met you at a job fair about one month ago. You spoke about some topics like DGL and Networkx. You suggested that I try to read about them and have a meeting around the end of February. 
I started to get to know more about some concepts like DGL, GCN, node representation, and representation of pairs of nodes. In addition, I tried to run some tasks like node classification, link prediction, and customizing GNN module. Also, I used the Networkx library to show the graphs graphically.
In the meantime, I read some articles about GNNs. It is a very interesting topic. Graph Neural Networks (GNNs) have gained much attention in biotechnology and drug discovery. Because the model can represent complex molecular structures as networks, capture vital structural information, and seamlessly handle diverse data types. 

I would like to dig into these topics. I wonder if there would be any position in your company.




# Deep Graph Library (DGL)
DGL provides an abstraction for building and working with graph neural networks. It allows users to define message functions, aggregation functions, and update functions easily.
## Node classification:
* Node classification, where a model needs to predict the ground truth category of each node.
* GNNs offer an opportunity to obtain node representations by combining the connectivity and features of a local neighborhood
* Before graph neural networks, many proposed methods are using either connectivity alone (such as DeepWalk or node2vec), or simple combinations of connectivity and the node's own features.
* A DGL graph can store node features and edge features in two dictionary-like attributes called ndata and edata.
* Graph Convolutional Network (GCN): Each layer computes new node representations by aggregating neighbor information.


## [GRAPH CONVOLUTIONAL NETWORKS](https://distill.pub/2021/understanding-gnns/#introduction) (GCN) 
* Graph Convolutional Networks (GCNs) are a type of Graph Neural Network that fits into the message passing paradigm. They use graph convolutional layers to update node representations by aggregating information from neighboring nodes.
* Graph neural networks (GNNs) are a family of neural networks that can operate naturally on graph-structured data. 
* Many important real-world datasets come in the form of graphs or networks: social networks, knowledge graphs, protein-interaction networks, the World Wide Web, etc.
* node representation learning: learning to map individual nodes to fixed-size real-valued vectors (called ‘representations’ or ‘embeddings’).
* Node representation refers to the numerical or vectorial representation of a node in a graph. In the context of a Graph Convolutional Network (GCN), each node in the graph is associated with a vector that captures its features or characteristics. These representations aim to encode relevant information about the node and its neighborhood within the graph.





Tutorials:
1. This tutorial will show how to build such a GNN for semi-supervised node classification with only a small number of labels on the Cora dataset, a citation network with papers as nodes and citations as edges. The task is to predict the category of a given paper. 


