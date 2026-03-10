import json

from confluent_kafka import Consumer
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest",
}
consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])
print("consumer is running and subscribed to topic")
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: ",msg.error())
            continue
        value = msg.value().decode('utf-8')
        order = json.loads(value)
        print(f"order received: {order['quantity']}*{order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("closing consumer")
finally:
    consumer.close()