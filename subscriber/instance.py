import sys
import requests
sys.path.append("..")
import json
from confluent_kafka import Consumer
# from my_paho.client_paho import create_client

api_url = 'http://127.0.0.1:5000/save-info'
# topic = "reading/solar"
def save(data):
    response = requests.post(api_url,json=json.loads(data))

    if response.status_code == 201:
        print("Saved on database")
    else:
        print(f"Error: {response.json()}")
    

# def on_connect(client, userdata, flags, rc, proerties=None):
#     client.subscribe(topic)
#     print(f"Inscrito no tópico '{topic}'\n")


# client = create_client(on_connect, on_message)
# client.loop_forever()

def read_config():
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

def main():
  config = read_config()
  topic = "topic_0"
  
  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"

  consumer = Consumer(config)
  consumer.subscribe([topic])
  try:
    while True:
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")

        save(value)
        print(f"Consumed message from topic {topic}: key = {key:12} value = {value:12}")
  except KeyboardInterrupt:
    pass
  finally:
    consumer.close()


main()

