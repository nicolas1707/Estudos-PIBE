import subprocess
from datetime import datetime

args = ["ping", "www.yahoo.com"]

try:
    # Inicia o processo
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Lê a saída do processo em tempo real
    start_time = datetime.now()
    while True:
        # Verifica se o tempo limite de 30 segundos foi excedido
        elapsed_time = datetime.now() - start_time
        if elapsed_time.total_seconds() > 30:
            print("O processo excedeu o tempo limite de 30 segundos.")
            process.kill()  # Termina o processo se exceder o tempo limite
            break

        # Lê uma linha da saída do processo
        line = process.stdout.readline()
        if not line:
            break  # Se não houver mais linhas para ler, sai do loop
        print(line, end="")  # Imprime a linha lida

    # Captura possíveis erros
    stdout, stderr = process.communicate()
    
    # Verifica se houve erro
    if stderr:
        print("Erro:", stderr)

except subprocess.TimeoutExpired:
    print("O processo excedeu o tempo limite de 30 segundos.")
    process.kill()  # Termina o processo se exceder o tempo limite
