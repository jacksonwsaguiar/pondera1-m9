from csv_reader import read_csv
from publisher.publisher import send_mqtt_message, start
import time

broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "reading/solar" 

file = 'simulation.csv'
data = read_csv(file)

mqtt_client = start(broker_address, port)

try:
    for single in data:
        send_mqtt_message(mqtt_client, topic, str(single))
        print("reading data...\n")
        time.sleep(3)
        
except KeyboardInterrupt:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("Desconectado do broker MQTT")
