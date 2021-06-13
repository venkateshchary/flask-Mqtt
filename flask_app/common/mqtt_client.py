import paho.mqtt.client as mqtt
from ..views.mqtt_sender import sender
from ..views.mqtt_receiver import receiver

MQTT_SUBSCRIBERS = {
    "test_receive": receiver,
    "test_sender": sender
}

CLIENT = mqtt.Client("connection_test", clean_session=True)


def on_connect(client, userdata, flags, rc):
    for topic, funct in MQTT_SUBSCRIBERS.items():
        CLIENT.subscribe(topic, 0)
        CLIENT.message_callback_add(topic, funct)


def init_mqtt():
    try:
        broker = "127.0.0.1"
        CLIENT.connect(broker, 1883, 60)
        CLIENT.on_disconnect = on_disconnect
        CLIENT.on_connect = on_connect
        CLIENT.loop_start()
    except Exception as e:
        print("error at connecting to mqtt : ", e)


def on_disconnect(client, userdata, rc):
    print("client is disconnected")
    client.reconnect()
