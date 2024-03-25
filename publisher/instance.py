
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


# from confluent_kafka import Producer

# p = Producer({'bootstrap.servers': 'mybroker1,mybroker2'})

# def delivery_report(err, msg):
#     """ Called once for each message produced to indicate delivery result.
#         Triggered by poll() or flush(). """
#     if err is not None:
#         print('Message delivery failed: {}'.format(err))
#     else:
#         print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# for data in some_data_source:
#     # Trigger any available delivery report callbacks from previous produce() calls
#     p.poll(0)

#     # Asynchronously produce a message. The delivery report callback will
#     # be triggered from the call to poll() above, or flush() below, when the
#     # message has been successfully delivered or failed permanently.
#     p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# # Wait for any outstanding messages to be delivered and delivery report
# # callbacks to be triggered.
# p.flush()





