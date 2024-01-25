# Apache-Flink-para-processamento-em-tempo-real-de-dados-IoT-na-nuvem

Equipe: Cloud Computing

Integrantes:

HUMBERTO VITTORIO ALMEIDA GUADAGNINI (202204397) - hvittorioguadagnini@discente.ufg.br;

Luiza Martins de Freitas Cintra (202203520) - cintraluiza@discente.ufg.br;

Mateus Eduardo Silva Ribeiro (202203522) - mateus.eduardo@discente.ufg.br;

Isabela de Queiroz (202203512) - isabela.queiroz@discente.ufg.br;

Matheus Yosimura Lima (202203523) - matheusyosimura@discente.ufg.br;


## *Introdução:*
A "Internet das Coisas" (IoT) representa uma revolução na rede, expandindo sua abrangência para além dos computadores, incorporando objetos cotidianos. Suas aplicações abrangem telemetria, coleta de dados e interação direta com diversos dispositivos. A IoT está intimamente ligada ao conceito de "Big Data", envolvendo a geração contínua e massiva de dados por objetos e computadores, viabilizada pelo avanço dos protocolos de Internet, proporcionando a cada dispositivo um "endereço IP" próprio.

O Apache Flink é um mecanismo distribuído de código aberto projetado para processamento contínuo de dados ilimitados (fluxos) e limitados (lotes). Foi concebido visando baixa latência, execução de cálculos na memória, alta disponibilidade e escalabilidade horizontal. Seus atributos incluem um avançado gerenciamento de estado com garantias de consistência, semântica de processamento de tempo de evento e tratamento sofisticado de dados atrasados e fora de ordem. O Apache Flink destaca-se por ser especialmente adequado para a captura de picos de temperatura em ambientes conectados a sensores.

## *Descrição do Problema:*
O texto aborda a integração estratégica da Internet das Coisas (IoT) com a nuvem, com ênfase no papel vital do Apache Flink e dos sistemas operacionais. A IoT, ao expandir a conectividade para objetos cotidianos, gera enormes volumes de dados, dando origem ao desafio do "Big Data".

O Apache Flink, sendo um mecanismo distribuído, emerge como a solução para processamento em tempo real, especialmente em cenários práticos, como monitoramento ambiental com sensores de temperatura. Sua capacidade de escala horizontal e processamento distribuído o torna central em arquiteturas baseadas em nuvem.

A relação entre sistemas operacionais e IoT é evidente, destacando a importância do gerenciamento eficiente para a coleta de dados em tempo real e a tolerância a falhas. Mecanismos como pontos de verificação automática garantem a continuidade operacional em ambientes dinâmicos.

Em resumo, o problema delineia um contexto complexo onde a intersecção entre IoT, nuvem e sistemas operacionais é crucial. O Apache Flink surge como uma peça-chave para superar desafios, impulsionando eficiência e tomada de decisões informadas em tempo real.


## *Proposta de Solução:*
A pesquisa tem como objetivo central a construção de um sistema em tempo real para análise e geração de métricas baseadas em dados de temperatura residenciais, coletados periodicamente por sensores. A solução proposta consiste na implementação de um pipeline utilizando a biblioteca PyFlink em Python. Este pipeline será responsável por receber, analisar sistematicamente os dados e gerar métricas, apresentando-as por meio de dashboards intuitivos para os usuários da interface.

## *Fundamentos Teóricos:*
O Apache Flink é uma ferramenta versátil usada para criar aplicações de transmissão e em lotes. Suas aplicações incluem processamento orientado por eventos, análise de dados e pipelines de dados. Ele se destaca por processamento de fluxo de alto throughput e baixa latência, permitindo a criação de grafos complexos de fluxo de dados.

A tolerância a falhas é garantida por meio de checkpoints automáticos e periódicos, mantendo estados da aplicação para recuperação automática em falhas. O Apache Flink oferece benefícios como processamento de dados ilimitados e limitados, execução em grande escala, desempenho na memória e consistência de estado exatamente uma vez.

