import pika, json, os, time

def start_consumer():
    rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')
    print(f"Connecting to RabbitMQ at {rabbitmq_host}...",flush=True)
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            break
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not available, retrying in 5 seconds...")
            time.sleep(5)
    channel = connection.channel()
    channel.queue_declare(queue='ingest_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f"Received message : {body}", flush=True)
        data = json.loads(body)
        print(f"[x] Received: {data}",flush=True)
        # TODO: Add chunking + indexing logic here

    channel.basic_consume(queue='ingest_queue', on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()