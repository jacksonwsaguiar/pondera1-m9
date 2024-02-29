import sys
import requests
sys.path.append("..")
import json

from my_paho.client_paho import create_client

api_url = 'http://127.0.0.1:5000/save-info'
topic = "reading/solar"
def on_message(client, userdata, msg):
    print(f"Nova mensagem recebida no tópico '{msg.topic}':\n{msg.payload.decode()}")
    response = requests.post(api_url,json=json.loads(msg.payload.decode()))

    if response.status_code == 201:
        print("Saved on database")
    else:
        print(f"Error: {response.json()}")
    

def on_connect(client, userdata, flags, rc, proerties=None):
    client.subscribe(topic)
    print(f"Inscrito no tópico '{topic}'\n")


client = create_client(on_connect, on_message)
client.loop_forever()