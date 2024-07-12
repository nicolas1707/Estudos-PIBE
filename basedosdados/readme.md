# [basedosdados.org](https://basedosdados.org/)

A Base dos Dados é uma ONG que cataloga e organiza dados públicos do Brasil em um datalake no Google Big Query (uma serviço de hospedagem de dados com suporte à SQL).

Você pode acessar os dados tanto pelo serviço do Google Big Query, quanto por bibliotecas python, R e Stata. 

O objetivo desse módulo é aprender como criar um projeto no Google Cloud, criar uma chave de acesso e conseguir baixar os dados disponibilizados por eles. 

Gostei dessa base pois eles tem uma documentação legal e vídeos no youtube. 


## Importante

Quando estamos acessando dados na nuvem, uma das maneiras de fazer isso é usando chaves de acesso. Essas chaves devem permanecer ocultas dentro do nosso código. Para isso, utilizamos as _variáveis de ambiente_.

No `python`, podemos utilizar o pacote `dotenv` para gerenciar essas variáveis de ambiente. 


## Variáveis de ambiente

Tanto no linux quanto no windows, temos as variáveis de ambiente. São variáveis utilizadas para configurar o computador e podem ser lidas por quaisquer programas que estejam rodando na máquina. 

No terminal normal, podemos listar todas as variáveis com o comando `env`

Para acessar o valor de uma variável, utilizamos o símbolo do sifrão `$` antes do nome da variável. Por exemplo, a variável `HOME` contém o caminho para a pasta home do usuário logado. Se você quiser acessar o valor dessa variável em um terminal ou um script, basta escrever `$HOME`. 

Se eu quiser imprimir o valor da variável na tela, posso usar o comando echo

```shell
echo $HOME
```

## Acessando variáveis de ambiente no `python`

No python, podemos acessar as variáveis utilizando o pacote padrão `os`. O código abaixo, pega o valor da variável `HOME` e imprime na tela.

```python
import os
home = os.getenv("HOME") # captura o valor da variável HOME
print(home)
```

## O pacote `dotenv`

Quando você criar sua conta no Google Cloud, vai criar uma chave de acesso, que deve ser privada e não pode subir pro Github de jeito nenhum. 

Como então criar uma maneira de ocultar sua chave e mesmo assim publicar o seu código?

Para isso, vamos armazenar sua chave em uma arquivo `.env` separado do seu código principal. Esse arquivo também não vai ser indexado pelo git, pois colocaremos ele dentro do `.gitignore`. 

### Minitutorial `dotenv`

1. Crie um aquivo `.env` (sem nome mesmo, só a extensão, isso faz com que ele fique oculto em sistemas linux);
2. Dentro desse arquivo, escreva o seguinte conteúdo
```
MINHA_VARIAVEL=valorsupersecreto
```
3. Crie um ambiente virtual aqui nesse diretório e instale os `requirements.txt`
4. Crie um arquivo python com o seguinte conteúdo

```python
import os
from dotenv import load_dotenv 
# essa função puxa os valores que estão dentro do arquivo .env 
# e transforma em variáveis de ambiente

load_dotenv()  # chamamos a função para ela fazer o seu trabalho
 
print(os.getenv("MINHA_VARIAVEL"))
```
5. Ao executar o código acima, deve aparecer na tela `valorsupersecreto`

Dessa forma, você pode armazenar a sua chave secreta numa variável dentro do `.env`, acessar esse valor dentro do script python e não publicar ele no github.

## Roteiro de estudos

1. Acesse a [Documentação](https://basedosdados.github.io/mais/) do Base dos Dados. 
2. Faça um resumo dessa documentação em um arquivo `basedosdados.md` aqui nesse diretório. 
3. Como você gosta de aprender por videos-tutoriais, pode acessar o [canal do youtube](https://www.youtube.com/c/BasedosDados/featured) e procurar pela playlist "Aprendendo com a BD"

O objetivo principal dessa primeira parte é:
1. Configurar sua conta na Google Cloud;
2. Obter uma chave de acesso;
3. Instalar o pacote `basedosdados` no python;
4. Escolher um conjunto de dados do seu interesse;
5. Conseguir baixar esse pacote de dados utilizando um script python.;

