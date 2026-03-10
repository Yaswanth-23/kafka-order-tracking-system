# 🚀 Kafka Order Tracking System



\

A **real-time event-driven order tracking system** built using **Apache Kafka and Python**.

This project demonstrates how distributed systems communicate using **event streaming architecture**, where services interact through **Kafka topics instead of direct communication**.

---

# 📌 Project Overview

Modern scalable applications rely on **event-driven architectures** to process data in real time.

This project simulates a **simple order processing pipeline**:

1️⃣ A **Producer service** generates an order event
2️⃣ The event is published to a **Kafka topic**
3️⃣ A **Consumer service** listens for events
4️⃣ The consumer processes and prints the order details

This pattern is widely used in:

* E-commerce platforms
* Payment processing systems
* Real-time analytics pipelines
* Logistics tracking systems

---

# 🏗 System Architecture

```id="arch001"
        +-------------+
        |  Producer   |
        |  (Python)   |
        +------+------+
               |
               |  Order Event
               v
        +-------------+
        |   Kafka     |
        |   Topic     |
        |  "orders"   |
        +------+------+
               |
               |  Event Stream
               v
        +-------------+
        |  Consumer   |
        |  (Tracker)  |
        +-------------+
```

Kafka acts as the **event broker**, ensuring reliable and scalable communication between services.

---

# 🛠 Tech Stack

| Technology             | Purpose                            |
| ---------------------- | ---------------------------------- |
| Python                 | Producer & Consumer implementation |
| Apache Kafka           | Event streaming platform           |
| Zookeeper              | Kafka coordination service         |
| Docker                 | Containerized Kafka setup          |
| Confluent Kafka Client | Python Kafka integration           |

---

# 📂 Project Structure

```id="struct001"
kafka-order-tracking-system
│
├── docker-compose.yaml
├── producer.py
├── tracker.py
└── README.md
```

### Files

**docker-compose.yaml**

Starts Kafka and Zookeeper using Docker.

**producer.py**

Generates and sends order events to Kafka.

**tracker.py**

Consumes events from Kafka and processes them.

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```id="clone001"
git clone https://github.com/yourusername/kafka-order-tracking-system.git
cd kafka-order-tracking-system
```

---

## 2️⃣ Start Kafka Infrastructure

Run:

```id="docker001"
docker-compose up -d
```

This will start:

* Zookeeper
* Kafka Broker

Check running containers:

```id="docker002"
docker ps
```

---

## 3️⃣ Install Python Dependency

```id="pip001"
pip install confluent-kafka
```

---

# ▶️ Running the System

## Step 1 — Start Consumer

```id="run001"
python tracker.py
```

Output:

```id="out001"
consumer is running and subscribed to topic
```

---

## Step 2 — Run Producer

Open another terminal:

```id="run002"
python producer.py
```

Producer sends order event.

---

# 📦 Example Event

Producer sends a JSON message to Kafka:

```json
{
  "order_id": "8e7c9a4f",
  "user": "Nani",
  "item": "icecream",
  "quantity": 20
}
```

---

# 📊 Consumer Output

```id="out002"
order received: 20*icecream from Nani
```

This confirms the **event successfully traveled through Kafka**.

---

# 🔄 Event Flow Explained

1️⃣ Producer creates an order event
2️⃣ Event is serialized to JSON
3️⃣ Message is published to Kafka topic `orders`
4️⃣ Kafka stores the event in the log
5️⃣ Consumer polls the topic
6️⃣ Consumer processes the event

---

# 💡 Concepts Demonstrated

This project demonstrates key distributed system concepts:

* Event Driven Architecture
* Apache Kafka Producer / Consumer
* Topic-based messaging
* Message serialization (JSON)
* Consumer groups
* Real-time event processing
* Containerized infrastructure

---

# 🚀 Possible Improvements

This project can be expanded with:

* Multiple producers
* Multiple consumers
* Kafka partitions
* Order status service
* Database persistence
* REST API gateway
* Kafka monitoring dashboard
* Schema registry
* Stream processing with Kafka Streams

---

# 🎯 Learning Outcomes

After completing this project you will understand:

* How **Apache Kafka works**
* How **event streaming systems operate**
* How **microservices communicate asynchronously**
* How to build **real-time data pipelines**

---

# 👨‍💻 Author

Yaswanth

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork it and build your own improvements
