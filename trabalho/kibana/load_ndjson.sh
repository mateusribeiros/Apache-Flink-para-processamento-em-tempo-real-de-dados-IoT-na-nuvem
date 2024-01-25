#!/bin/bash

# Loop até que o endpoint http://kibana:5601/login esteja acessível
until curl -s http://kibana:5601/login -o /dev/null; do
    echo Esperando pelo Kibana...
    sleep 10
done

# Aguarda mais 20 segundos após o Kibana estar acessível
sleep 20

# Realiza uma solicitação POST para importar objetos salvos no Kibana usando um arquivo NDJSON
curl -X POST kibana:5601/api/saved_objects/_import -H "kbn-xsrf: true" --form file=@/tmp/load/export.ndjson

# Imprime uma mensagem indicando que a carga foi concluída
echo 'Tudo carregado'
