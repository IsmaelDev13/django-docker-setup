import pika, json, os, django
from products.models import Product
import environ
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

env = environ.Env()
environ.Env.read_env()

params =pika.URLParameters(env("CLOUD_AMPQ"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes  =product.likes+1
    product.save()
    print("Product liked!")

channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()