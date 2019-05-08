# Baguncinha

## Problemática

Um amigo meu me contou o seguinte problema: Algumas caixas de som não conseguiam aleatorizar as musicas inseridas por um pendrive, por exemplo. As famosas caixas JBL conseguem tocar randomizadas, pois conseguimos realizar a conexão por bluetooth e pelo aplicativo do reprodutor de áudio utilizar a opção para tocar de maneira aleatória.

## Objetivo

Criar uma maneira de aleatorizar os arquivos de música (no PC) para serem reproduzidos pela caixa de som.

## Projeto Estratégia

Obter endereço de uma pasta onde somente arquivos seriam copiados para uma pasta nova no mesmo endereço da pasta onde os arquivos originais estão. Porém, os novos arquivos consistem de números de 0 até o total de arquivos que contém na pasta menos um em vez dos nomes anteriores. Isto resultaria em uma ordem aleatória mesmo as pastas sendo organizadas por ordem alfabética. Dois pontos importantes foram necessários para o projeto. 

* Pastas seriam ignoradas dentro da pasta onde estão as músicas, ou seja, só copiará arquivos e não pastas.
* O endereço precisa ser válido, caso não for informar o usuário que o endereço não é válido.

## Projeto Real

O projeto consistiu de criar um programa com uma GUI com opções básicas que conseguisse randomizar os arquivos de áudio que são abrir a pasta onde estão os arquivos de áudio e randomizar os mesmos (bagunçar). Design da janela do programa abaixo.

![Baguncinha](https://i.imgur.com/nR55ifO.png "Janela do programa Baguncinha")

Observe que há duas maneiras de informamos a pasta onde os arquivos estão, o primeiro é copiar o endereço completo e colar onde possui o espaço em branco para digitar. Outra maneira é utilizar o botão "Abrir" onde facilitaria informar o endereço e evitaria possíveis entradas erradas. Figura abaixo mostra a janela aberta quando se clica em "Abrir".

![Botão Abrir](https://i.imgur.com/MlsGzjU.png "Janela para pesquisar o diretório da pasta")

Após informar o diretório da pasta, basta clicar no botão bagunçar onde o mesmo vai copiar os arquivos da pasta alvo (onde possui as musicas, por exemplo) para uma pasta nova com um acréscimo de "ba

Abaixo temos um exemplo da funcionalidade. Inicialmente escolhemos uma pasta com arquivos de música qualquer. E então carregamos seu diretório no espaço de edição de texto.


![Pasta genérica](https://i.imgur.com/84sUuJK.png "Pasta com arquivos de áudio")

![Selecionando pasta](https://i.imgur.com/em1jFea.png "Selecionando com 'Abrir' a pasta alvo")

Após selecionado basta clicar no botão "Bagunçar" onde verifica se o diretorio é válido e então cria uma pasta nova, copia os arquivos da pasta alvo para a pasta nova e renomea os arquivos com números de maneira randomica. Abaixo temos a pasta criada e os arquivos randomizados com números.

![Bagunçar](https://i.imgur.com/zKeF9JT.png "Clicando no botão bagunçar para processar os dados")

![Arquivos Novos](https://i.imgur.com/qz77zMW.png "Arquivos da pasta nova randomizada")



