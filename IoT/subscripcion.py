# Importar las librerias
import paho.mqtt.client as mqtt
from secrets import choice
import string
# import psycopg2
from connect import insertDB
import json
from datetime import datetime


class sClient:

    # Declarar variables de conexion al broker
    broker_address = ""
    port = 1883

    # declarar cliente aleatorio
    num = ''.join([choice(string.ascii_uppercase
                   + string.digits) for _ in range(30)])
    num_client = 'sClient_' + num
    client = mqtt.Client(num_client)

    # función de recogida mensajes
    def on_message(client, userdata, msg):
        print('*** Mensaje:', str(msg.payload))
        print('Topic:', msg.topic)
        data = json.loads(msg.payload)
        # print(data)
        vivienda = str(msg.topic).split("/")[0]
        # print(vivienda)
        ubicacion = str(msg.topic).split("/")[1]
        # print(ubicacion)
        time = datetime.utcnow()  # str(data['timestamp'])
        temperatura = str(data['Temperatura'])
        # print('time: ', time)
        # print('temperatura: ', temperatura)

        # TODO: insertar en base de datos esta información.
        insertDB(vivienda, ubicacion, temperatura, time)

    # log de información
    def on_log(client, userdata, level, buff):
        print('log:' + str(buff))

    # funciones de informacion de conexion
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("connected OK Returned code=", rc)
        else:
            print("Bad connection Returned code=", rc)

    def on_disconnect(client, userdata, rc):
        print("disconnecting reason " + str(rc))
        client.connected_flag = False
        client.disconnect_flag = True

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # subscripcion al topic
    client.connect(broker_address, port)
    client.on_log = on_log
    client.subscribe("Casa/Salon/", qos=1)
    client.on_message = on_message
    client.loop_forever()