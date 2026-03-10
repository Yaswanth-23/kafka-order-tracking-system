import json
import uuid
from confluent_kafka import Producer
conf = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(conf)
def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"delivered {msg.value().decode('utf-8')}")
order = {
    "order_id": str(uuid.uuid4()),
    "user": "Nani",
    "item": "icecream",
    "quantity": 20
}
value = json.dumps(order).encode("utf-8")
producer.produce(
    topic="orders",
    value=value,
    callback=delivery_report
)
producer.flush()
