import os
from dotenv import load_dotenv 
# essa função puxa os valores que estão dentro do arquivo .env e transforma em variáveis de ambiente

load_dotenv()  # chamamos a função para ela fazer o seu trabalho
 
print(os.getenv("MINHA_VARIAVEL"))