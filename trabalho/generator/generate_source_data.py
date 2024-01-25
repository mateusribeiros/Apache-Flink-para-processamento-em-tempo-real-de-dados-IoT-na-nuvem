import random
import time, calendar
from random import randint
from kafka import KafkaProducer
from kafka import errors 
from json import dumps
from time import sleep

def write_data(producer):
    # Número total de dados a serem gerados
    data_cnt = 20000
    # Cria um ID de pedido baseado no tempo atual em segundos
    order_id = calendar.timegm(time.gmtime())
    # Temperatura máxima para gerar dados aleatórios
    max_temp = 100
    # Tópico Kafka para enviar os dados
    topic = "temperature_msg"

    for i in range(data_cnt):
        # Obtém a data e hora formatadas
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # Gera um número aleatório para simular dados de temperatura
        rd = random.random()
        # Incrementa o ID do pedido
        order_id += 1
        # Calcula a quantidade de temperatura com base no número aleatório gerado
        temp_amount = max_temp * rd
        # Cria um dicionário representando os dados atuais
        cur_data = {"createTime": ts, "orderId": order_id, "tempAmount": temp_amount}
        # Envia os dados para o tópico Kafka especificado
        producer.send(topic, value=cur_data)
        # Aguarda por meio segundo antes de enviar o próximo conjunto de dados
        sleep(0.5)

def create_producer():
    print("Conectando aos brokers do Kafka")
    for i in range(0, 6):
        try:
            # Cria um produtor Kafka com os servidores especificados e um serializador JSON
            producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
            print("Conectado ao Kafka")
            return producer
        except errors.NoBrokersAvailable:
            print("Aguardando a disponibilidade dos brokers")
            # Aguarda 10 segundos antes de tentar novamente
            sleep(10)

    # Lança uma exceção se não conseguir se conectar aos brokers dentro de 60 segundos
    raise RuntimeError("Falha ao se conectar aos brokers em 60 segundos")

if __name__ == '__main__':
    # Cria um produtor Kafka
    producer = create_producer()
    # Chama a função para gerar e enviar dados para o tópico Kafka
    write_data(producer)
