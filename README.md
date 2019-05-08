# Baguncinha

## Problemática

Um amigo meu me contou o seguinte problema: Algumas caixas de som não conseguiam aleatorizar as musicas inseridas por um pendrive já que elas leem os arquivos em ordem alfábetica sempre. As famosas caixas JBL conseguem tocar randomizadas, pois conseguimos realizar a conexão por bluetooth e pelo aplicativo do reprodutor de áudio utilizar a opção para tocar de maneira aleatória.

## Objetivo

Criar uma maneira de aleatorizar os arquivos de música (no PC) para serem reproduzidos pela caixa de som que não possuem função de randomizar a playlist.

## Projeto Estratégia

Obter endereço de uma pasta onde somente arquivos seriam copiados para uma pasta nova no mesmo endereço da pasta onde os arquivos originais estão. Porém, os novos arquivos consistem de números de 0 até o total de arquivos que contém na pasta menos um em vez dos nomes anteriores. Isto resultaria em uma ordem aleatória mesmo as pastas sendo organizadas por ordem alfabética. Dois pontos importantes foram necessários para o projeto. 

* Pastas seriam ignoradas dentro da pasta onde estão as músicas, ou seja, só copiará arquivos e não pastas.
* O endereço precisa ser válido, caso não for informar o usuário que o endereço não é válido.

## Projeto Real

O projeto consistiu de criar um programa com uma GUI com opções básicas que conseguisse randomizar os arquivos de áudio que são abrir a pasta onde estão os arquivos de áudio e randomizar os mesmos (bagunçar). Design da janela do programa abaixo.

![Baguncinha](https://i.imgur.com/nR55ifO.png "Janela do programa Baguncinha")

Observe que há duas maneiras de informamos a pasta onde os arquivos estão, o primeiro é copiar o endereço completo e colar onde possui o espaço em branco para digitar. Outra maneira é utilizar o botão "Abrir" onde facilitaria informar o endereço e evitaria possíveis entradas erradas. Figura abaixo mostra a janela aberta quando se clica em "Abrir".

![Botão Abrir](https://i.imgur.com/MlsGzjU.png "Janela para pesquisar o diretório da pasta")

Após informar o diretório da pasta, basta clicar no botão bagunçar onde o mesmo vai copiar os arquivos da pasta alvo (onde possui as musicas, por exemplo) para uma pasta nova com um acréscimo de "baguncinha" no nome anterior da pasta.

Abaixo temos um exemplo da funcionalidade. Inicialmente escolhemos uma pasta com arquivos de música qualquer. E então carregamos seu diretório no espaço de edição de texto.


![Pasta genérica](https://i.imgur.com/84sUuJK.png "Pasta com arquivos de áudio")

![Selecionando pasta](https://i.imgur.com/em1jFea.png "Selecionando com 'Abrir' a pasta alvo")

Após selecionado basta clicar no botão "Bagunçar" onde verifica se o diretorio é válido e então cria uma pasta nova, copia os arquivos da pasta alvo para a pasta nova e renomea os arquivos com números de maneira randomica. Abaixo temos a pasta criada e os arquivos randomizados com números.

![Bagunçar](https://i.imgur.com/zKeF9JT.png "Clicando no botão bagunçar para processar os dados")

![Arquivos Novos](https://i.imgur.com/qz77zMW.png "Arquivos da pasta nova randomizada")

![Pastas](https://i.imgur.com/qz77zMW.png "Criação de uma nova pasta no mesmo diretório da anterior")

A nova pasta com os arquivos randomizados possui um acréscimo de "baguncinha" como citado antes e todos os arquivos foram sorteados e renomeados para números em ordem crescente. 

## Requisitos para rodar o código

Instalar o PyQt5 no computador. Ou usar a distribuição Anaconda onde a mesma possui o PyQt5. Nesse caso abaixo eu utilizei o Spyder para executar.

![Spyder](https://i.imgur.com/luV8GLQ.png "Executando o main no spyder para rodar o código") 

**OBS:** O que entreguei para o meu amigo foi uma pasta com os arquivos e um '.exe' para executar sem precisar baixar o PyQt5, pois os arquivos do PyQt5 que são pré-requisito para funcionamento do programa estão na pasta. Para isso utilizei o pacote PyInstaller. Segue o link .rar com a pasta com o .exe: <http://www.mediafire.com/file/uzx0z46tb1w59z3/Baguncinha.rar/file>

## Melhorias no projeto

As melhorias que tenho em mente são:

1. Adicionar mais comentários no código;
2. Quebrar mais o código em funções ou até mesmo em novas classes;
3. Trabalhar melhor as possíveis excessões ou erros que podem ocorrer;
4. Mudança no código em geral utilizando mais os paradigmas da programação.

## Conclusão

O programa atende bem ao proposto randomizando as musicas utilizando o PC e passar a nova pasta para um pendrive para plugar numa caixa de som e ouvir as músicas aleatorizadas. O programa ainda pode randomizar outros arquivos como, por exemplo, arquivos de fotos. Sendo então de uso geral, não só limitado a arquivos de áudio. 
