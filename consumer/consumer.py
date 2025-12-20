from kafka import KafkaConsumer

consumer = KafkaConsumer("player-actions", bootstrap_servers='127.0.0.1:9092', api_version=(0, 11, 5))

print("Consumer started, waiting for events...\n")
for message in consumer:
    event = message.value
    print(f"Consumed: Player did {event['action']} to {event['direction']} at {event['target']} with {event['collect_item']} or {event['use_item']}")
