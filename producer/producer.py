import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

players = ["Alice", "Bob", "Charlie"]
actions = ["move_north", "move_south", "attack", "collect_item", "use_item"]

for i in range(10):
    action_event = {
        "player": random.choice(players),
        "action": random.choice(actions),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    producer.send("player-actions", value=action_event)
    print(f"Produced: {action_event}")
    time.sleep(1)

producer.flush()