A IoT, por sua vez, utiliza a interconexão de objetos inteligentes. Esses objetos possuem unidades de processamento, comunicação, energia e sensores/atuadores. Sua arquitetura básica permite aplicações como coleta de dados, monitoramento de ambientes e diversos usos em setores como saúde, energia e transporte.

Essas tecnologias, quando aplicadas em conjunto, expandem as possibilidades para desenvolver soluções inteligentes em diversos campos, criando uma rede interligada de objetos na Internet das Coisas.

## *Metodologia: * 
O objetivo central da pesquisa construir em tempo real um meio de comunicação para que analisar e gerar métricas pautadas nos dados de temperatura residenciais e periódicos coletados por sensores, com seu sistemas individuais de processamento, com a finalidade de detectar picos inesperados. Portanto, fundamentalmente a solucão definida foi a construção de um pipeline na biblioteca de Python, PyFlink, 
que seja capaz de receber os dados coletados, analisá-los sistematicamente, gerar métricas em cima da coletas e ser capaz de apresentar dashboards de simples entendimento para informar o usuario da interface.

Ha utilização do Kafka para armazenar dados de entrada sobre temperatura. Um script atuando como gerador de dados simples para simular o recebimento de dados de uma IoT, chamado generate_source_data.py e fornecido para gravar em tempo real novos registros no temperature_msg tópico Kafka. Cada registro foi estruturado da seguinte forma: {"createTime": "2020-08-12 06:29:02", "orderId": 1597213797, "tempAmount":
29.159}
• createTime: A hora da criação.
• orderId: O id da temperatura atual.
• tempAmount: O valor da temperatura.
Os dados de temperatura serão processados com PyFlink usando o script Python temperature_msg.py. Este script primeiro mapeará os orderId registros e calcular a soma dos valores das transações para cada id. O ambiente é baseado no Docker Compose. Ele usa uma imagem personalizada para ativar o Apache Flink (JobManager + TaskManager), Kafka+Zookeeper, o gerador de dados e conteinêres ElasticSearch+Kibana.
Ademais, foi construída uma máquina virtual através do Amazon EC2, onde configurou-se uma imagem Docker e sendo baixadas todas as imagens das tecnologias mencionadas anteriormente. Apos a ambientação estar completa os serviços disponibilizaram no url http://localhost:8081 as métricas necessárias para análise. Durante todo o processo para o fortalecimento da metodologia foram realizados testes por grandes quantidades de tempo com temperaturas ficticías variadas.

## *Resultados e Conclusão:*
Por fim, obteve-se uma profunda quantidade amostral de dados capaz da geração de diversas métricas importantes para a análise. Sendo capaz, portanto, de aprofundar os saberes no tópico Apache Flink para processamento em tempo real de dados IoT na nuvem, sendo capaz futuramente de impulsionar trabalhos científicos interessados em utilizar dados oriundo de IoT e processados em tempo real na nuvem para automatizar
ambientes residenciais ou empresariais. Os resultados obtidos foram muito satisfatórios para o esperado do projeto, as métricas apresentadas estavam de acordo com o esperado do espaço amostral com uma eficácia de 100%. Portanto, conclui-se a oportunidade tecnológica para um cenário que apresenta como core este processamento, sem a necessidade da utilização de recursos locais.

## *Referências:*
[1] Faccioni Filho, Mauro. ”Internet das coisas.” Unisul Virtual(2016)
[2] https://aws.amazon.com/pt/what-is/apache-flink/
[3] Santos, Bruno P., et al. ”Internet das coisas: da teoria a prática.” 
Minicursos SBRC-Simpósio Brasileiro de Redes de Computadores e 
Sistemas Distribuídos 31 (2016): 16.
[4] Santaella, Lucia, et al. ”Desvelando a Internet das coisas.” Revista
GEMInIS 4.2 (2013): 19-32.
[5] https://github.com/apache/flink-playgrounds/tree/master/pyflinkwalkthrough
[6] https://thingspeak.com/channels/public
[7] https://medium.com/@daeynasvistas/a-iot-internet-das-coisas-surgiucomo-a-nova-gera
[8] https://www.confluent.io/blog/apache-flink-stream-processing-use-caseswith-examples/
