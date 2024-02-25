import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))

def send_mqtt_message(client, topic, msg):
   
    try:
        client.publish(topic, msg)
        print(f"Mensagem enviada: \n{msg}")
                      
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
        print("Desconectado do broker MQTT")


def start(broker_address, port):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker_address, port, 60)
    client.loop_start()
    return client





