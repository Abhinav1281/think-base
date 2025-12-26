import importlib
import json
import os
import sys
import time

import pika

from .ingest import ingest_message

accessories = importlib.import_module(".accessories", package="Accessories")
logger = accessories.logger

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE")
RABBITMQ_DEFAULT_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.getenv("RABBITMQ_DEFAULT_PASS")

# Log resolved RabbitMQ configuration for easier debugging
logger.info(
    f"RabbitMQ config -> host: {RABBITMQ_HOST}, queue: {RABBITMQ_QUEUE}, user: {RABBITMQ_DEFAULT_USER}"
)


def start_consumer():
    logger.info(f"Connecting to RabbitMQ at {RABBITMQ_HOST}...")
    credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)
    connParam = pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)

    connection = None

    while True:
        try:
            connection = pika.BlockingConnection(connParam)
            break
        except pika.exceptions.AMQPConnectionError:
            logger.error("RabbitMQ not available, retrying in 5 seconds...")
            time.sleep(5)

    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    def __callback(ch, method, properties, body):
        logger.info(f"Received message : {body}")
        data = json.loads(body)
        logger.info(f"[x] Received: {data}")
        ingest_message(data)
        logger.info(" [x] Done")

    channel.basic_consume(
        queue=RABBITMQ_QUEUE, on_message_callback=__callback, auto_ack=True
    )
    logger.info(" [*] Waiting for messages. To exit press CTRL+C")

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
