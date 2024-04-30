# Estudos-python


 Link para ínicio dos estudos: [python 101](https://python101.pythonlibrary.org/)

Guia: Criar um resumo para cada capítulo e testar os comandos do tutorial diretamente no terminal do vscode (comando `python3` para iniciar o terminal do python, e utilizar o comando `CTRL+D` para voltar ao terminal normal). -> Para acessar, usamos CTRL+SHIFT+P e buscamos Create New Terminal

Notas: Se quisermos verificar algum teste no compilador, igual fazemos nas linhas de comando, usamos print("comando") caso este comando apareça alguma mensagem feita pelo python. No python, sempre que formos fazer uma estrutura de programa nas linhas de comando, devemos respeitar os __espaçamentos__ dados pela tecla __TAB__.

## Parte 1: Aprendendo o Básico

### 1) Capítulo 1: Programação IDLE 
- __Usando IDLE__

 Python, por ser uma linguagem interpretativa, utiliza de elementos próprios e não utiliza outros como compiladores. No caso, um que é utilizado é o chamado **IDLE**, que funciona como um editor de código, destacando, depurando e até mesmo preenchendo automaticamente algumas áreas do código.

- __Sobre comentários__

Comentários são de extrema importância para caso alguém queira fazer algum comentário em alguma linha de código, tanto para relembrar algo ou para fazer alguma observação.


### 2) Capítulo 2: Tudo sobre strings

- __Como criar uma string__

 De início podemos fazer strings usando aspas duplas simples e triplas, sendo que as aspas triplas (''') nos proporcionam a opção de continuar a string em outra linha do comando. Outra forma também é utilizando o comando str (informação) no qual podemos guardar as informações já registradas em outro lugar em uma string, esse método é conhecido como **fundição** *(1)*. Strings são imutáveis, ou seja, mesmo se atribuirmos uma definição diferente, mas para um mesmo nome de string, sua **identidade** muda, não sendo mais o mesmo ID daquela string anterior na qual definimos *(2)*.

_(1)_
```py
>>> meu_número  =  123 
>>> minha_string  =  str ( meu_número )
```
_(2)_
```py
>>> minha_string  =  "abc" 
>>> id ( minha_string ) 
19397208 
>>> minha_string  =  "def" 
>>> id ( minha_string ) 
25558288 
>>> minha_string  =  minha_string  +  "ghi" 
>>> id ( minha_string ) 
31345312
```
- __Concatenar (ou somar) strings__

 Em python para somar strings, ou seja, ajuntar uma na outra, apenas é necessário definir cada uma que queiramos somar, e uma que utilizaremos para guardar, e depois utilizar o operador **soma (+)**.

```py
>>> string_one  =  "Meu cachorro comeu" 
>>> string_two  =  " meu dever de casa!" 
>>> string_três  =  string_um  +  string_dois
```
- __Métodos string__

 Por uma string ser um objeto me python, podemos modificar uma string utilizando comandos simples como **upper() lower() strip()** e etc. Estes comandos modificam nossa string e o conteúdo dela, e para saber todos os comandos possíveis utilizamos um comando específico _(3)_. Os métodos que começam e terminam com "__" não são muito utilizados, mas caso queiramos saber para o que cada um serve 
basta utilizar outro comando _(4)_.

_(3)_
```py
 >>> dir(my_string)
 ```
_(4)_
 ```py
 >>> help(my_string.capitalize)
```
- __Fatiamento de strings__

 Fatiamento de string é um método utilizado para mostrar apenas algumas **partes específicas** da string na qual queremos **visualizar**, em visualização fica mais fácil de entender como demonstrado no bloco de código _(5)_. No caso, podemos fatiar especificando o ínicio, o final, ou ambos. Isso vai depender do que queremos que saia no final. Também podemos acessar caracteres individuais de uma string utilizando `printf(minha_string[n])`, sendo n o número do caractere.

_(5)_
```py
>>> my_string = 'I like Python!'
>>> my_string[:1]
'I'
>>> my_string[0:12]
'I like Pytho'
>>> my_string[0:13]
'I like Python'
>>> my_string[0:14]
'I like Python!'
>>> my_string[0:-5]
'I like Py'
>>> my_string[:]
'I like Python!'
>>> my_string[2:]
'like Python!'
```
- __Formatação de string__

 Também conhecida como substiuição, a formatação serve para substituir os valores de uma string base. Na maioria das vezes, você inserirá strings dentro de strings, no entanto, você também inserirá números inteiros e flutuantes em strings com bastante frequência. Aqui temos um exemplo usual de como isso ocorre na prática _(6)_, aqui basicamente mudamos nosso %s para %(lang)s, que é basicamente o %s com uma variável dentro dele. Outro exemplo de substituição é utilizando **format**, no qual aparenta ser mais completo como a seguir _(7)_. Este último exemplo usa um dicionário como usamos no modelo anterior (que são as definições de x e y). No entanto, temos que extrair o dicionário usando o asterisco duplo para que funcione corretamente aqui.

_(6)_
```py
>>> print ( " %(lang)s é divertido!"  %  { "lang" : "Python" })
'Python é divertido!'
```

_(7)_
```py
>>> "Python é tão simples quanto {0}, {1}, {2}" . format ( "a" ,  "b" ,  "c" ) 
'Python é tão simples quanto a, b, c' 
>>> "Python é tão simples quanto {1}, {0}, {2}" . format ( "a" ,  "b" ,  "c" ) 
'Python é tão simples quanto b, a, c' 
>>> xy  =  { "x" : 0 ,  "y" : 10 } 
>>> print ( " Faça um gráfico de um ponto onde x={x} e y={y}" . format ( ** xy )) 
Faça um gráfico de um ponto onde x=0 e y=10
```

Há muitas outras coisas que você pode fazer com strings, como especificar uma largura, alinhar o texto, converter para bases diferentes e muito mais. Certifique-se de dar uma olhada em algumas das referências no fim do capítulo desta aula.


### 3) Capítulo 3: Listas, Tuplas e Dicionários

- __Listas__

 Uma lista é semelhante a um "array" e pode ser criada de duas maneiras:

```py
>>> minha_lista  =  [] 
>>> minha_lista  =  list ()
```
Uma lista contém elementos como strings, inteiros e objetos, podendo conter todos misturados inclusive. O que podemos fazer também, é criar listas de listas:

```py
>>> minha_lista_nested  =  [ minha_lista ,  minha_lista2 ] 
>>> minha_lista_nested 
[[1, 2, 3], ['a', 'b', 'c']]
```

Podemos também usar diferentes métodos para combinar duas listas como o método __extend__ ou apenas utilizando o operador __+__:

```py
>>> minha_lista  =  [ 1 ,  2 ,  3 ] 
>>> minha_lista2  =  [ "a" ,  "b" ,  "c" ] 
>>> combo_list  =  minha_lista  +  minha_lista2 
>>> combo_list 
[1, 2, 3, ' a', 'b', 'c']
```

Outra coisa que podemos fazer é classificar uma lista usando o comando __lista.sort()__, porém, se tentarmos atribuir uma lista classificada a outra variável qualquer teremos como resultado __None__ (ou NULL), ou seja, não podemos atribuir ela a uma variável diferente.

Além disso, também podemos "fatiar" uma lista com os mesmos comandos que usamos nas strings.

- __Tuplas__

Tuplas são semelhante a listas, mas são criadas com parenteses ao invés de colchetes. A diferença é que uma tupla é __imutável__, como podemos ver no exemplo a seguir:

```py
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple[0:1]
(1, 2, 3)
>>> another_tuple = tuple()
>>> abc = tuple([1, 2, 3])
```
O código acima demonstra uma maneira de criar uma tupla com cinco elementos. Também mostra que podemos fatiar tuplas. No entanto, não podemos classificar uma. Os dois últimos exemplos mostram como criar tuplas usando a palavra-chave tuple, o primeiro apenas cria uma tupla vazia, enquanto o segundo exemplo possui três elementos dentro dela. 

O ultimo exemplo (abc) é também um exemplo de __fundição__, no qual podemos alterar ou converter um item de um tipo de dado para outro (nesse caso de uma lista para uma tupla), e para reverter isso, basta utilizar o comando reverso `abc = lista(abc)`.

- __Dicionários__

Um dicionário é basicamente uma __tabela hash__, podem ser chamados também de memorias associativas ou matrizes associativas. Os dicionarios são indexados com __chaves__ que podem ser de qualquer tipo imutável (uma string, um número, etc). Podemos obter uma lista de chaves utilizando o método __keys__. Para verificar se um dicionário tem uma chave, podemos usar a palavra-chave __in__. Um exemplo de criação de dicionário: 

```py
>>> my_dict = {}
>>> another_dict = dict()
>>> my_other_dict = {"one":1, "two":2, "three":3}
>>> my_other_dict
{'three': 3, 'two': 2, 'one': 1}
```
Os dois primeiros exemplos mostram como criar um dicionário vazio, já o último contém elementos (chaves e suas correspondentes) dentro. Para acessar um valor em um dicionário basta usar `my_other_dict ["chave"]`. Para verificar se existe uma chave no dicionário, utilizamos o "in" comentado anteriormente dessa forma: `"chave" in my_other_dict`. Para acessar uma lista de todas as chaves presentes em um dicionário usamos `my_other_dict.keys()`.

Embora isso provavelmente não importe muito agora, em uma situação real de trabalho, os segundos importam. Quando temos milhares de arquivos para processar, esses pequenos truques podem economizar muito tempo a longo prazo.


### 4) Capítulo 4: Declarações condicionais

- __Instrução IF__

 A instrução if no python é simples,porém, devemos tomar cuidado com os __espaços__ e executar o if primeiro e depois a mensagem. Usando como exemplo as variáveis temos: 

```py
if var1 > var2 :
    print("Verdadeiro")
else :
    print("Falso")
```
- __Operações Booleanas__

 Analoga a outras linguagens de programação, as operações booleanas utilizam das operações __or__, __and__ e __not__, vejamos um exemplo de utilização:

```py
x  =  10 
y  =  10 
if  x  ==  10  and  y  ==  15 : 
    print ( "Esta afirmação era verdadeira" ) 
else : 
    print ( "A afirmação era falsa!" )
```
Podemos também usar os operadores booleanos para verificar elementos de listas:

```py
my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
    print("'x' não foi adicionado a lista")
```

- __Verificando se não há nada__

 Em python uma string, tupla ou lista vazia também é avaliada como __False__, assim como a __None__. O valor None é usado para representar a ausência do valor. Vejamos um exemplo:

```py
empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")
```
As primeiras quatro linhas configuram quatro variáveis. A seguir, temos quatro condicionais para testá-las. O primeiro verifica se a lista_vazia está realmente vazia. A segunda condicional verifica se o empty_tuple contém algo. As duas últimas condicionais estão fazendo o oposto da segunda, a terceira verifica se a string está vazia e a quarta verifica se a variável nothing é realmente nula.

O operador not significa que estamos verificando o significado oposto. Em outras palavras, estamos verificando se o valor NÃO é Verdadeiro.

- __Caracteres especiais__

Em python temos também caracteres especiais como __\n__ que pula linhas em um print e também __\t__ que da um "tab" em um print.


### 5) Capítulo 5 - Loops

- __Loop For__

Usamos o loop em Python todas vez que desejamos iterar algo repetidas vezes, e essas repetições são dadas por "n" vezes. Usaremos a função __range__ para entendermos como funciona, neste formato: `range(n)`. Esta função pega um número inteiro (n) e retorna um "range object". A função range também aceita um valor __inicial__, __final__ e um valor de __etapa__, nesta ordem. Aqui vai um exemplo:

```py
>>> range(5,10)
range(5, 10)
>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
```
Entendendo a função range, podemos finalmente criar um laço de repetição usando o __for__ em qualquer __programa__ usando python, aqui vai um exemplo:

```py
for number in range(5):
print(number)
```
Saída do código acima:
```py
0
1
2
3
4
```
Podemos perceber que `range(5)`=`[0, 1, 2, 3, 4]`. Podemos também usar um loop for com um dicionário, no qual ele percorre sobre as chaves dentro daquele dicionário:
```py
a_dict = {"one":1, "two":2, "three":3}
for key in a_dict:
    print(key)
```
Saída do código acima:
```py
three
two
one
```
Agora, sabemos que as chaves podem ser classificadas, podemos fazer isso também antes de iterá-las. Podemos ver como funciona no código abaixo:
```py
>>> a_dict = {1:"one", 2:"two", 3:"three"}
>>> keys = a_dict.keys()
>>> keys = sorted(keys)
>>> for key in keys:
       print(key)
```
Saída do código acima:
```py
1
2
3
```
Primeiro, criamos um dicionário que possui números inteiros para chaves. Em seguida, extraímos as chaves do dicionário (sempre que usarmos __keys()__, isso retornará uma lista não ordenada de chaves). Com isso, temos uma visão das chaves do dicionário, classificamos e então usamos o loop para percorrê-las.

Para avançarmos um pouco mais no conceito de loops, usaremos agora um algoritmo que implementa um loop que imprime apenas números pares. Para isso, também implementaremos uma condicional:
```py
>>> for number in range(10):
        if number % 2 == 0:
            print(number)
```
Saída do código acima:
```py
0
2
4
6
8
```
Utilizando o operador de módulo __%__ juntamente com a estrutura de condição, pudemos identificar todos os números pares presentes dentro do range (10), caso quisermos aumentar a quantidade de números pares, basta aumentar o range.

- __Loop While__

O loop while no Python é semelhante ao da linguagem C, repetindo o que estiver no loop 'n' vezes, dependendo de uma condição estabelecida:

```py
>>> i = 0
>>> while i < 10:
        print(i)
        i = i + 1
```
Existe uma forma de sair de um loop sem que a condição seja completada, que é usando o comando `break`. No exemplo abaixo, conseguimos ver isso na prática analisando o código e sua saída:
```py
>>> while i < 10:
        print(i)
        if i == 5:
            break
        i += 1
```
Saída do código acima:
```py
0
1
2
3
4
5
```
O atalho `+=` é muito útil nesses tipos de programas, e também podemos usar com qualquer outro operador matemático além da adição.

O break embutido é conhecido como uma ferramenta de controle de fluxo. Existe outro chamado `continue` que é usado basicamente para __pular uma iteração__ ou continuar com a próxima iteração. Esta é uma maneira de usá-lo:
```py
i = 0

while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break
    i += 1
```
- __Else em Loops__

A instrução else em loops só será executada se o loop for __concluído com sucesso__. O principal uso da instrução else é para __pesquisar itens__, como no código a seguir:
```py
my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")
```


### 6) Capítulo 6: Compreensões do Python

A linguagem Python possui alguns métodos para criar listas e dicionários conhecidos como compreensões. Existe também um terceiro tipo de compreensão para a criação de um conjunto Python. Neste capítulo aprenderemos como usar cada tipo de compreensão. 

- __Compreensões de lista__

A compreensão de lista é basicamente um loop for que produz uma estrutura de __lista__. Podemos visualizar isso melhor com um exemplo simples: `>>> x = [i for i in range(5)]`. Com isso se dermos um `print(x)` isso nos resultará uma lista contendo os inteiros de 0 até 4, isso pode ser útil quando queremos criar uma lista muito rapidamente. Seguimos para outro exemplo onde precisamos analisar um arquivo e procurar algo em particular, podemos usar uma comprrensão de lista como uma espécie de filtro.

Uma outra utilização importante das compreensões de lista é a capacidade de __converter elementos mutaveis__:
```py
>>> x = ['1', '2', '3', '4', '5']
>>> y = [int(i) for i in x]
>>> y
```
Saída do código acima:
```py
[1, 2, 3, 4, 5]
```

Também há ocasiões em que é necessário criar uma compreensão de lista aninhada. Uma razão para fazer isso é nivelar várias listas em uma. Este exemplo vem da documentação do Python:
```py
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
```
Saída do código acima:
```py
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- __Compreensões de dicionário__

São muito semelhantes a uma compreensão de lista na forma como são organizados, vejamos o exemplo a seguir:
```py
>>> print( {i: str(i) for i in range(5)} )
```
Saída do código acima:
```py
{0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}
```
Esse código cria um dicionário onde a chave __i__ é mapeada para o valor __str(i)__ para cada valor i em __range(5)__, range(5) gera uma sequência de números de 0 a 4. Em Python, __str(i)__ é uma função que __converte o valor de i__ para uma __string__. Em outras palavras, str(i) transforma um número inteiro i em uma representação de string desse número, por exemplo, __se i for 5__ então __str(i) será '5'__.

Agora podemos nos perguntar como poderíamos usar a compreensão de um dicionário na vida real. Uma das respostas é a possibilidade de efetuar __trocas__ de chaves e valores do dicionário. Vejamos como isso funciona:
```py
>>> my_dict = {1:"dog", 2:"cat", 3:"hamster"}
>>> print( {value:key for key, value in my_dict.items()} )
```
Saída do código acima:
```py
{'hamster': 3, 'dog': 1, 'cat': 2}
```
Isso só funcionará se os valores do dicionário forem de um tipo não mutável, como uma string. Caso contrário, você acabará fazendo com que uma exceção seja levantada.
- __Compreensões de Set__

As compreensões de "set" são criadas da mesma maneira que as de um dicionário. Vamos ver um exemplo usando __set__:
```py
>>> my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
>>> my_set = set(my_list)
>>> my_set
```
Saída do código acima:
```py
set{1, 2, 3, 4, 5, 7, 8}
```


### 7) Capítulo 7 - Tratamento de Exceções

O tratamento de exceções é um recurso muito importante e utilizado em Python e outras linguagens para evitar que programas travem, ou executem de forma equivocada por conta de erros. Existem vários casos de exceções, algum deles são: __IOError__, __IndexError__, __SyntaxError__ entre outros.

- __Lidando com exceções__

Para lidar com exceções em Python não é muito complicado, ao longo deste resumo veremos alguns exemplos que causarão exceções, começaremos por um famoso, a __divisão por 0__:
```py
>>> 1 / 0
Traceback (most recent call last):
    File "<string>", line 1, in <fragment>
ZeroDivisionError: integer division or modulo by zero
```
Para tratarmos isso, podemos usar diferentes métodos, um deles é utilizando o __except__ desta forma:
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida.")
```
Agora toda vez que tivermos uma divisão por 0, a mensagem escrita no __print__ será exibida. Utilizamos isso também em casos mais complexos já vistos anteriormente, como em um dicionário:
```python
my_dict = {"a":1, "b":2, "c":3}
try:
        value = my_dict["d"]
    except KeyError:
        print("That key does not exist!")
```
Também podemos criar várias exceções com uma única instrução, e da mesma forma há varias maneiras de isso ser realizado. Veremos algumas delas agora:
```python
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")
```
A utilização do comando `except:` sem nada após os dois pontos, nos leva a uma mensagem geral para qualquer outro erro que possa ocorrer.

Aqui está outra maneira de capturar múltiplas exceções:
```python
try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")
```
-  __Utilizando a declaração final__

A declaração final é fácil de usar. Vamos dar uma olhada em um exemplo simples:
```py
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")
```
Se executarmos o código acima, ele irá imprimir a instrução __except__ e a __finally__ simultaneamente, essa instrução é muito utilizada para alguma mensagem que queremos passar antes da finalização do programa.

- __Try, except, or else__

A instrução __try/except__ também possui uma cláusula __else__. O else só será executado se não houver erros gerados. Passaremos alguns momentos examinando alguns exemplos:
```py
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
```
E juntando tudo que aprendemos, podemos criar um tratamento completo, como por exemplo: 
```py
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!")
```


### 8) Capítulo 8 - Trabalhando com Arquivos

- __Como ler um arquivo__

Python tem uma função interna chamada __open__ que podemos usar para abrir um determinado arquivo para leitura. Vamos criar um arquivo de texto chamado "teste.txt", e realizar os seguintes comandos para a realização da abertura no Linux:
```py
handle = open("Teste.txt")
handle = open("/home/nicolas.fs/Downloads/Teste.txt", "r")
```

No primeiro exemplo, o Python procurará automaticamente teste.txt na pasta em que o script está sendo executado (GitHub), se não encontrar, você receberá um IOError, não é uma maneira qualificada.

No segundo exemplo temos um exemplo melhor, onde é especificado claramente onde está o arquivo. Podemos reparar também que está escrito __"r"__ ao final da linha, isso significa que o arquivo abrirá para __somente leitura__, existem várias outras funções de abertura como escrita (__"w"__), leitura e escrita (__"a"__) e etc.

No windows, temos que tomar cuidado com a __barra inversa__, logo devemos adicionar antes do local do arquivo a letra __r__ para não haver conflito com os caracteres especiais, desta forma: `handle = open(r"C:\Users\nicolas\dowloads\Teste.txt", "r")`

Outra coisa que podemos fazer é realizar a leitura do arquivo, guardar em uma variável de dados, imprimir os dados e fechar o identificador para economizar memória e para caso outro programa queira abri-lo.

```py
>>> handle = open("/home/nicolas.fs/Downloads/Teste.txt", "r")
>>> data = handle.read()
>>> print(data)
>>> handle.close()
```
Vejamos agora algumas diferentes maneiras de ler um arquivo: lendo uma linha de cada vez _(1)_ e lendo todas as linhas _(2)_ esse na qual as linhas são retornadas em uma __lista__.

_(1)_
```py
handle = open("/home/nicolas.fs/Downloads/Teste.txt", "r")
data = handle.readline() # read just one line
print(data)
handle.close()
```
_(2)_
```py
handle = open("/home/nicolas.fs/Downloads/Teste.txt", "r")
data = handle.readlines() # read ALL the lines!
print(data)
handle.close()
```

- __Como ler arquivos parte por parte__

A maneira mais simples de se ler um arquivo em partes é usar um loop. Primeiro veremos como ler um arquivo __linha por linha__, e depois veremos como ler um __kilobyte__ de cada vez. Usaremos um loop for no nosso primeiro exemplo:
```py
handle = open("Teste.txt", "r")

for line in handle:
    print(line)

handle.close()
```
Aqui abrimos um arquivo somente leitura e usamos um loop para iterar sobre ele, agora vamos fazer isso em pedaços:
```py
handle = open("Teste.txt", "r")

while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break
```
Neste exemplo, usamos o loop while do Python para ler um kilobyte do arquivo por vez (1.024 bytes). Agora veremos como ler outros arquivos.

- __Como ler um arquivo binário__

Para ler um arquivo binário, tudo que precisamos fazer é alterar o __tipo e modo do arquivo__: `handle = open("Teste.pdf", "rb")`. Então desta vez alteramos o modo do arquivo para __rb__, o que significa __read-binary__.

- __Escrevendo arquivos em Python__

Utilizaremos agora para realizar gravação em arquivos os modos __w__ e __wb__, mas __CUIDADO__, ao usar os modos w ou wb, se o arquivo já existir, ele será sobrescrito __sem aviso prévio__ (usaremos o arquivo guardado na máquina, pois o do GitHub é salvo como uma tupla).
```py
handle = open("/home/nicolas.fs/Downloads/Teste.txt", "w")
handle.write("This is a test!")
handle.close()
```

- __Usando o operador With__

Python tem um pequeno recurso interno chamado de __with__, no qual podemos usar para simplificar arquivos de leitura e escrita. O operador with cria o que é conhecido como __gerenciador de texto__ em Python, que fechará automaticamente o arquivo para você qundo terminar de processar.
```py
with open("/home/nicolas.fs/Downloads/Teste.txt") as file_handler:
    for line in file_handler:
        print(line)
```

- __Capturando erros__

Da mesma forma que tínhamos no capítulo anterior, podemos tratar alguns erros utilizando __with__, no exemplo que veremos a seguir, não precisamos fazer a __declaração final__ como fizemos anteriormente, pois o gerenciador de contexto irá cuidar disso.
```py
try:
    with open("/home/nicolas.fs/Downloads/Teste.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occurred!")
```


### 9) Capítulo 9 - Importando

Python vem com muitos códigos pré-prontos, esses códigos são conhecidos como módulos e pacotes. Um módulo é um único arquivo Python importável, enquanto um pacote é dois ou mais destes módulos. Sempre que salvamos um script no Python, criamos um módulo.

- __Import this__

O python possuí um comando específico para esta ação, que seria o `import this`. Se executarmos esse código, veremos o que chamamos de o "Zen do Python". Isso na verdade não faz nada, mas fornece uma maneira divertida de mostrar como importar algo. Importemos agora algo que iremos utilizar:
```py
>>>import math
>>>math.sqrt(4)
```
Aqui importamos um __módulo matemático__ e depois fizemos uma de suas funções, no caso, a função __sqrt__. Este módulo possuí várias outras funções matemáticas que conhecemos e podemos utilizar.

- __Usando from para importar__

Nem todas as vezes queremos importar todas as funções de um módulo, para isso, usamos o comando __from__ para importar apenas funções selecionadas de um módulo:
```py
>>>from math import sqrt
>>>sqrt(16)
```
Também podemos implementar múltiplas funções usando da seguinte forma: 
```py
from math import pi, sqrt, ...
```

- __Importanto tudo__

Python também fornece uma maneira de importar __todas__ as funções e valores de um módulo. Mas devemos tomar cuidado para não contaminar nosso __namespace__(lugar onde todas as variáveis residem), criando um variável com o mesmo nome de uma função, como por exemplo:
```py
from math import *
>>> sqrt = 5
>>> sqrt(16)
```
Isso irá gerar um erro do tipo `'int' object is not callable`.

Finalmente, para importar tudo, em vez de especificar uma lista de itens apenas usamos o símbolo __*__.


### 10) Capítulo 10 - Funções

Uma função é uma estrutura que __definimos__, juntamente com seus argumentos, que podem ser palavras-chave e argumentos padrão. Uma função é um bloco de código que começa com a palavra-chave __def__, aqui está um exemplo simples:
```py
>>> def funcao ():
    print("Função definida")
```

- __Uma função vazia__

Às vezes queremos definir uma função sem colocar nenhum código nelas, podemos fazer isso usando o comando __pass__, desta forma:
```py
>>> def empty_func():
    pass
```

- __Passando argumentos para uma função__

Agora aprenderemos como criar uma função que pode aceitar argumentos e como passar esses argumentos. Criaremos uma função simples para visualização:
```py
>>> def add(a, b):
        return a + b
```
Após definirmos, podemos colocar os argumentos usando `>>> add(1, 2)` resultando neste caso no número __3__.

Todas as funções retornam algo, se não especificarmos o que retornar ela irá retornar __None__. O que podemos fazer também, é chamar a função juntamente com seus argumentos:
```py
>>> total = add(b=4, a=5)
>>> print(total)
```
Saída do código acima: `9`.

- __Argumentos de palavras-chave__

As funções também podem aceitar argumentos de palavra-chave. O que significa que podemos especificar quais queremos passar. Vejamos um exemplo:
```py
>>> def keyword_function(a=1, b=2):
        return a+b

>>> keyword_function(b=4, a=5)
```
Isso faz com que __a__ e __b__ tenham valores padrão definidos (1 e 2 nesse caso).

- __*args e **kwargs__

Também podemos configurar funções para aceitar qualquer número de argumentos usando uma sintaxe especial. Para obtermos infinitos argumentos usamos __*args__ e para palavras-chave usamos __**kwargs__. Vejamos como isso funciona na prática:
```py
>>> def many(*args, **kwargs):
        print(args)
        print(kwargs)
>>> many(1, 2, 3, name="Mike", job="programmer")
```
Saída do código acima:
```py
(1, 2, 3)
{'job': 'programmer', 'name': 'Mike'}
```
A própria função imprime dois tipos de argumentos. E como podemos ver, o parâmetro __args__ se transforma em uma __tupla__ e __kwargs__ em um __dicionario__.

- __Uma nota sobre escopo e variáveis globais__

Python tem o conceito de __escopo__, o escopo nos dirá quando uma variável está disponível para uso e onde. Se definirmos as variáveis dentro de uma função, essas variáveis só poderão ser usadas dentro dessa função. Depois que a função termina eles não podem mais ser usados pois estão __fora do escopo__, com isso, precisamos definir variáveis __globais__, como por exemplo a variável __a__ que veremos no exemplo a seguir:
```py
>>>def function_a():
    global a
    a = 1
    b = 2
    return a+b

>>>def function_b():
    c = 3
    return a+c

>>>print( function_a() )
>>>print( function_b() )
```


### 11) Capítulo 11 - Classes

Tudo em Python é um objeto, o que significa que tudo em Python possuí métodos e valores. Por exemplo, se atribuírmos uma string a variável __x__, essa string irá possuir __muitos métodos__. Se usarmos a palavra chave `dir (x)`poderemos obter uma lista de todos esses métodos. Ou seja, isso significa que uma string é baseada em uma classe e __x__ é uma __instância__ dessa classe!

- __Criando uma classe__

Uma classe em Python pode ser definida desta forma:
```py
class Vehicle:
    """docstring"""

    def __init__(self):
        """Constructor"""
        pass
```
Para criar a classe utilizamos a palavra chave __class__, seguida do __nome da classe__, e com o __objeto__ que é o que a classe se baseia ou herda. As classes possuem um método especial chamado `__init__`(para inicialização). Este método é chamado sempre que você cria um objeto baseado nesta classe. Este método é chamado apenas uma vez e não deve ser chamada novamente dentro do programa. Outro termo para o init é __constructor__, mas não é muito usual. Vamos expandir um pouco nossa definição de classe:
```py
class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!
```
O código acima adicionou três atributos e dois métodos. Os três atributos são:
```
self.color = color
self.doors = doors
self.tires = tires
```
Os métodos são:
```
brake
drive
```
Os atributos __descrevem o veículo__. Então o veículo tem uma cor, um certo número de portas e um certo número de pneus. Também possui dois métodos. Um método __descreve o que uma classe faz__. Portanto, neste caso, um veículo pode frear e dirigir.

- __O que é "self"__

As classes em Python precisam de uma maneira de se referirem a si mesmas, a palavra __self__ é uma forma de se descrever. Daremos uma olhada em um exemplo a seguir:
```py
class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)

if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())
```
Neste exemplo, passamos outro parâmetro para informar à classe qual tipo de veículo estamos criando. Em seguida, chamamos cada método para cada instância. Se você executar este código, deverá ver a seguinte saída:
```
car braking
I'm driving a blue car!
I'm driving a red truck!
truck braking
```
- __Subclasses__

Anteriormente, mesmo que não tenha sido especificado foi subclassificado __object__. Como object não é muito interessante, os exemplos anteriores não demonstram realmente o poder da subclasse. Então, vamos subclassificar nossa classe Vehicle e descobrir como tudo isso funciona:
```py
class Car(Vehicle):
    """
    A classe do Carro
    """

    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"

if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    car.brake()
    'The car class is breaking slowly!'
    car.drive()
    "I'm driving a yellow car!"
```
Neste caso nós criamos uma subclasse da nossa classe __Vehicle__. Podemos notar que `__init__`ou outro método não foi incluído. A razão disso é que quando subclassificamos Vehicle, obtemos todos os seus atributos e métodos. Assim, podemos notar que substituímos o método __brake__ e o fizermos dizer algo diferente do padrão. 

Usar os valores padrão da classe pai é conhecido como __herança__. Este é um grande tópico utilizado em __Programação Orientada a Objetos__. Este também é um exemplo simples de polimorfismo . As classes polimórficas normalmente têm as mesmas interfaces (ou seja, métodos, atributos), mas não têm conhecimento uma da outra.

## Parte 2: Aprendendo com a Biblioteca

### 12) Capítulo 12 - Introspecção

- __The Python type__

Algo interessante do Python é que ele pode nos dizer que tipo de variável possuímos e de que __tipo__ ela é, é uma pequena ferramenta muito útil que aprenderemos a usar como neste exemplo:
```py
>>> x = "test"
>>> y = 7
>>> z = None

>>> type(x)

>>> type(y)

>>> type(z)

```
Saída do código acima:
```
<class 'str'>
<class 'int'>
<class 'NoneType'>
```
Como podemos ver, o Python tem uma palavra-chave chamada __type__ que nos possibilita dizer qual o tipo de cada variável.

- __O diretório em Python__

Como já vimos em alguns casos, a palavra __dir__ é usada para informar ao programador quais atributos e métodos existem no __objeto__ passado. Como tudo em Python é um objeto, podemos passar uma string para dir e descobrir quais métodos ela possui utilizando `>>> import sys` e `dir(sys)`.

A função dir é extremamente útil para os pacotes de terceiros que baixamos (ou iremos baixar em breve) e que possuem pouca ou nenhuma documentação.

- __Python Help!__

Python vem com um prático utilitário de ajuda, basta digitar `help()` em um shell Python e você verá instruções. (Para sair do terminal de ajuda bastapressionar __Q__).

Se digitarmos __module__ veremos um atraso enquanto o Python pesquisa pastas da biblioteca para adquirir uma lista. Se foi instalado muitos módulos de terceiros, isso pode demorar um pouco.


### 13) O Módulo CSV

O módulo csv oferece ao programador a capacidade de __analisar arquivos CSV__. Um arquivo CSV (comma-separated value) é um arquivo de __texto legível__, onde cada linha possuí vários campos, __separados por vírgulas__ ou algum outro delimitador.

O formato CSV não possuí padrão, mas são semelhantes o suficiente para que o módulo csv seja capaz de ler a grande maioria dos arquivos em CSV.

- __Lendo um arquivo CSV__

Existem duas maneiras de ler um arquivo CSV, podemos usar uma função __reader__ ou a classe __DictReader__. Antes de testarmos os 2 métodos precisamos obter um arquivo CSV, usaremos o site da OMS para baixar algumas informações.
```py
import csv

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

if __name__ == "__main__":
    csv_path = "CSV.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
```
Primeiro importamos o __módulo csv__, então criamos uma função chamada __csv_reader__ que aceita um objeto de arquivo. Dentro da função, passamos o objeto __file__ para a função. O objeto leitor permite a iteração, assim como um objeto de arquivo normal, isso nos permite iterar cada linha no objeto leitor e imprimir a linha de dados (menos víergulas).

Agora criaremos nosso próprio arquivo CSV e iremos inseri-lo na classe __DictReader__. Iremos salvar este arquivo com o nome de __data.csv__, e vamos analisar o arquivo usando a classe DictReader, vamos experimentar:

```py
import csv

def csv_dict_reader(file_obj):
    """
    Lê um arquivo CSV usando csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)
```
No exemplo acima, abrimos um arquivo e passamos o file_obj para nossa função como fizemos antes, e ela passa o file_object para nossa classe __DictReader__, e dizemos a ele que o delimitador é uma vírgula. Em seguida, percorremos o file_object e descobrimos que cada linha no file_object é um dicionário, isso torna muito fácil __imprimir peças específicas__.

- __Escrevendo um arquivo CSV__

O módulo csv também possuí dois métodos que você pode usar para gravar um arquivo CSV. Podemos usar a função __writer__ ou a classe __DicWriter__ para isso. Veremos agora um exemplo usando a função:
```py
import csv

def csv_writer(data, path):
    """
    Grava dados em um caminho de arquivo CSV
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    path = "output.csv"
    csv_writer(data, path)
```
No código acima criamos uma função __csv_writer__ que aceita dois argumentos: __dados__ e __caminho__. Os __dados__ são uma lista de listas que criamos na parte inferior do script, usamos uma versão abreviada dos dados do exemplo anterior e dividimos as strings por vírgulas, isso retorna __uma lista__, então terminamos com uma lista alinhada parecida com esta:
```
[[ 'nome' ,  'sobrenome' ,  'cidade' ], 
 [ 'Tyrese' ,  'Hirthe' ,  'Strackeport' ], 
 [ 'Jules' ,  'Dicki' ,  'Lake Nickolasville' ], 
 [ 'Dedric' ,  ' Medhurst' ,  'Stiedemannberg' ]]
 ```

Essa função abre o caminho para que passemos e criemos um _csv writer object_. Em seguida, percorremos a estrutura da lista aninhada e gravamos cada linha no disco, observe que especificamos qual deveria ser o delimitador quando criamos o _writer object_. Se quisermos que o delimitador seja algo além de uma vírgula, é aqui que devemos defini-lo.

Agora iremos aprender a como escrever um arquivo CSV usando a classe __DictWriter__. Usaremos os dados da versão anterior e transformá-los em uma lista de dicionários. Vamos dar uma olhada em como isso funciona:
```py
import csv

def csv_dict_writer(path, fieldnames, data):
    """
    Grava um arquivo CSV usando DictWriter 
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "dict_output.csv"
    csv_dict_writer(path, fieldnames, my_list)
```
Como podemos ver, começamos com a estrutura de __lista aninhada__ que tínhamos antes, em seguida, criamos uma lista vazia e uma lista que contém os __nomes dos campos__, que é a primeira lista dentro da lista aninhada (temos que lembrar que as listas são baseadas em zero, então o primeiro elemento de uma lista começa em zero). Em seguida, fazemos um __loop__ na construção da lista aninhada começando com o segundo elemento.

Dentro do loop usamos recursos internos do Python para criar o dicionário. O método __zip__ pegará dois iteradores e os transformará em uma lista de __tuplas__, como o exemplo a seguir:
```py
zip(fieldnames, values)
[('first_name', 'Dedric'), ('last_name', 'Medhurst'), ('city', 'Stiedemannberg')]
```
Agora, quando agrupamos essa chamada em __dict__, ela transforma essa lista de tuplas em um __dicionário__, e finalmente, acrescentamos o dicionário à lista. Quando o laço __for__ termina, teremos uma estrutura de dados semelhante a essa:
```
[{'cidade': 'Strackeport', 'primeiro_nome': 'Tyrese', 'sobrenome': 'Hirthe'},
{'cidade': 'Lake Nickolasville', 'primeiro_nome': 'Jules', 'sobrenome': 'Dicki'}, {'cidade': 'Stiedemannberg', 'primeiro_nome': 'Dedric', 'sobrenome': 'Medhurst '}]
```
No final da segunda sessão, chamamos nossa função __csv_dict_writer__ e passamos todos os argumentos necessários. Dentro da função, criamos uma instância DictWriter e passamos a ela um objeto de arquivo, um valor delimitador e nossa lista de nomes de campos. Em seguida, escrevemos os nomes dos campos no disco e percorremos os dados, uma linha por vez, gravando os dados no disco.

A classe DictWriter também suporta o método __writerows__, que poderíamos ter usado em vez do loop. A função csv.writer também oferece suporte a essa funcionalidade.


### 14) Capítulo 14 - Configparser

Os arquivos de configuração são usados para armazenar as configurações de aplicativos, ou até mesmo do sistema operacional. A biblioteca principal do Python incluí um módulo chamado __configparser__ que você pode usar para criar e interagir com arquivos de configuração.

- __Criando um arquivo de configuração__

Criar um arquivo de configuração com configparser é extremamente simples, vamos ver um exemplo de como isso funciona:
```py
import configparser

def createConfig(path):
    """
    Cria um arquivo de configuração
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)
```
O código acima criará um __arquivo de configuração__ com uma seção chamada __Settings__ que conterá quatro opções: __font, font_size, font_style__ e __font_info__. No Python 3 só precisamos especificar que estamos escrevendo o arquivo no modo __somente gravação__ ou seja, no modo __w__.

- __Como ler, atualizar e excluir opções__

Agora estamos prontos para aprender como ler, atualizar e deletar opções nos arquivos de configuração:
```py
import configparser
import os

def crudConfig(path):
    """
    Criar, ler, atualizar, e deletar configurações
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # lê alguns valores da configuração
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # altera um valor na configuração
    config.set("Settings", "font_size", "12")

    # exclui um valor da configuração
    config.remove_option("Settings", "font_style")

    # grava as alterações de volta no arquivo de configuração
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)
```

Primeiramente, o código acima verifica se o caminho para o arquivo de configuração __existe__; caso não, ele usa a função __createConfig__ que utilizamos anteriormente para criá-lo. Em seguida, criamos um __objeto__ chamado __ConfigParser__ e passamos o caminho do arquivo de configuração para leitura. Para ler uma opção no arquivo, chamamos o método __get__ do nosso objeto, passando a ele o __nome da seção__ e o __nome da opção__. Isso retornará o valor da opção. Se quisermos alterar o valor de alguma opção, utilizamos o método __set__, onde passamos o nome da seção, o nome da opção e o __novo valor__.

Neste código de exemplo, alteramos o valor de __font_size__ para __12__ e removemos completamente a opção __font_style__. Em seguida, gravamos as alterações de volta no disco.

Este não é um bom exemplo, pois __nunca__ devemos ter __uma função que faça tudo__ como esta. Então a dividiremos em uma série de funções:
```py
import configparser
import os

def create_config(path):
    """
    Cria um arquivo de configuração
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Retorna o objeto de configuração
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Imprimir uma configuração
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value)
    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Atualizar uma configuração
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Excluir uma configuração
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)



if __name__ == "__main__":
    path = "settings.ini"
    font = get_setting(path, 'Settings', 'font')
    font_size = get_setting(path, 'Settings', 'font_size')

    update_setting(path, "Settings", "font_size", "12")

    delete_setting(path, "Settings", "font_style")
```
Agora ao invés de termos toda logica em uma função, nós a separamos em várias funções e então demonstramos sua funcionalidade na instrução if.

- __Como usar a interpolação__

O módulo de configparser também permite __interpolação__, o que significa que podemos __usar__ algumas __opções__ para __construir outra opção__. Fazemos isso com a opção __font_info__, pois seu valor é baseado nas opções __font e font_size__. Além disso, podemos __alterar um valor interpolado__ usando um __dicionário__. Vejamos o exemplo a seguir:
```py
import configparser
import os

def interpolationDemo(path):
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get("Settings", "font_info"))

    print(config.get("Settings", "font_info",
                     vars={"font": "Arial", "font_size": "100"}))


if __name__ == "__main__":
    path = "settings.ini"
    interpolationDemo(path)
```
Saída do código:
```
You are using Courier at 12 pt
You are using Arial at 100 pt
```

### 15) Capítulo 15 - Registro (logs)

Python fornece uma biblioteca de __"log"__ em sua biblioteca padrão. Nesta seção, veremos como criar e usar logs para aplicativos e programas.

- __Criando um registrador simples__

Criar um log com o __módulo de registro__ é fácil e pode ser feito da seguinte forma:
```py
import logging

# adicione filemode="w" para substituir 
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
```
Para acessarmos o módulo de registro devemos primeiramente importá-lo. Com isso, a maneira mais fácil de criar um log é usando a função __basicConfig__ do módulo de log e passar alguns argumentos de palavras-chave. Como __nome do arquivo, modo de arquivo, formato, datafmt, nível e fluxo__. Em nosso exemplo, passamos um nome de arquivo e o nível de registro que definimos como __INFO__. Existem cinco níveis de registro (em ordem crescente): __DEBUG, INFO, WARNING, ERROR e CRITICAL__. Se preferirmos que nosso registro substitua o log, passamos o parametro __filemode="w"__. Vejamos agora o que temos quando executamos:
```
INFO:root:Informational message
ERROR:root:An error has happened!
```
Podemos observar que a mensagem de depuração não está na saída, isso ocorre porque definimos o nível como INFO, então nosso logger só registrará se for uma mensagem INFO, WARNING, ERROR ou CRITICAL (DEBUG não aparece pois vem antes na ordem). A parte "root" significa apenas que esta mensagem de registro vem do "registro principal". Se não usarmos __basicConfig__, o módulo de log será enviado para o console.

O módulo de registro também pode registrar exceções no arquivo, como por exemplo no código a seguir:
```py
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")
```
Aqui usamos o método __getLogger__ do __módulo de registro__ para retornar um objeto de registro que foi nomeado como __ex__. Isso é útil quando temos vários registradores em um aplicativo, pois permite __identificar quais mensagens vieram de cada registrador__. Este exemplo forçará o surgimento de um __RuntimeError__, __capturando o erro__ e __registrando todo o rastreamento__ no arquivo.

- __Como fazer logon de vários múdlos + formatação__

Quanto mais codificamos, mais acabamos criando um conjunto de módulos personalizados que funcionam juntos. Primeiramente vejamos uma maneira simplificada de realizar isso:
```py
import logging
import otherMod

def main():
    """
    O ponto de entrada principal do aplicativo 
    """
    logging.basicConfig(filename="mySnake.log", level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7, 8)
    logging.info("Done!")

if __name__ == "__main__":
    main()
```
Aqui __importamos__ o log e um módulo de nossa própria criação __"otherMod"__. Então criamos nosso arquivo de log (como feito anteriormente):
```py
# otherMod.py
import logging

def add(x, y):
    """"""
    logging.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y
```
Se executarmos o código principal, veremos um log com o seguinte conteúdo:
```
INFO:root:Program started
INFO:root:added 7 and 8 to get 15
INFO:root:Done!
```
O problema de fazer desta maneira é que não podemos dizer facilmente __de onde vêm as mensagens de log__. Então precisaremos de uma maneira mais complexa, porém mais __personalizável__ de fazer isso:
```py
import logging
import otherMod2

def main():
    """
    O principal ponto de entrada do aplicativo 
    """
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

# cria o manipulador do arquivo
    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # adiciona o manipulador ao logger do objeto
    logger.addHandler(fh)

    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()
```
Aqui criamos uma instância do logger chamada __"exampleApp__, definimos seu nível de registro, criamos um objeto manipulador de arquivo de registro e um objeto formatador de registro. O __manipulador de arquivo__ deve definir o objeto formatador como __seu formatador__ e, em seguida, o manipulador de arquivo deve ser __adicionado à instância do criador de logs__. E aqui está o código para __otherMod2__ atualizado:
```py
# otherMod2.py
import logging

module_logger = logging.getLogger("exampleApp.otherMod2")

def add(x, y):
    """"""
    logger = logging.getLogger("exampleApp.otherMod2.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y
```
Observamos que aqui temos dois loggers definidos. Não fazemos nada com __module_logger__ nesse caso, mas usamos o outro.

Se executarmos o script principal, obteremos isso:
```
2012-08-02 15:37:40,592 - exampleApp - INFO - Program started
2012-08-02 15:37:40,592 - exampleApp.otherMod2.add - INFO - added 7 and 8 to get 15
2012-08-02 15:37:40,592 - exampleApp - INFO - Done!
```
Podemos notar que todas as referências à __raiz__ foram __removidas__, em vez disso, usamos nosso objeto __Formatter__, que diz que devemos obter um __tempo__ legível por humanos, o __nome__ do registrador, o __nível__ de registro e depois a __mensagem__. Eles são conhecidos como atributos __LogRecord__, e para obtermos uma lista completa dos atributos podemos acessar o link: https://docs.python.org/3/library/logging.html#logrecord-attributes.


### 16) Capítulo 16 - O módulo OS

O módulo __os__ tem muitas utilizações importantes no Python, e antes de conhecermos algumas destas utilizações precisamos usar o comando `import os`.

- __os.name__

O módulo os possuí __funções__ que podem ser chamadas, e também possuí valores normais. No caso de __os.name__, será apenas um valor, e ao acessar os.name, obteremos __informações sobre a plataforma que estamos executando__. No caso, será enviado para nós algum dos seguintes valores: __'posix'__, __'nt'__, __'os2'__, __'ce'__, __'java'__, __'riscos'__. Por exemplo, se executarmos este comando no Windows 7, receberemos um __'nt'__, pois nt é como a Microsoft chama seu sistema operacional.

- __os.enviro, os.getenv() e os.putenv()__

O valor __os.environ__ é conhecido como objeto de __mapeamento__ que retorna um __dicionário das variáveis ambientais do usuário__. Estas variáveis aparecem e são definidas toda vez que usamos nosso computador, elas podem fornecer informações valiosas, como número de processadores, tipo de CPU, nome do computador, etc.

Como este comando retorna um dicionário, isso significa que podemos acessar nossas variáveis ambientais usando os métodos de chamada do dicionário. Como por exemplo, caso quisessemos identificar a pasta "temp" usariamos:
```py
>>> print(os.environ["TMP"])
'C:\\Users\\mike\\AppData\\Local\\Temp'
´´´
Também podemos usar o comando __os.getenv__ para acessar esta variável ambiental:
```py
>>> os.getenv("TMP")
'C:\\Users\\mike\\AppData\\Local\\Temp'
```
O benefício de usar a função os.gentev() em vez do dicionário é que se tentarmos acessar uma variável ambiental que não existe, a função retornará apenas __None__. Se fizessemos a mesma coisa com o dicionário receberiamos um erro.

- __os.chdir() e os.getcwd()__

A função __os.chdir__ nos permite __alterar o diretório__ no qual estamos executando nossa sessão. Se quisermos saber em qual caminho estamos atualmente, chamamos a função __os.getcwd()__. Vejamos um exemplo desta mudança:
```py
>>> os.getcwd()
'C:\\Python27'
>>> os.chdir(r"c:\Users\mike\Documents")
>>> os.getcwd()
'c:\\Users\\mike\\Documents'
```
O código acima nos mostra que nós começamos no diretório "Python" por padrão, então, chamamos os.chdir para mudar as pastas para "Documents". E por fim, usamos os.getcwd novamente para verificar se a mudança foi realizada com sucesso.

- __os.mkdir() e os.makedirs()__

Estes dois métodos tem o mesmo propósito de __criar diretórios__. O primeiro é o __os.mkdir()__, que nos permite criar uma única pasta, como uma pasta de teste para entenderemos melhor:
```py
>>> os.mkdir("test")

>>> path = r'C:\Users\mike\Documents\pytest'
>>> os.mkdir(path)
```
Explicando o código, primeiramente usamos a função __os.mkdir__ para criar uma pasta chamada __teste__ no diretório atual. O segundo exemplo atribui um caminho a uma variável __path__, e então, passamos o caminho para a função. Isso nos permite criar uma pasta em __qualquer lugar do sistema__ no qual tenhamos permissão.

A função __os.makedirs()__ criará todas as __pastas intermediárias__ em __um caminho__, caso elas ainda não existam. Basicamente, podemos criar um caminho que contenha __pastas aninhadas__. Vejamos um exemplo:
```py
>>> path = r'C:\Users\mike\Documents\pytest\2014\02\19'
>>> os.makedirs(path)
```
Caso não tenhamos as pastas indicadas, a função irá criar elas, e no fim teremos múltiplas pastas.

- __os.remove() e os.rmdir()__

As funções __os.remove()__ e __os.rmdir__ são usadas para __excluir arquivos e diretórios__ respectivamente.

- __os.rename(src,dst)__

A função os.rename() pode renomear __pastas ou diretórios__, como por exemplo `>>> os.rename("test.txt", "pytest.txt")`. Neste exemplo, dizemos para a função para renomear o arquivo __test.txt__ para __pytest.txt__. Existe também a função __os.renames__ que renomeia __recursivamente__ um diretório ou arquivo.

- __os.startfile__

O métood __os.startfile()__ nos permite __"iniciar" um arquivo com seu programa associado__. Como quando abrimos um PDF e ele abre no Adobe Reader.

Um exemplo simples disso no código a seguir, é passar um caminho qualificado para a função, que informa para abrir um arquivo chamado __labels.pdf__: `>>> os.startfile(r'C:\Users\mike\Documents\labels.pdf')`.

- __os.walk()__

O método __os.walk()__ nos dá uma maneira de __iterar__ sobre um caminho de __nível raiz__. O que significa que podemos passar um caminho para esta função, e obter acesso a todos os subdiretórios e arquivos.

- __os.path.basename__

A função __basename__ retorna apenas o __nome do arquivo de um caminho__, por exemplo:
```py
>>> os.path.basename(r'C:\Python27\Tools\pynche\ChipViewer.py')
'ChipViewer.py'
```

- __os.path.dirname__

A função __dirname__ retornará apenas a parte do __diretório do caminho__.
```py
>>> os.path.dirname(r'C:\Python27\Tools\pynche\ChipViewer.py')
'C:\\Python27\\Tools\\pynche'
```

- __os.path.exists__

A função __exists__ informará se __um caminho existe, ou não__.
```py
>>> os.path.exists(r'C:\Python27\Tools\pynche\ChipViewer.py')
True
>>> os.path.exists(r'C:\Python27\Tools\pynche\fake.py')
False
```

- __os.path.isdir - os.path.isfile__

Os métodos __isdir e isfile__ estão relacionados ao método __exists__, pois também testam a existência. Porém, __isdir__ testa se um __caminho é um diretório__, e __isfile__ verifica se um __caminho é um arquivo__.
```py
>>> os.path.isfile(r'C:\Python27\Tools\pynche\ChipViewer.py')
True
>>> os.path.isdir(r'C:\Python27\Tools\pynche\ChipViewer.py')
False
>>> os.path.isdir(r'C:\Python27\Tools\pynche')
True
>>> os.path.isfile(r'C:\Python27\Tools\pynche')
False
```
No caso, temos __pynche__ como um __diretório__ de ChipViewer.py, e __ChipViewer.py__ como um __arquivo__ de pynche.

- __os.path.join__

O método __join__ oferece a capacidade de __unir um ou mais componentes do caminho__ usando o separador apropriado. Por exemplo, no Windows o separador é a barra inversa, no Linux, o separador é a barra.
```py
>>> os.path.join(r'C:\Python27\Tools\pynche', 'ChipViewer.py')
'C:\\Python27\\Tools\\pynche\\ChipViewer.py'
```
Neste exemplo, unimos um caminho de diretório e um caminho de arquivo para obter um caminho totalmente qualificado.

- __os.path.split__

O método __split__ dividirá um caminho em uma __tupla__ que contém o __diretório e o arquivo__. Vejamos um exemplo super comum do uso do split:
```py
>>> dirname, fname = os.path.split(r'C:\Python27\Tools\pynche\ChipViewer.py')
>>> dirname
'C:\\Python27\\Tools\\pynche'
>>> fname
'ChipViewer.py'
```
Quando dividimos o caminho, ele retorna uma tupla de dois elementos. Como temos duas variáveis, o primeiro elemento é atribuído à primeira variável e o segundo à segunda variável.


### 17) Capítulo 17 - O módulo email/smtplib

O Python fornece alguns módulos que podemos usar para criar e-mails, estes são os módulos __email e smtplib__.

- __Como enviar um e-mail com smtplib__

Vamos escrever um exemplo rápido que mostra como enviar um e-mail. Para isso, salvaremos o seguinte código em um arquivo no diretório:
```py
import smtplib

HOST = "mySMTP.server.com"
SUBJECT = "Test email from Python"
TO = "mike@someAddress.org"
FROM = "python@mydomain.com"
text = "Python 3.4 rules them all!"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
    ))

server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()
```
Neste código importamos dois módulos, __smtplib__ e o módulo __string__. Dois terços deste código são usados para configurar o email. Primeiramente vamos nos concentrar na variável ímpar chamada __BODY__. Aqui usamos o módulo __string__ para __combinar__ todas as __variáveis__ anteriores em uma __única string__ onde cada linha termina com /r mais uma nova linha com /n. Se imprimirmos `>>>print(BODY)`, ficaria assim: `'From: python@mydomain.com\r\nTo: mike@mydomain.com\r\nSubject: Test email from Python\r\n\r\nblah blah blah'`.

Após isso, configuramos uma conexão de servidor com o host e então chamamos o método __sendmail__ do outro módulo para enviar o e-mail, depois, nos desconectamos do servidor. Podemos notar que este código não contém um __usuário ou senha__, caso o servidor exigir autenticação, precisamo adicionar a seguinte linha ao código: `server.login(username, password)`

Isso deve ser __adicionado logo após a criação do objeto servidor__. Vejamos agora este código implementado em uma função:
```py
import smtplib

def send_email(host, subject, to_addr, from_addr, body_text):
    """
    Envia um e-mail
    """
    BODY = "\r\n".join((
            "From: %s" % from_addr,
            "To: %s" % to_addr,
            "Subject: %s" % subject ,
            "",
            body_text
            ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()

if __name__ == "__main__":
    host = "mySMTP.server.com"
    subject = "Test email from Python"
    to_addr = "mike@someAddress.org"
    from_addr = "python@mydomain.com"
    body_text = "Python rules them all!"
    send_email(host, subject, to_addr, from_addr, body_text)
```
Agora adicionaremos um __arquivo de configuração__ para armazenar as __informações do servidor__ e o __endereço de origem__, para que facilite quando formos mudar algo no arquivo sem ter que mudar o código. Vamos dar uma olhada neste arquivo de configuração:
```
[smtp]
server = some.server.com
from_addr = python@mydomain.com
```
Esse é um arquivo de configuração bem simples. Nele temos uma seção chamada __smtp__ na qual temos dois itens: __server__ e __from_addr__. Usaremos __configObj__ para ler este arquivo e transformá-lo em um dicionário Python. Salvaremos então, esta versão atualizada do código (smtp_config.py):
```py
import os
import smtplib
import sys

from configparser import ConfigParser

def send_email(subject, to_addr, body_text):
    """
    Envia o e-mail
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject ,
        "",
        body_text
    ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()

if __name__ == "__main__":
    subject = "Test email from Python"
    to_addr = "mike@someAddress.org"
    body_text = "Python rules them all!"
    send_email(subject, to_addr, body_text)
```
Primeiro, queremos pegar o caminho em que o script está, que é o que __base_path__ representa. Em seguida, combinamos este caminho com o nome do arquivo para obter um caminho qualificado para o arquivo de config. Logo após, verificamos a existência desse arquivo, se estiver lá, criamos um __ConfigParser__, e se não estiver, imprimimos uma mensagem e saímos do script. Devemos adicionar um __manipulador de exceção__ em torno da chamada __ConfigParser.read()__ apenas para garantir a segurança, pois o arquivo pode existir mas estar corrompido ou podemos não ter permissão para abri-lo, e isso gerará uma exceção. Caso ConfigParser seja criado com sucesso, podemos extrair __informações de host e from_addr__ usando a sintaxe usual.

- __Enviando vários e-mails de uma vez__

Para enviar vários e-mails, teremos que modificar um pouco o código, como a seguir:
```py
import os
import smtplib
import sys

from configparser import ConfigParser

def send_email(subject, body_text, emails):
    """
    Envia um e-mail
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    BODY = "\r\n".join((
            "From: %s" % from_addr,
            "To: %s" % ', '.join(emails),
            "Subject: %s" % subject ,
            "",
            body_text
            ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, BODY)
    server.quit()

if __name__ == "__main__":
    emails = ["mike@someAddress.org", "someone@gmail.com"]
    subject = "Test email from Python"
    body_text = "Python rules them all!"
    send_email(subject, body_text, emails)
```
Neste exemplo removemos o parâmetro __to_addr__ e adicionamos um parâmetro __emails__, que será uma __lista de endereços de e-mail__. Para fazer isso, precisamos criar uma string separada por vírgula na parte __To:__ do BODY, e também passar a lista de e-mails para o método __sendmail__. Assim, usamos a seguinte syntaxe para criar a string separada por vírgula: `join(emails)`.

- __Enviar e-mails usando as linhas TO,CC e BCC__

Iremos ver agora como enviar usando os campos CC e BCC. Primeiramente teremos que novamente atualizar o código:
```py
import os
import smtplib
import sys

from configparser import ConfigParser

def send_email(subject, body_text, to_emails, cc_emails, bcc_emails):
    """
    Send an email
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    BODY = "\r\n".join((
            "From: %s" % from_addr,
            "To: %s" % ', '.join(to_emails),
            "CC: %s" % ', '.join(cc_emails),
            "BCC: %s" % ', '.join(bcc_emails),
            "Subject: %s" % subject ,
            "",
            body_text
            ))
    emails = to_emails + cc_emails + bcc_emails

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, BODY)
    server.quit()

if __name__ == "__main__":
    emails = ["mike@somewhere.org"]
    cc_emails = ["someone@gmail.com"]
    bcc_emails = ["schmuck@newtel.net"]

    subject = "Test email from Python"
    body_text = "Python rules them all!"
    send_email(subject, body_text, emails, cc_emails, bcc_emails)
```
Neste código passamos 3 listas, cada uma com um endereço de e-mail. Criamos os campos CC e BCC exatamente como antes, mas também combinamos as __3 listas em uma__ para que possamos passar ela para o método __sendmail()__.

- __Adicione um anexo/corpo usando o módulo de e-mail__

Agora pegaremos tudo que aprendemos até agora e combinar com o __módulo de e-mail__ do Python para que possamos enviar anexos. O módulo de e-mail torna a adição desses anexos extremamente fácil. Vejamos o código:
```py
import os
import smtplib
import sys

from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

#----------------------------------------------------------------------
def send_email_with_attachment(subject, body_text, to_emails,
                               cc_emails, bcc_emails, file_to_attach):
    """
    Envie um e-mail com anexo
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    header = 'Content-Disposition', 'attachment; filename="%s"' % file_to_attach

    # get the config
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    # extract server and from_addr from config
    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if body_text:
        msg.attach( MIMEText(body_text) )

    msg["To"] = ', '.join(to_emails)
    msg["cc"] = ', '.join(cc_emails)

    attachment = MIMEBase('application', "octet-stream")
    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
        attachment.set_payload( data )
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print(msg)
        sys.exit(1)

    emails = to_emails + cc_emails

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, msg.as_string())
    server.quit()

if __name__ == "__main__":
    emails = ["mike@someAddress.org", "nedry@jp.net"]
    cc_emails = ["someone@gmail.com"]
    bcc_emails = ["anonymous@circe.org"]

    subject = "Test email with attachment from Python"
    body_text = "This email contains an attachment!"
    path = "/path/to/some/file"
    send_email_with_attachment(subject, body_text, emails,
                               cc_emails, bcc_emails, path)
```
Para este último exemplo renomeamos nossa função e adicionamos um novo argumento: __file_to_attach__. Também precisamos adicionar um cabeçalho e criar um objeto: __MIMEMultipart__, e adicionamos elementos a este objeto, como faríamos com as chaves de um dicionário. Podemos notar que precisamos usar o método __formdate__ deste módulo para __inserir a data formatada__ corretamente. Para adicionar o corpo da mensagem, precisamos criar uma instância de __MIMEText__. Em seguida, adicionamos o anexo, que foi envolvido em um manipulador de exceções e usamos a instrução __with__ para extrair o arquivo e colocá-lo em nosso objeto. Finalmente, adicionamos a variável __msg__ e enviamos. Devemos notar também que neste caso convertemos a __mensagem__ em uma __string__ no método sendmail.


### 18) Capítulo 18 - O Módulo sqlite

__SQLite__ é um mecanismo de banco de dados SQL transacional independente, sem servidor e configuração. Se quisermos inspecionar seu banco de dados visualmente, podemos usar o plugin __SQLite Manager__ para Firefox, ou usar o shell de linha de comando do SQLite.

- __Como criar um banco de dados e inserir dados__

Criar um banco de dados em SQLite é muito fácil, mas o processo requer que conheçamos um pouco de SQL para fazê-lo. Aqui está um código que criará um banco de dados para armazenar álbuns de músicas:
```py
import sqlite3

conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE albums
                  (title text, artist text, release_date text,
                   publisher text, media_type text)
               """)
```
Primeiro __importamos o módulo sqlite3__ e criamos uma conexão com o banco de dados. Podemos também passar um caminho ou nome de arquivo, ou apenas usar a string especial __":memory:"__ para criar o banco de dados na memória. No nosso caso, criamos um disco em um arquivo chamado __mydatabase.db__. A seguir criamos um __objeto cursor__ que permite __interagir com o banco de dados__ e __adicionar registros__, entre outras coisas. Usamos também a sintaxe SQL para criar uma __tabela__ chamada álbuns com 5 campos de texto. O SQLite suporta apenas cinco tipos de dados: __nulo, inteiro, real, texto e blob__. Agora desenvolveremos um código para inserir alguns dados em nossa nova tabela.
```py
import sqlite3

conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

# insere dados
cursor.execute("""INSERT INTO albums
                  VALUES ('Glow', 'Andy Hunter', '7/24/2012',
                          'Xplore Records', 'MP3')"""
               )

# salva no banco de dados
conn.commit()

# insere vários registros usando um método mais seguro
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
```
Aqui usamos o comando __INSERT INTO SQL__ para __inserir um registro__ em nosso banco de dados. E, logo a seguir, o código nos mostra como adicionar vários registros de uma vez usando o método executemany do cursor. Podemos observar que estamos usando _?_ ao invés de substituição de strings _%s_ para inserir os valores. Isso ocorre porque usar a substituição de string __não é seguro__ e não deve ser usado, pois pode permitir a ocorrência de ataques de injeção de SQL.

- __Atualizando e excluindo Registros__

Para aprendermos como atualizar e excluir registros, iremos primeiramente fazer uma atualização.
```py
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
UPDATE albums
SET artist = 'Nicolas'
WHERE artist = 'John Doe'
"""
cursor.execute(sql)
conn.commit()
```
Aqui usamos o comando __UPDATE__ do SQL para indicar qual tabela queremos atualizar, usamos __SET + O campo que queremos alterar__ e atribuímos qual a nova mudança que aparecerá, e por fim, utilizamos __WHERE + O campo que queremos alterar__ atribuído ao que está escrito e será mudado.

Para __deletar__ elementos também é muito fácil:
```py
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
DELETE FROM albums
WHERE artist = 'John Doe'
"""
cursor.execute(sql)
conn.commit()
```
Aqui usamos o comando __DELETE FROM__ para indicar de qual tabela vamos deletar algo, e o __WHERE__ já visto anteriormente.

- __Consultas SQLite básicas__

As consultas no SQLite são praticamente as mesmas que usamos em outros bancos de dados. Aqui estão alguns exempĺos:
```py
conn = sqlite3.connect("mydatabase.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()

sql = "SELECT * FROM albums WHERE artist=?" #Consulta
cursor.execute(sql, [("Trip Lee")]) #Nome para busca
print(cursor.fetchall()) 

print("\nHere's a listing of all the records in the table:\n") #Listagem
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"): 
    print(row)

print("\nResults from a LIKE query:\n") 
sql = """
SELECT * FROM albums
WHERE title LIKE 'The%'""" #Faz a consulta para um caractere específico usando caractere% no qual todos elementos que tiverem este começo serão listados
#Para o final, basta usar %caractere
#Para ambos os lados, basta usar %caractere%
cursor.execute(sql)
print(cursor.fetchall())
```
Neste exemplo, temos 3 tipos de busca. O primeiro, selecionamos __diretamente__ a informação que queremos buscar. No segundo, o algoritmo executa uma __listagem__ de todos elementos presentes no banco (rowid), ordenando os resultados pelo nome do artista em ordem crescente utilizando o comando __ORDER BY__. E por fim, no terceiro fazemos __buscas por caractéres específicos__.
