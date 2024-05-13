# Ambientes virtuais

Os `virtual environments` (ou `venvs`) são ambientes python que ficam isolados da instalação python do seu sistema.

Ao criar um `venv`, é criada uma pasta dentro do diretório do seu projeto que contém uma instalação nova do python e todas as suas dependências.

Eles permitem a reproducibilidade do seu código, uma vez que você lista todas as dependências do mesmo.

## Criando um `venv`

No terminal, usamos o comando 

```bash
python3 -m venv nome_do_venv
```

Esse comando cria uma pasta chamada `nome_do_venv` dentro da pasta atual e instala o python ali dentro. 

## Ativando o `venv`

Após criado o `venv`, precisamos ativá-lo. No terminal, usamos o comando 

```bash
source nome_do_venv/bin/activate
```
Quando o `venv` for ativado, aparecerá o nome dele no começo do `prompt de comando`, tipo

```console
(nome_do_venv) ~/Estudos-python/ambientes-virtuais/ $
```

## Desativando o `venv`

No terminal, utilizamos o comando

```bash
deactivate
```

## Instalando dependências

Dependências são os pacotes extra que instalamos num projeto. 

Você pode instalar de duas maneiras.

### Listando a dependência

Após ativar o `venv`, utilize o comando
```bash
python -m pip install NomeDaDependência
```

> Note que depois que o `venv` foi ativado, trocamos o comando `python3` por `python`

### Utilizando um `requirements.txt`

Muitos projetos vem com um arquivo `requirements.txt` no diretório principal. Ele lista as dependências do seu projeto. 

Nesse caso, com o `venv` ativado, utilizamos o comando 
```bash
python -m pip install -r requirements.txt
```

## Listando os pacotes instalados

Para listar os pacotes que foram instalados no ambiente virtual, ativamos o mesmo e utilizamos o comando

```bash
python -m pip freeze
```


## Tutorial

Nesse tutorial, vamos criar não 1, mas 2 ambientes virtuais no mesmo diretório. 

1. Crie um venv chamado `venv1`

```bash
python3 -m venv venv1
```

2. Ative o `venv1` e instale a dependência `numpy`

```bash
source venv1/bin/activate
python -m pip install numpy
```

3. Entre no terminal do `python` digitando `python` na linha de comando e verifique que o módulo `numpy` foi instalado, executando os comandos abaixo 

```python-repl
>>> import numpy as np
>>> print(np.pi)
3.141592653589793
```
4. Desative o `venv1`

```bash
deactivate
```

5. Crie um `venv2`, ative-o e instale as dependências listadas em `requirements.txt`

```bash
python3 -m venv venv2
source venv2/bin/activate
python -m pip install -r requirements.txt
```

6. Abra o terminal do python e veja que o pandas foi corretamente instalado.

```python-repl
>>> import pandas as pd
>>> print(pd.__version__)
2.2.2
```

Note que na instalação do `pandas`, foram instalados vários outros pacotes, que são dependências do pandas.

```
Successfully installed numpy-1.26.4 pandas-2.2.2 python-dateutil-2.9.0.post0 pytz-2024.1 six-1.16.0 tzdata-2024.1
```

Assim, se você executar o comando 
```python-repl
>>> import numpy as np
>>> print(np.pi)
3.141592653589793
```
dentro do `venv2`, ele não irá retorar nenhum erro, pois o numpy foi instalado como dependência do `pandas`.

6. Agora, se você desativar o `venv2`, ativar o `venv1`, abrir o terminal do python e executar
```python-repl 
>>> import pandas as pd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```
Veja que temos um erro de Módulo Não Encontrado. 