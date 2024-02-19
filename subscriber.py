import paho.mqtt.client as mqtt

broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "reading/solar" 

def on_message(client, userdata, msg):
    print(f"Nova mensagem recebida no tópico '{msg.topic}':\n{msg.payload.decode()}")

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    print(f"Inscrito no tópico '{topic}'\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port, 60)
client.loop_forever()
