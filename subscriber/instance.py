import sys
sys.path.append("..")
from my_paho.client_paho import create_client

topic = "reading/solar"

def on_message(client, userdata, msg):
    print(f"Nova mensagem recebida no tópico '{msg.topic}':\n{msg.payload.decode()}")
    return msg.payload.decode()

def on_connect(client, userdata, flags, rc, proerties=None):
    client.subscribe(topic)
    print(f"Inscrito no tópico '{topic}'\n")


client = create_client(on_connect, on_message)
client.loop_forever()