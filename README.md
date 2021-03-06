# GeoLiteraturas

O objectivo deste projecto é explorar o texto nas suas vertentes geográficas, extraindo automaticamente as referências a locais de um corpus de texto.

## Usar
* Colocar os livros que vão ser tratados pelo script na pasta `pubs`;
* `python locationCounter.py` - cria uma `matriz.csv` para cada obra ocorrências de cada concelho (eventualmente pode imprimir na consola o total de cada concelho)

Convém que quando se corre este script se subtraia a lista anterior, uma vez que esta pode ser indo corrigida.

### Step by Step
1. Download de todos os livros do Projecto Adamastor
 * (ou) usando o plugin DownThem All para Firefox
 * (ou) usando o script (ou os livros já descarregados) [adamaSHtor](https://github.com/marado/adamaSHtor)
2. Conversão de epub para txt utilizando o Epub2txt Python
3. Download do data set que contém os concelhos Portugueses
4. Comparar a lista de concelhos com o conjunto de textos

## ToDo
* Saber o número de ocorrências de um concelho num livro
* Saber o número de ocorrências de um concelho no conjunto total dos livros
* Saber o número de ocorrências de um concelho no conjunto de livros de um autor
* Mapear o texto dos livros (colocando um excerto num mapa)

## Problemas
* Nomes das localidades podem ser confundidos com outros nomes (ex.: Corvo).
 * Alternativa: Optar para já por concelhos, para minimizar este problema.
 * Possível solução: linkar as localidades ao texto de forma a poder haver uma verificação humana
* Maiúsculas/Minúsculas (mais problemático no caso do acordo ortográfico)
* Palavras que podem ser parte de outras (ex.: o concelho de Mora)

## Fontes Utilizadas
* Projecto Adamastor - http://projectoadamastor.org/
* Informação sobre as localidades - http://centraldedados.pt/codigos_postais/

## Software Utilizado
* Epub2txt Python - Converter os livros em epub para txt - https://code.google.com/p/yaepub2txt/downloads/detail?name=epub2txt.py
* Download dos livros:
 * (ou) https://addons.mozilla.org/en-US/firefox/addon/downthemall/
 * (ou) https://github.com/marado/adamaSHtor

## Lista de Autores
```
Alexandre Herculano
Almeida Garrett
Álvaro do Carvalhal
Ana de Castro Osório
Antero de Quental
António Nobre
Augusto dos Anjos
Bernardo Guimarães
Camilo Castelo Branco
Camilo Pessanha
Cândido de Figueiredo
Cesário Verde
Eça de Queirós
Eça de Queirós e Ramalho Ortigão
Émile Souvestre
Fernando Pessoa
Fialho de Almeida
Florbela Espanca
Guerra Junqueiro
H. Rider Haggard
João da Câmara
Machado de Assis
Mário de Sá-Carneiro
Melo de Matos
Raul Brandão
Venceslau de Morais
William Shakespeare
```
