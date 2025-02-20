import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps 
producer = KafkaProducer(bootstrap_servers=['<EC2_PUBLICIP:<KAFKA_PORT>'], value_serializer=lambda x:dumps(x).encode('utf-8'))
df = pd.read_csv("data/dataset.csv")
while True:
    stock_dict = df.sample(1).to_dict(orient="records")[0]
    producer.send('data', value=stock_dict)
    sleep(2)