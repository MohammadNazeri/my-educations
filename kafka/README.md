# Kafka
* Kafka is an open-source distributed event streaming platform used to handle real-time data feeds.
* Think of Kafka as a high-performance messaging system where data can be published, stored, and processed in real time — often used in large-scale systems like those at Netflix, LinkedIn, or Uber.
<img src="https://github.com/user-attachments/assets/a012b81c-2096-47aa-8b61-5d7b0b7d6062" style="width: 30%;" />

### Event
* Event is form of data which read or write to Kafka. It is Json.
* Events are stored in Topics
```
{
  "event_type": "user_login",
  "user_id": "u-123",
  "ip": "203.0.113.42",
  "ts": "2025-10-16T14:07:00Z"
}
```
### Main Concept
* Producer sends events to Topic
* Cosumer(microservices) subscribe to Topics. Each respective consumer gets notified by Kafka when a new event is added to that topic.
<img src="https://github.com/user-attachments/assets/b2373ea9-71b3-44d2-b28f-77d677c2a95f" style="width: 50%;" />

## Kafka usecases
* Enables chain reaction: by ordering a product, it generate squence of action to deliver to user
* Real-time Processing: Like sales dashboard, driver location in Uber
### Kafka Stream API
* It allows you to create real-time apps by continuously transforming and analysing incoming data stream.
* You donot need to explicitly request new records, you just receive them.

## Kafka Partition
* In big project, a Kafka topic is divided into one or more partitions.
  * Events with the same Key are written to the same partition.
  * The benefits: Scalability, paralelism, ordering, Fault Tolerance, Logical grouping.
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

