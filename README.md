
<!-- Logo -->

<h1 align="center" style="font-family: Ubuntu; font-size: 45px; color: #333; margin-bottom: 0">
  Atividade de IA 2022.2 - Frozen Lake (Busca e QLearn)
</h1>

<!-- Description -->

<h4 align="center">
	UFBA - Instituto de Computação - MATA64 - 2022.2 - Natan Moura e Caio Nery
</h4>

<!-- Summary -->

<h2>Guia</h2>

- [:book: Introdução](#book-introdução)
- [:rocket: Tecnologias](#rocket-tecnologias)
- [:boom: Como rodar](#boom-como-rodar)

<a id="doc"></a>

<div align="justify">

<a id="introdução"></a>

## :book: Introdução

Este repositório contém 2 aplicações simples com propósitos distintos:
- ["qlearn"](https://github.com/ntsmoura/IA2022.2/blob/master/qlearn.py) disponibilza uma interface simples para treinar e executadr modelos gerados utilizando qlearn, dos ambientes do [Gym](https://www.gymlibrary.dev/content/basic_usage/) : [Taxi](https://www.gymlibrary.dev/environments/toy_text/taxi/), [Cliff Walking](https://www.gymlibrary.dev/environments/toy_text/cliff_walking/) e [Frozen Lake](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/).
- ["search"](https://github.com/ntsmoura/IA2022.2/blob/master/search.py) realiza buscas em largura e profundidade para um mapeamento controlado do ambiente de [Frozen Lake](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/), ignorando a existência de buracos e mapeando somente gelo e o estado final. O mapeamento está disponível através do [json](https://github.com/ntsmoura/IA2022.2/blob/master/frozen_lake_mapping.json).

<a id="tecnologias"></a>

## :rocket: Tecnologias

Essa aplicação utiliza as seguintes tecnologias:

- [ThreeJs](https://threejs.org/)

<a id="como-executar"></a>

## :boom: Como rodar

#### Prerequisitos

Para rodar essa aplicação é necessário somente um servidor HTTP, como Apache, VS Code Live Server, Nginx, entre outros. Mostrarei um exemplo utilizando o apache através do [Xampp](https://www.apachefriends.org/pt_br/index.html)

#### Rodando com xampp

Após instalar o xampp e configurar o terminal para o diretório principal de onde instalei-o, executo a seguinte sequência de comandos:

```sh
# Muda para o diretório htdocs e clona o repositório
$ cd htdocs
$ git clone https://github.com/MATA65-2022-1/atividade-01---visita-guiada-virtual-ntsmoura/

```

Ao clonar o repositório estou fazendo download de todas as dependências da aplicação, já que estas estão incluídas na pasta [Assets](https://github.com/MATA65-2022-1/atividade-01---visita-guiada-virtual-ntsmoura/tree/main/Assets). No caso do Xampp, eu inicio o servidor Apache e em qualquer browser acesso o link http://localhost/atividade-01---visita-guiada-virtual-ntsmoura/Passeio.html. Algo similar a isto deve aparecer:
	
</div>


