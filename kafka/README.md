# Kafka
* Kafka is an open-source distributed event streaming platform used to handle real-time data feeds.
* Think of Kafka as a high-performance messaging system where data can be published, stored, and processed in real time — often used in large-scale systems like those at Netflix, LinkedIn, or Uber.
<img src="https://github.com/user-attachments/assets/a012b81c-2096-47aa-8b61-5d7b0b7d6062" style="width: 50%;" />

* Events are stored in Topics
* Cosumer(microservices) subscribe to Topics. Each respective consumer gets notified when a new event is added to that topic.
<img src="https://github.com/user-attachments/assets/b2373ea9-71b3-44d2-b28f-77d677c2a95f" style="width: 50%;" />

## Functionality of Kafka
* Enables chain reaction: by ordering a product, it generate squence of action to deliver to user
* Real-time analytics: like Uber whichi send location in real-time

## Kafka performance
* In big project, a Kafka topic is divided into one or more partitions.
* A consumer group is a set of consumers that work together to read data from a topic. This makes it possible to process data in parallel.
<img src="https://github.com/user-attachments/assets/252d4f59-a090-4d86-a0be-d4f3ef0837e0" style="width: 50%;" />

## Data Persistence
* After consuming data from topics, there keeps in broker.
* Later, those kept data can be used for analytics.
















## Event 
## Chain of Events
## Real-time Processing Stream
## Stream API
### Producer and Consumer
## partitions for Scalability and Performance > partition topics
## Consumer groups for scalable message consumptions
## Kafka Broker
## Zookeeper

