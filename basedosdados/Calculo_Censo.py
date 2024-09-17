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