# Estudos-python


 Link para ínicio dos estudos: [python 101](https://python101.pythonlibrary.org/)

Guia: Criar um resumo para cada capitulo e testar os comandos do tutorial diretamente no terminal do vscode (comando `python3` para iniciar). -> Para acessar usamos CTRL+SHIFT+P e buscamos Create New Terminal

### 1) Capitulo 1: Programação IDLE 
- Usando IDLE: Python por ser uma linguagem interpretativa utiliza de elementos próprios e não utiliza outros como compiladores. No caso, um que é utilizado é o chamado **IDLE** que funciona como um editor de código, destacando, depurando e até mesmo preenchendo automaticamente algumas areas do código

- Sobre comentários: Comentários são de extrema importância para caso alguém queira fazer algum comentario em alguma linha de código, tanto para relembrar algo ou para fazer alguma observação.


### 2) Capitulo 2: Tudo sobre strings

- Como criar uma string: De inicio podemos fazer strings usando aspas duplas simples e triplas, sendo que as aspas triplas (''') nos proporcionam a opção de continuar a string em outra linha do comando. Outra forma também, é utilizando o comando str (informação) no qual podemos guardar as informações ja registradas em outro lugar em uma string, esse método é conhecido como **fundição** *(1)*. Strings são imutáveis, ou seja, mesmo se atribuirmos uma definição diferente mas para um mesmo nome de string sua **identidade** muda, não sendo mais o mesmo ID daquela string anterior na qual definimos *(2)*.

_(1)_
```
>>> meu_número  =  123 
>>> minha_string  =  str ( meu_número )
```
_(2)_
```
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
- Concatenar (ou somar) strings: Em python para somar strings, ou seja, ajuntar uma na outra, apenas é necessário definir cada uma que queiramos somar, e uma que utilizaremos para guardar, e depois utilizar o operador **soma (+)**.

```
>>> string_one  =  "Meu cachorro comeu" 
>>> string_two  =  " meu dever de casa!" 
>>> string_três  =  string_um  +  string_dois
```
- Métodos string: Por uma string ser um objeto me python, podemos modificar uma string utilizando comandos simples como **upper() lower() strip()** e etc. Estes comandos modificam nossa string e o conteúdo dela, e para saber todos os comandos possíveis utilizamos um comando específico _(3)_. Os métodos que começam e terminam com "__" não são muito utilizados, mas caso queiramos saber para o que cada um serve 
basta utilizar outro comando _(4)_.

_(3)_
```
 >>> dir(my_string)
 ```
_(4)_
 ```
 >>> help(my_string.capitalize)
```
- Fatiamento de strings: Fatiamento de string é um método utilizado para mostrar apenas algumas **partes específicas** da string na qual queremos **visualizar**, em visualização fica mais fácil de entender como demonstrado no bloco de código _(5)_. No caso, podemos fatiar especificando o ínicio, o final, ou ambos. Isso vai depender do que queremos que saia no final. Também podemos acessar caracteres individuais de uma string utilizando `printf(minha_string[n])`, sendo n o número do caractere.

_(5)_
```
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
- Formatação de string: Também conhecida como substiuição, a formatação serve para substituir os valores de uma string base. Na maioria das vezes, você inserirá strings dentro de strings, no entanto, você também inserirá números inteiros e flutuantes em strings com bastante frequência. Aqui temos um exemplo usual de como isso ocorre na prática _(6)_, aqui basicamente mudamos nosso %s para %(lang)s, que é basicamente o %s com uma variável dentro dele. Outro exemplo de substituição é utilizando **format**, no qual aparenta ser mais completo como a seguir _(7)_. Este último exemplo usa um dicionário como usamos no modelo anterior (que são as definições de x e y). No entanto, temos que extrair o dicionário usando o asterisco duplo para que funcione corretamente aqui.

_(6)_
```
>>> print ( " %(lang)s é divertido!"  %  { "lang" : "Python" })
'Python é divertido!'
```

_(7)_
```
>>> "Python é tão simples quanto {0}, {1}, {2}" . format ( "a" ,  "b" ,  "c" ) 
'Python é tão simples quanto a, b, c' 
>>> "Python é tão simples quanto {1}, {0}, {2}" . format ( "a" ,  "b" ,  "c" ) 
'Python é tão simples quanto b, a, c' 
>>> xy  =  { "x" : 0 ,  "y" : 10 } 
>>> print ( " Faça um gráfico de um ponto onde x={x} e y={y}" . format ( ** xy )) 
Faça um gráfico de um ponto onde x=0 e y=10
```

Há muitas outras coisas que você pode fazer com strings, como especificar uma largura, alinhar o texto, converter para bases diferentes e muito mais. Certifique-se de dar uma olhada em algumas das referências no fim do capítulo desta aula.





