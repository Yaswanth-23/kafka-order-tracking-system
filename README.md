# Kafka Order Tracking System

This project demonstrates a simple Producer-Consumer system using Apache Kafka and Python.

## Technologies Used
- Apache Kafka
- Zookeeper
- Python
- Docker
- Confluent Kafka Python Client

## Project Structure

producer.py
tracker.py
docker-compose.yaml

## How It Works

Producer:
Generates an order event and sends it to Kafka topic `orders`.

Consumer:
Subscribes to the `orders` topic and prints order details when received.

## Setup Instructions

### 1 Start Kafka using Docker

docker-compose up -d

### 2 Install Python dependency

pip install confluent-kafka

### 3 Run Producer

python producer.py

### 4 Run Consumer

python tracker.py

## Example Output

order received: 20*icecream from Nani