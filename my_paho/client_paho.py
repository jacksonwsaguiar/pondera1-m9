import sys
sys.path.append("..")

import paho.mqtt.client as mqtt

host = "0461d3bb20f749cd936e6566a4b00c44.s1.eu.hivemq.cloud"
port = 8883

username = "hivemq.webclient.1708885300681"
password = "69bmGBZ.3OoA!dahP,4&"

def create_client(on_connect, on_message):
    client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    
    client.username_pw_set(username, password)
    client.connect(host, port)
    return client