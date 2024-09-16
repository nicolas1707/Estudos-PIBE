import basedosdados as bd
import pandas as pd
import os
from billing_id import Id_Faturamento

# Lista de estados do Brasil
estados = ['AC']

# Intervalo de anos de 2008 até 2024
anos = list(range(2020, 2025))

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