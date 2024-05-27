# Lista de comandos LINUX

## Comando PWD

O comando serve pwd para __encontrar o caminho para o diretório atual__ (da pasta) em que você está. O comando vai retornar um caminho completo (cheio), que é basicamente um caminho que começa com uma barra inclinada (/). Um exemplo de um caminho completo é /home/username.

### Comandos

- __pwd__ : Mostra o caminho do diretório atual.

- __pwd [-l]__ : Imprime o conteúdo da variável de ambiente.

- __pwd [-p]__ : Imprime o caminho real do diretório atual.

## Comando cd

O comando cd serve para __navegar entre arquivos e diretórios__ no LINUX. Vamos dizer que você esteja em /home/username/Documents e quer ir para Photos, um subdiretório de Documents. Para fazer isso, simplesmente digite cd Photos.

### Comandos

- __cd ..__ : Para subir um diretório acima do que você está.

- __cd ~[username]__ : Para acessar o diretório inicial de outro usuário.

- __cd-__ : Para mover para diretórios anteriores.

## Comando ls

O comando ls é usado para __visualizar conteúdos em um diretório__. Por padrão, ele irá mostrar os conteúdos do diretório atual que estivermos, mas podemos utilizar um comando complementare para verificar outros diretórios.

### Comandos

- __ls -r__ : Lista todos os arquivos nos subdiretórios.

- __ls -a__ : Mostra todos os arquivos ocultos.

- __ls -lh__ : Lista todos os tamanhos de arquivos em formatos fáceis, como MB, GB ou TB.

- __ls caminho__ : Para mudar o diretório que queremos visualizar, utilizamos o comando ls juntamente com o caminho para este diretório.

## Comando cat

O cat é utilizado para __visualizar, criar e relacionar arquivos__.

### Comandos

- __cat > nomedoarquivo.txt__ : Cria um novo arquivo dentro do diretório que estamos. Se fizermos o comando para um txt, podemos dar enter e escrever seu conteúdo.

- __cat nomedoarquivo1.txt nomedoarquivo2.txt > nomedoarquivo3.txt__ : Junta os arquivos 1 e 2 em um novo (3) combinando seus conteúdos.

- __tac nomedoarquivo.txt__ : Exibe o conteúdo do arquivo em ordem reversa.

## Comando cp

Usamos o comando cp para __copiar arquivos ou diretórios__.

### Comandos

- __cp nomedoarquivo.txt / Caminho__ : Copia o arquivo para um diretório especificando seu caminho. Podemos copiar mais de um arquivo, basta colocar os outros arquivos junto com o primeiro.

- __cp nomedoarquivo1.txt nomedoarquivo2.txt__ : Copia o conteúdo de um arquivo para um outro arquivo no mesmo diretório.

- __cp -r /Caminho1 /Caminho2__ : Copia um diretório inteiro, utilizando seu caminho (1) e o caminho de destino (2).

## Comando mv

Possuí 2 usos principais que é __mover arquivos entre diretórios__ e __renomear arquivos__.

### Comandos

- __mv arquivo.txt Caminho__ : Move o arquivo indicado para o diretório indicado.

- __mv arquivo1.txt arquivo2.txt__ : Renomeia o nome do arquivo no diretório (de 1 para 2).

## Comando mkdir

O comando mkdir é utilizado para __criar um ou mais diretórios de uma vez__ e __definir permissões para cada um__.

### Comandos

- __mkdir diretório__ : Cria um novo diretório a partir do diretório atual.

- __mkdir -p diretório__ : Cria um diretório entre duas pastas existentes. Por exemplo, mkdir -p Music/2020/Songs criará o novo diretório “2020”.

- __mkdir -m diretório__ : Define as permissões do arquivo. As permissões vão depender do comando acompanhado do __-m__. 

Na notação octal, podemos utilizar números para definir as permissões. Cada dígito na notação octal representa uma combinação de permissões para o proprietário, grupo e outros, respectivamente:

4 - Permissão de leitura (r)

2 - Permissão de escrita (w)

1 - Permissão de execução (x)

Esses números podem ser somados para combinar permissões. Por exemplo:

7 (4+2+1) - Leitura, escrita e execução (rwx)

6 (4+2) - Leitura e escrita (rw-)

5 (4+1) - Leitura e execução (r-x)

4 - Apenas leitura (r--)

3 (2+1) - Escrita e execução (-wx)

2 - Apenas escrita (-w-)

1 - Apenas execução (--x)

0 - Nenhuma permissão (---)

- __mkdir -v diretório__ : Cria o diretório e confirma sua criação com uma mensagem.

## Comando rmdir

Utilizado para excluír permanentemente um diretório vazio.

### Comandos

- __rmdir -p dir/subidr__ : Excluí o subdiretório e sua pasta.

## Comando rm

O comando rm é utilizado para excluir arquivos em um diretório.

### Comandos

- __rm arquivo__ : Excluí o arquivo indicado.
- __rm arquivo1 arquivo2 arquivon___ : Excluí n arquivos indicados.

__Opções que podemos adicionar:__
- __-i__ solicita a confirmação do sistema antes de excluir um arquivo.
- __-f__ permite que o sistema faça a remoção sem confirmação.
- __-r__ exclui arquivos e diretórios recursivamente.

## Comando touch

O comando touch permite criar um arquivo vazio ou gerar e modificar um registro de data e hora.

### Comandos

- __touch  /home/username/Documents/arquivo__ : Cria um arquivo no caminho indicado.

## Comando locate

Usamos este comando para localizar um arquivo. Podemos também utilizar o argumento __-i__ para que não seja necessário diferenciar letras maiusculas e minusculas.

## Comando find

Similar ao locate, o comando find ajuda a procurar por arquivos, sendo que este comando usamos para procurar dentro de um __diretório específico__.

### Comandos

- __find -name arquivo__: Para localizar um arquivo no diretório atual.
- __find ./ -type d -name diretorio__: Para procurar diretórios.




