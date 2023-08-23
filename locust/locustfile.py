from locust import HttpUser, TaskSet, task
import pika

class RabbitMQTaskSet(TaskSet):
    def on_start(self):
        # Chamada quando o usuário inicia a tarefa. Aqui, estabeleceremos uma conexão RabbitMQ.
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='teste-carga', durable=True)

    def on_stop(self):
        # Chamada quando o usuário encerra a tarefa. Aqui, fecharemos a conexão RabbitMQ.
        self.connection.close()

    @task
    def enviar_para_fila(self):
        self.channel.basic_publish(exchange='',
                                   routing_key='teste-carga',
                                   body='Mensagem de teste')
        print("Mensagem enviada para a fila")

class RabbitMQUser(HttpUser):
    tasks = [RabbitMQTaskSet]
    min_wait = 500
    max_wait = 1000
