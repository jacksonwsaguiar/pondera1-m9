import time
from publisher.instance import send_mqtt_message, start
from my_paho.client_paho import create_client


broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "reading/solar"

received_messages = []

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    received_messages.append(msg.payload.decode())

def create_subscriber(broker_address, topic, port):
    client = create_client(on_connect=None, on_message=on_message)
    client.subscribe(topic)
    return client

def test_publisher_data():
    print("Testing confirm data sent and data validation")
    msg = '{"period":"night","radiation_intensity": "841.7"}'

    sub_client = create_subscriber(broker_address,topic, port)

    mqtt_client = start()

    send_mqtt_message(mqtt_client, topic, msg)

    time.sleep(5)
  
    sub_client.loop_start()
    time.sleep(10)
    sub_client.loop_stop()

    mqtt_client.disconnect()
    sub_client.disconnect()

    print("Received messages:", received_messages)

    assert len(received_messages) > 0, "Nenhuma mensagem recebida."
    assert received_messages[0] == msg, "Dados inválidos."


message_count=0

def on_message_perform(client, userdata, msg):
    message_count += 1

def test_perform_mqtt_test():
    print("Testing performance")

    expected_rate = 1
    error_margin = 2
    test_duration = 10

    start_time = time.time()
    
    client = create_client(on_connect=None, on_message=on_message_perform)

    try:
        client.subscribe(topic)
        client.loop_start()
        
        time.sleep(test_duration)

        client.loop_stop()
        client.disconnect()
    except Exception as e:
        print(f"Exception during MQTT operation: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    message_rate = message_count / elapsed_time

    assert abs(message_rate - expected_rate) < error_margin, "Taxa de disparo fora da margem de erro."
    print("Taxa de disparo dentro da margem de erro.")