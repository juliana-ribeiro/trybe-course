## Exercício 1 - Criando uma imagem a partir de outra no Docker (chuanwen/cowsay)

* O objetivo desse exercício é de utilizar uma imagem disponível no DockerHub, chamada **cowsay**, e criar a partir dela instruções no Dockerfile para construir (build) uma nova imagem. A imagem, que contém o programa de mesmo nome, funciona gerando no terminal uma *ASCII Art* de uma vaca e uma mensagem. Como o exemplo abaixo:

  <img src="https://i.imgur.com/Jo5FYTP.png" alt="Cowsay exemplo"/>

* Espera-se que a nova imagem tenha uma mensagem padrão, ao invés de ser gerada aleatoriamente, e que esta também possa ser substituída. Isso é possível explorando a característica da instrução CMD ser sobrescrita sempre que fornecida uma nova, mesmo via linha de comando (CLI), já que é executada sempre a última. Dessa forma, a mensagem padrão pode facilmente ser substituída passando um argumento através do `docker run`.


### Resolução:

   1 - Criando o Dockerfile usando a imagem **chuanwen/cowsay**:

`FROM chuanwen/cowsay:latest`

   2 - Definindo um executável para iniciar o programa:

 `ENTRYPOINT ["/usr/games/cowsay"]`

   3 - Definindo uma mensagem padrão a ser exibida sempre que não for passado nenhum argumento ao iniciar o contêiner:

`CMD ["Be Vegan! <3"]`

   4 -  Gerando uma **build** a partir do Dockerfile e criando uma nova imagem com o nome **cowsay**, considerando que estamos na mesma pasta do arquivo de instrução:

`docker image build ./ -t cowsay`

   5 - Rodando um novo contêiner a partir da imagem criada, sem passar argumento:

`docker container run cowsay`

  <img src="https://imgur.com/sBLvWyZ.png" alt="Novo container a partir da imagem criada e mensagem padrão"/>

   6 - Rodando um novo contêiner a partir da imagem criada, passando uma nova mensagem como argumento:

`docker container run cowsay Muuuuh`

<img src="https://imgur.com/FbqcjHa.png" alt="Novo container a partir da imagem criada e mensagem personalizada"/>

   Bônus 1: Obtendo a lista de outros animais que podem ser gerados no lugar da vaca:

`docker container run cowsay -l`

   Bônus 2:  Rodando um novo contêiner a partir da imagem criada para mostrar um leão e uma nova mensagem:

`docker container run cowsay -f moofasa "Rawr, I'm a lion"`

<img src="https://imgur.com/AAtQhor.png" alt="Novo container gerando a arte de um leão"/>

