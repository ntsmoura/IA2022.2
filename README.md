
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

- [Python3.10+](https://www.python.org/downloads/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Gym](https://www.gymlibrary.dev/)

<a id="como-executar"></a>

## :boom: Como rodar

Inicialmente clone o diretório e mude para a pasta principal:

```sh
# Clone de repo
$ git clone https://github.com/ntsmoura/IA2022.2
$ cd IA2022.2

```

Se já tiver o pipenv instalado, basta instalar as dependências e rodar o pipenv shell:

```sh
# Rodando pipenv shell
$ pipenv install
$ pipenv shell
```	

E para executar qualquer um dos algoritmos, basta utilizar o comando do python instalado:

```sh
# Rodando algoritmos
$ py qlearn.py
$ py search.py
```

Obs: Se houver erro em instalar o gym[box2d] faça o seguinte
	
```sh
# Instalando box2d
$ pip install swig
$ pip install gym[box2d]
$ pipenv install
```
	
</div>


