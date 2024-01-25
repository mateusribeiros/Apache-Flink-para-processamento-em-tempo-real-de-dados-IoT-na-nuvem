from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.table import StreamTableEnvironment, DataTypes
from pyflink.table.udf import udf

def process_data(t_env):
    try:
        # Define a DDL para criar uma tabela de origem Kafka chamada 'temperature_msg'
        create_kafka_source_ddl = """
            CREATE TABLE temperature_msg(
                createTime VARCHAR,
                orderId BIGINT,
                tempAmount DOUBLE
            ) WITH (
              'connector' = 'kafka',
              'topic' = 'temperature_msg',
              'properties.bootstrap.servers' = 'kafka:9092',
              'properties.group.id' = 'test_3',
              'scan.startup.mode' = 'latest-offset',
              'format' = 'json'
            )
            """

        # Define a DDL para criar uma tabela de destino Elasticsearch chamada 'es_sink'
        create_es_sink_ddl = """
                CREATE TABLE es_sink(
                    orderId BIGINT PRIMARY KEY,
                    temp_amount DOUBLE
                ) with (
                    'connector' = 'elasticsearch-7',
                    'hosts' = 'http://elasticsearch:9200',
                    'index' = 'platform_temp_amount_1',
                    'document-id.key-delimiter' = '$',
                    'sink.bulk-flush.max-size' = '42mb',
                    'sink.bulk-flush.max-actions' = '32',
                    'sink.bulk-flush.interval' = '1000',
                    'sink.bulk-flush.backoff.delay' = '1000',
                    'format' = 'json'
                )
        """

        # Executa a DDL para criar as tabelas de origem Kafka e de destino Elasticsearch
        t_env.execute_sql(create_kafka_source_ddl)
        t_env.execute_sql(create_es_sink_ddl)

        # Define uma consulta Flink SQL para calcular a temperatura média e inserir em 'es_sink'
        t_env.from_path("temperature_msg") \
            .select("tempAmount") \
            .group_by() \
            .select("avg(tempAmount) as avg_temperature") \
            .execute_insert("es_sink")

    except Exception as e:
        print(f'Erro: {e}')  # Declaração de impressão de exceções que ocorrem durante o processo

if __name__ == '__main__':
    # Configura o StreamExecutionEnvironment e o StreamTableEnvironment
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(stream_execution_environment=env)
    t_env.get_config().get_configuration().set_boolean("python.fn-execution.memory.managed", True)

    # Chama a função de processamento de dados
    process_data(t_env)

    print("Execução concluída.")
