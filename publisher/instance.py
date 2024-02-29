
import sys
sys.path.append("..")
from my_paho.client_paho import create_client

def on_connect(client, userdata, flags, rc,properties=None):
    print("Conectado com código de resultado: " + str(rc))

def send_mqtt_message(client, topic, msg):
   
    try:
        client.publish(topic, msg)
        print(f"Mensagem enviada: \n{msg}")
                      
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
        print("Desconectado do broker MQTT")


def start():
    client = create_client(on_connect, on_message=None)
    client.loop_start()
    return client





