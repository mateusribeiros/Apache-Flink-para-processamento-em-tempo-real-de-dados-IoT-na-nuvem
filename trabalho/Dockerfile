# Usa a imagem base do Apache Flink com a versão 1.16.0, Scala 2.12 e Java 8
FROM apache/flink:1.16.0-scala_2.12-java8

# Argumento para especificar a versão do Flink
ARG FLINK_VERSION=1.16.0

# Instalação de dependências e configuração do ambiente Python
RUN set -ex; \
  apt-get update && \
  apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libffi-dev lzma liblzma-dev && \
  wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz && \
  tar -xvf Python-3.7.9.tgz && \
  cd Python-3.7.9 && \
  ./configure --without-tests --enable-shared && \
  make -j4 && \
  make install && \
  ldconfig /usr/local/lib && \
  cd .. && rm -f Python-3.7.9.tgz && rm -rf Python-3.7.9 && \
  ln -s /usr/local/bin/python3 /usr/local/bin/python && \
  ln -s /usr/local/bin/pip3 /usr/local/bin/pip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  python -m pip install --upgrade pip; \
  pip install apache-flink==${FLINK_VERSION}; \
  pip install kafka-python;

# Download dos conectores do Flink para JSON, Kafka e Elasticsearch
RUN wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-json/${FLINK_VERSION}/flink-json-${FLINK_VERSION}.jar; \
    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/${FLINK_VERSION}/flink-sql-connector-kafka-${FLINK_VERSION}.jar; \
    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-elasticsearch7/${FLINK_VERSION}/flink-sql-connector-elasticsearch7-${FLINK_VERSION}.jar;

# Configuração adicional do Flink: aumenta o tamanho da metaspace da JVM do TaskManager
RUN echo "taskmanager.memory.jvm-metaspace.size: 512m" >> /opt/flink/conf/flink-conf.yaml;

# Define o diretório de trabalho como /opt/flink
WORKDIR /opt/flink
