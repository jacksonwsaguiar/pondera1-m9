from csv_reader import read_csv
from publisher.instance import send_mqtt_message, start
import time

topic = "reading/solar" 

file = 'simulation.csv'
data = read_csv(file)

mqtt_client = start()

try:
    for single in data:
        send_mqtt_message(mqtt_client, topic, str(single))
        print("reading data...\n")
        time.sleep(3)
        
except KeyboardInterrupt:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("Desconectado do broker MQTT")
