# Atividade de IA 2022.2 - Frozen Lake (Busca e QLearn)

<!-- Logo -->

<h1 align="center" style="font-family: Ubuntu; font-size: 45px; color: #333; margin-bottom: 0">
  Passeios sobre modelo Sponza
</h1>

<!-- Description -->

<h4 align="center">
	UFBA - Instituto de Computação - MATE65 - 2022.1 - Natan Moura
</h4>

<!-- Summary -->

<h2>Guia</h2>

- [:book: Introdução](#book-introdução)
- [:rocket: Tecnologias](#rocket-tecnologias)
- [:boom: Como rodar](#boom-como-rodar)
    - [Prerequisitos](#prerequisitos)
    - [Rodando com xampp](#rodando-com-xampp)
- [:sparkles: Tipos de passeio](#sparkles-tipos-de-passeio)
- [:no_entry: Confinamento ao modelo](#no_entry-confinamento-ao-modelo)
- [:european_castle: Cubemap background](#european_castle-cubemap-background)

<a id="doc"></a>

<div align="justify">

<a id="introdução"></a>

## :book: Introdução

Esta é uma aplicação feita com ThreeJs para a disciplina MATE65 - Computação Gráfica com o objetivo de implementar três tipos de passeio sobre o modelo [Sponza](https://github.com/jimmiebergmann/Sponza). Os passeios correspondem a três modos distinto de visão:
- Modo "A pé" - Remete a uma pessoa caminhando dentro do modelo
- Modo "Drone" - Remete aos graus de liberdade de um drone voando sobre o modelo
- Modo "Visita Guiada" - Remete a uma visita automática sobre o modelo com pontos pré-definidos e um guia amigável

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

