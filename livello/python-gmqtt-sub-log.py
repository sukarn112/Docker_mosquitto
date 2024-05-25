import asyncio
import logging
from gmqtt import Client as MQTTClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', handlers=[logging.FileHandler("/app/log/mqtt.log"), logging.StreamHandler()])

# MQTT broker details
BROKER = '172.17.0.1'  # docker's local ip address
PORT = 1883
TOPIC = '/event'

# Define the client class
class MQTTClientAsync:
    def __init__(self, client_id):
        self.client = MQTTClient(client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe

    async def connect(self, broker, port):
        await self.client.connect(broker, port)
    async def disconnect(self):
        await self.client.disconnect()
    async def publish(self, topic, payload):
        await self.client.publish(topic, payload)
    def on_connect(self, client, flags, rc, properties):
        client.subscribe(TOPIC)
    def on_message(self, client, topic, payload, qos, properties):
        message = payload.decode()
        logging.info(f"Received message on topic {topic}: {message}")

    def on_disconnect(self, client, packet, exc=None):
        logging.info("disconnected from broker")
    def on_subscribe(self, client, mid, qos, properties):
        logging.info(f"Subscribed to topic with QoS: {qos}")

# Main function to run the async MQTT client
async def main():
    client = MQTTClientAsync("mqtt_client_id")
    await client.connect(BROKER, PORT)

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await client.disconnect()

# Run the main function
if __name__ == '__main__':
    asyncio.run(main())