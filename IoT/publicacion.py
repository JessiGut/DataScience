import json
import paho.mqtt.client as mqtt
from secrets import choice
import string
import random
from time import sleep
# from datetime import datetime

# Declarar las variables de conexion al broker
host = ""
port_MQTT = 1883

# User y password
# USER_MQTT = ''
# PASS_MQTT = ''

# Crear un cliente aleatorio para no tener problemas en la conexion
num = ''.join([choice(string.ascii_uppercase
               + string.digits) for _ in range(30)])
num_client = 'interface_' + num

# Crear el cliente
client = mqtt.Client(num_client)

# client.username_pw_set(username= USER_MQTT, password= PASS_MQTT)

# Realizar la conexion
try:
    connect = client.connect(host, port_MQTT)
except Exception as e:
    print('error connection MQTT:', str(e))

"""
Publicar mensaje de temperatura
y tiempo mandar 50 mensajes uno por cada 3 segundos
"""

for i in range(0, 50):
    data = {"Temperatura": random.randrange(15, 35)}

    def publishNew(topic):
        def on_publishSingle(client, userdata, mid):
            print("on_publish callback id: " + str(mid))

        routing_key = str(topic)
        data_json = json.dumps(data)
        message = data_json

        # Realizar la publicacion
        client.on_publish = on_publishSingle
        client.publish(routing_key, message, qos=0, retain=False)
        print(f"{routing_key}:{message}")
        client.loop_start()

    # topic del mensaje (ruta del envio)
    topic = "Casa/Salon/"
    # LLamar a la función de publicar
    publishNew(topic)
    sleep(10)