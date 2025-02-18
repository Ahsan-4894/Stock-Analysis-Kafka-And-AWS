from kafka import  KafkaConsumer
from json import  loads
import json
from s3fs import S3FileSystem
consumer = KafkaConsumer('data', bootstrap_servers = ['<EC2_Global_IP>:<KAFKA_PORT>'], value_deserializer = lambda x: loads(x.decode('utf-8')))
s3 = S3FileSystem()
for count, c in enumerate(consumer):
    with s3.open("s3://<BUCKET_NAME>/stock_market_{}.json".format(count), 'w') as file:json.dump(c.value, file) 