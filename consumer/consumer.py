import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "player-actions",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started, waiting for events...\n")
for message in consumer:
    event = message.value
    print(f"Consumed: Player {event['player']} did action '{event['action']}' at {event['timestamp']}")
