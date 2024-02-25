# Simulação do Protocolo MQTT com Sensor de Radiação Solar HOBOnet RXW-LIB-900

Este projeto tem como objetivo simular a comunicação MQTT utilizando dados simulados provenientes do sensor de radiação solar HOBOnet RXW-LIB-900. A aplicação gera mensagens MQTT a partir de dados fictícios do sensor e as envia para um broker MQTT.

## Detalhes do Sensor

O sensor de radiação solar HOBOnet RXW-LIB-900 é utilizado para medir a intensidade da radiação solar. Este projeto simula a geração de dados realistas a partir deste sensor e envia esses dados para um broker MQTT.

## Requisitos

- Python 3.x
- Biblioteca `paho-mqtt` (instalável via `pip install paho-mqtt`)

## Estrutura do Projeto

- `csv_reader.py`: Módulo responsável pela leitura de dados a partir de um arquivo CSV.
- `publisher.py`: Módulo contendo funções para iniciar o cliente MQTT e enviar mensagens para um tópico MQTT.
- `simulation.csv`: Dados ficticios do sensor.
- `main.py`: Script principal que utiliza os módulos acima para ler dados do CSV e enviar mensagens MQTT simuladas.

## Configuração

1. Instale as dependências usando o seguinte comando:
    ```
    pip install -r requirements.txt
    ```

2. Execute o script principal `main.py` para iniciar a simulação e o publisher.
    ```
    python3 main.py
    ```
3. Execute o script `subscriber.py` para receber a mensagem.
    ```
    python3 subscriber.py
    ```
## Tests
Testes unitarios de casos para publisher e subscriber, onde são testados items como validação de envio e recebimento de mensagem, e perfomance do subscriber.

### Para executar

1. Execute o script de teste todos os casos:
    ```
    pytest test_cases.py
    ```
## Demonstrações

[Assista a Demonstração Local](https://drive.google.com/file/d/1_2yDsDVj2sjO9qUikU3xUrpuAW4xCzYP/view?usp=sharing)

[Assista a Demonstração HiveMQ](https://drive.google.com/file/d/1ohYb8gyiSkReY6O0R_WIRcS-MGjz7nFl/view?usp=sharing)