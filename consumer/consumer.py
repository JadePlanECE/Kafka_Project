import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "player-actions",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest'
)

print("Consumer started, waiting for events...\n")

for message in consumer:
    event = message.value
    action = event['action']
    
    if action == "move":
        detail = f"moved {event['direction']}"
    elif action == "attack":
        detail = f"attacked {event['target']}"
    elif action == "collect_item":
        detail = f"collected {event['collect_item']}"
    elif action == "use_item":
        item = event['use_item'] if event['use_item'] else "nothing"
        detail = f"used {item}"
    else:
        detail = action
    
    print(f"Consumed: Player {detail}")
