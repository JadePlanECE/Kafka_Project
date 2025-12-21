import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

actions = ["move", "attack", "collect_item", "use_item"]
directions = ["north", "south", "est", "ouest"]
targets = ["goblins", "dragon", "team mate"]
collect_items = ["gold coins", "rock", "stick", "weapon"]
use_items = ["heal potion", ""]

for i in range(10):
    action = random.choice(actions)
    direction = ""
    target = ""
    collect = ""
    use = ""

    if action == actions[0]:
        direction = random.choice(directions)
    elif action == actions[1]:
        target = random.choice(targets)
    elif action == actions[2]:
        collect = random.choice(collect_items)
    elif action == actions[3]:
        use = random.choice(use_items)

    action_event = {
        "action": action,
        "direction": direction,
        "target": target,
        "collect_item": collect,
        "use_item": use
    }
    producer.send("player-actions", value=action_event)
    print(f"Produced: {action_event}")
    time.sleep(1)

producer.flush()