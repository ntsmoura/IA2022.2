# Atividade de IA 2022.2 - Frozen Lake (Busca e QLearn)

## Contexto



## Objetivo:

O objetivo da atividade é construir uma aplicação em [Three.JS](https://threejs.org/) que permita fazer um passeio virtual nesse modelo. Para tanto voces devem fornecer ao usuário 3 modalidades de percurso:

1. **Modo "Andando a pé"**: O usuário poderá andar pelo modelo como uma pessoa o faria no modelo real;

1. **Modo "Drone"**: Simular os graus de liberdade de um drone se movendo pelo espaço do modelo[^1];

1. **Modo "Visita Guiada"**: Nesse modo um caminho pré-definido deve ser fornecido, levando o usuário a pelo menos 4 pontos relevantes do modelo.

Voce pode utiliziar qualquer um dos [*controlers*](https://threejs.org/docs/index.html?q=control) disponíveis no *Three.JS*. No entanto, esses *controlers* devem ser customizados, de tal forma que permitam a real sensação de uma visita a pé, um sobrevoo ou uma visita guidada automática. Em outras palavras, questões como escala, velocidade do movimento e tipo de controle disponível devem ser levadas em conta. 

## Requisitos:

- Como o modelo não contempla a parte externa do átrio do palácio, os passeios devem ser restritos aos limites do modelo;
- Considere a questão da escala ao configurar o movimento nos passeios, de modo a garantir uma sensação de estar mesmo dentro do espaço real;
- No modo **"visita guiada"** o usuário deverá ter um avatar como "guia" para conduzi-lo ao longo do percurso. O avatar deverá ser um modelo articulado e animado[^2] que irá à frente do usuário durante o percurso.  

## Entrega e Critérios de Avaliação:

O trabalho será submetido individualmente através do repositório disponibilizado pelo professor, via GitHub Classroom, para essa atividade. 
> **Não serão consideradas versões enviadas por e-mail, Google Classroom, Discord, ou outros meios.**

O trabalho será avaliado a partir dos seguintes critérios:

| Critério | Pontuação |
| :--- | :---: |
| 1. Documentação (README) | 0,5 |
| 2. Configuração do cenário | 0,5 | 
| 3. Modo "Andando à Pé" | 2,0 |
| 4. Modo "Drone" | 2,0 |
| 5. Modo "Visita Guiada" |  |
| - Movimentação | 2,0 |
| - Avatar do "guia" | 1,5 |
| 6. Confinamento dos movimentos ao modelo | 1,5 |

## Penalidades:              

> Será aplicada a penalização de -1,0 pto por dia de atraso (verificado via data da ultima submissão no repositório)
> 
>> **Em casos de plágio (total ou parcial) todos os envolvidos terão suas avaliações zeradas**. 

## Referências:

[1] Peter SHIRLEY, Michael ASHIKHMIN, Steve MARSCHNER. **Fundamentals of Computer Graphics**. AK Peters/CRC Press, 5th Edition, 2021.

[2] John F. Hughes, Andries van Dam, Morgan McGuire, David F. Sklar, James D. Foley, Steven K. Feiner. **Computer Graphics : Principles and 
Practice Third Edition in C**. Addison-Weslley. 2013.

[3] DIRKSEN, Jos. **Learn Three. js: Programming 3D animations and visualizations for the web with HTML5 and WebGL**. Packt Publishing Ltd, 2018.

[^1]: a colisão entre os elementos do espaço, como colunas, cortinas, etc, podem ser desconsideradas nesse caso. 
[^2]: nos exemplos do *Three.JS* voce pode encontrar alguns modelos desse tipo. Mas se quiser pode escolher outros em sites especializados como o [*SketchFab*](https://sketchfab.com/) fica a seu critério.-->

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


