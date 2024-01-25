# Usa a imagem Alpine Linux versão 3.6 como base
FROM alpine:3.6

# Instalação do wget, unzip e curl usando o gerenciador de pacotes 'apk'
RUN apk update && apk add bash curl && rm -rf /var/cache/apk/*

# Cria um diretório chamado /tmp/load/
RUN mkdir -p /tmp/load/

# Move o arquivo de configuração 'export.ndjson' para dentro do contêiner no diretório /tmp/load/
COPY ./export.ndjson /tmp/load/export.ndjson

# Move o script 'load_ndjson.sh' para dentro do contêiner no diretório /tmp/load/
COPY ./load_ndjson.sh /tmp/load/load_ndjson.sh

# Concede permissões de leitura, gravação e execução para todos os usuários nos arquivos dentro do diretório /tmp/load/
RUN chmod -R 777 /tmp/load/*
