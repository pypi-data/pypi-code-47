#!/usr/bin/env python
import argparse
from   paho.mqtt.client import Client

def print_publish_info(client, userdata, message_id):
    print(f'message id: {message_id}')

def main():
    parser = argparse.ArgumentParser(description='Command line utility for quick MQTT publishes')
    parser.add_argument('--broker-port', type=int, default=1883)
    parser.add_argument('broker_address')
    parser.add_argument('topic')
    parser.add_argument('message', default='')
    args = parser.parse_args()

    client = Client()
    client.on_publish = print_publish_info
    client.connect(args.broker_address, args.broker_port)
    client.publish(args.topic, args.message)
    client.disconnect()


if __name__ == '__main__':
    main()
