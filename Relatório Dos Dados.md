

# Relatório: Download e Organização de Dados do Censo Escolar Usando a Base dos Dados

## Objetivo
O objetivo foi baixar e organizar os dados do Censo Escolar, disponíveis na plataforma [Base dos Dados](https://basedosdados.org/), utilizando a API do BigQuery, filtrando por estado e ano. Os dados foram baixados em formato CSV e organizados em pastas, separadas por estado e ano.

## IMPORTANTE
__Modo de Simulação (Query Validator)__


Antes de executar uma consulta, o BigQuery permite que vejamos uma estimativa do tamanho de dados que será processado. Isso pode te ajudar a entender se a consulta ultrapassará o limite gratuito. 


__No console do BigQuery:__

- Abra a página de consulta SQL.

- Escreva a sua consulta.

- No canto direito, ao lado do botão "Run", clique no ícone de "Query Validator" (um pequeno link com uma linha dizendo "This query will process X GB").

- O BigQuery mostrará quantos gigabytes (GB) a consulta processará. Se esse número ultrapassar os 1 TB mensais gratuitos (ou o limite da sua conta), você será cobrado.


__Script de validação:__

- Instale a biblioteca `google-cloud-bigquery`
- Execute o script:
```python
import os
from google.cloud import bigquery

# Função para calcular o tamanho estimado da consulta
def calcular_tamanho_query(estado, ano, dataset_id, table_id, project_id):
    # Inicializar o cliente do BigQuery
    client = bigquery.Client(project=project_id)

    # Definir a query para o estado e ano especificado
    query = f"""
    SELECT *
    FROM `{dataset_id}.{table_id}`
    WHERE sigla_uf = '{estado}' AND ano = {ano}
    """

    # Configurar a consulta para rodar como 'dry run' (simulação)
    job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)

    # Executar a consulta em modo dry run
    query_job = client.query(query, job_config=job_config)

    # Retornar o tamanho em bytes
    return query_job.total_bytes_processed

# Definir os estados e anos de interesse
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 
           'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']  # Adicione os estados desejados
anos = list(range(2008, 2025))  # Adicione os anos desejados

# Dataset e tabela
dataset_id = 'basedosdados.br_inep_censo_escolar'
table_id = 'escola'
project_id = 'download-dos-dados-inep'

# Calcular o total de dados processados
total_bytes = 0

for estado in estados:
    for ano in anos:
        bytes_processados = calcular_tamanho_query(estado, ano, dataset_id, table_id, project_id)
        total_bytes += bytes_processados
        # Converter para gigabytes
        gigabytes_processados = bytes_processados / (1024 ** 3)
        print(f'Estado: {estado}, Ano: {ano}, Dados processados: {gigabytes_processados:.2f} GB')

# Total em GB
total_gigabytes = total_bytes / (1024 ** 3)
print(f'Total de dados a serem processados: {total_gigabytes:.2f} GB')
````


## Passos Para o Download

### 1. **Criação de Ambiente Virtual no VS Code**

Foi criado um ambiente virtual para isolar as dependências do projeto.

- **Comando no terminal**:
    ```bash
    python -m venv venv
    ```

- **Ativação do ambiente virtual**:

    - **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

### 2. **Instalação das Bibliotecas Necessárias**

As bibliotecas `basedosdados` e `pandas` foram instaladas para manipulação e download de dados.

- **Comando no terminal**:
    ```bash
    pip install basedosdados pandas
    ```

### 3. **Configuração Manual das Credenciais do Google Cloud**

Como o comando `basedosdados configure` foi removido das versões recentes, fizemos a configuração manual das credenciais.

#### 3.1. **Download do Arquivo de Credenciais**

- O arquivo de credenciais JSON foi baixado do Google Cloud Console, em:
    - `IAM & Admin` > `Service Accounts` > Gerar Chave.

#### 3.2. **Definição da Variável de Ambiente**

O arquivo de credenciais foi configurado através da variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`.

- **Comando no terminal**:
    - **Linux/macOS**:
        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS=/caminho/para/suas/credenciais.json
        ```

A variável de ambiente informa à biblioteca onde encontrar o arquivo JSON para autenticação no Google Cloud.

### 4. **Especificação do Project ID**

No código Python, foi necessário especificar o `billing_project_id`, que é o ID do projeto de cobrança no Google Cloud, utilizado para acessar os dados via BigQuery.

- **Exemplo no código**:
    ```python
    df = bd.read_sql(query, billing_project_id='Id_Faturamento')
    ```
    *__Id_Faturamento__ está salvo em um __arquivo oculto__

### 5. **Execução do Script Python**

O script Python foi criado para baixar os dados filtrados por estado e ano, e salvá-los em pastas organizadas. Aqui está o código utilizado:

```python
import basedosdados as bd
import pandas as pd
import os
from billing_id import Id_Faturamento

# Lista de estados do Brasil
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 
           'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Intervalo de anos de 2008 até 2024
anos = list(range(2008, 2025))

# Tabela do censo escolar (verifique o dataset_id e table_id)
dataset_id = 'br_inep_censo_escolar'
table_id = 'escola'

# Diretório base onde os dados serão salvos
base_dir = 'censo_escolar_dados'

# Criar o diretório base se não existir
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for estado in estados:
    for ano in anos:
        # Filtrar por estado e ano
        query = f"""
        SELECT *
        FROM `basedosdados.{dataset_id}.{table_id}`
        WHERE sigla_uf = '{estado}' AND ano = {ano}
        """

        # Fazer o download dos dados usando a API
        try:
            df = bd.read_sql(query, billing_project_id='Id_Faturamento')

            # Definir o caminho da pasta e do arquivo CSV
            pasta_estado_ano = os.path.join(base_dir, f'{estado}-{ano}')
            if not os.path.exists(pasta_estado_ano):
                os.makedirs(pasta_estado_ano)
            
            caminho_csv = os.path.join(pasta_estado_ano, f'{estado}_{ano}.csv')

            # Salvar os dados em CSV
            df.to_csv(caminho_csv, index=False)

            print(f'Dados de {estado}-{ano} salvos em {caminho_csv}')

        except Exception as e:
            print(f'Erro ao processar {estado}-{ano}: {e}')
