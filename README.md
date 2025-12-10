# Kafka_Project

Final Project : Technical Project (option A)

Big Data tool : Kafka 

The aim of this project is to reproduce real-time data flows in a video game. A producer will create an action, which will be processed by the broker(s), then the consumer will display the action. 

## Structure 
```
kafka_project/
│
├── consumer/
│   ├── consumer.py
│   └── requirements.txt
│
├── data/
│   └── actions.json
│
├── producer/
│   ├── producer.py
│   └── requirements.txt
│
├── screenshots/
│   ├── kafka-running.png
│   ├── producer-output.png
│   └── consumer-output.png
│
├── docker-compose.yaml
└── README.md
```

## Installation 
1. Clone project 
```bash
git clone https://github.com/JadePlanECE/Kafka_Project.git
```

2. Create virtual environnement (recommanded) 
```bash
python -m venv kafka__env

# Windows 
kafka_env\Scripts\activate 
# Linux 
source kafka_env/bin/activate
```

3. Install dependencies 
```bash
pip install -r requirements.txt
```

## Running 
1. Run Kafka tool
```bash
docker-compose up -d
docker ps # check if container started 
```

2. Run producer 
```bash
cd producer
pip install -r requirements.txt
python producer.py
```

3. Run consumer
```bash
cd consumer
pip install -r requirements.txt
python consumer.py
```

## Authors 
- [Jade Planterose](https://github.com/JadePlanECE)
- [Eden Masmoudi](https://github.com/edenmsd)
