# Apache Spark
* This is an open-source distributed computing system that is designed for big data processing and analytics.
* Hadoop is an open-source software framework used for distributed storage and processing of large datasets across clusters of commodity hardware. It has two parts:
  * HDFS (Hadoop Distributed File System): It is used for storing our data across multiple computers. It's a distributed file system.
  * MapReduce: It is used to process all data in parallel.
* Hadoop relies on storing data on disk(slow). The solution is RDD which is 100 times faster than Hadoop
* RDD (Resilient Distributed Dataset) is a fundamental data structure in Apache Spark. It allows to store data in memory and enable faster processing.
* Components:
  * Spark Core: It provides distributed task scheduling, memory management, fault recovery, and interaction with storage systems. Spark Core also includes the Resilient Distributed Dataset (RDD) API, which represents a distributed collection of objects that can be operated on in parallel.
  * Spark SQL: It provides a programming interface for working with structured data within Spark. It allows users to run SQL queries, as well as perform SQL-like operations
  * Spark Streaming: It enables real-time processing of streaming data. 
  * MLlib: MLlib is Spark's scalable machine learning library. It provides a wide range of machine learning algorithms and utilities
  * GraphX: It provides a distributed graph processing framework built on top of Spark's RDD abstraction. GraphX enables users to manipulate and analyze graph-structured data, such as social networks or web graphs, using a range of graph algorithms and operators.
 
![image](https://github.com/MohammadNazeri/my-educations/assets/109389707/82bd6069-0b7c-409f-9656-0a2f79d2840d)

## Apache Spark architecture
1. Driver process: It is the main control program that coordinates the execution of a Spark application (an application that runs on the distributed system)
2. Executor process: It executes the code assigned by the driver process.
* Cluster manager: is responsible for allocating and managing resources across the nodes in a Spark cluster. It acts as a resource manager and scheduler, coordinating the execution of Spark applications on the cluster nodes.

