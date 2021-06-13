import json


def receiver(client, userdata, data):
    try:
        data = json.loads(data.payload.decode())
        print("received from receiver: ", data)
    except Exception as e:
        print("error at encoding the message from mqtt", e)
