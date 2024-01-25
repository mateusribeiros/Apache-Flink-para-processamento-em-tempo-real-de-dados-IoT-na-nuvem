# Usa a imagem Python 3.7 Alpine como base
FROM python:3.7-alpine

# Executa os comandos seguintes de forma verbose (-ex)
RUN set -ex; \
  # Atualiza o pip para a versão mais recente
  python -m pip install --upgrade pip; \
  # Instala a biblioteca kafka-python usando o pip
  pip install kafka-python;

# Adiciona o arquivo generate_source_data.py ao diretório raiz do contêiner
ADD generate_source_data.py /

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "-u", "./generate_source_data.py"]
