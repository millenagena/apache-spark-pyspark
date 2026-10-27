# Apache Spark com PySpark

Projeto do curso de Spark com PySpark da Alura. Você faz parte do time de dados da **Arena Analytics**, uma empresa
que produz estatísticas de Copa do Mundo para transmissões de TV e de streaming, e vai construir com Spark o
pipeline que transforma os dados do fornecedor nessas estatísticas.

Este repositório traz o ambiente (Docker), os dados e os notebooks do curso. O código, você escreve junto nas aulas.

## O que você vai construir

| Aula | Tema | O que o projeto ganha |
|---|---|---|
| 1 | Introdução ao Spark | o ambiente no ar e a primeira leitura dos dados |
| 2 | Transformações com DataFrames | dados limpos e as primeiras estatísticas, em `src/wc_pipeline/transformacoes.py` |
| 3 | Spark SQL | consultas em SQL para o time de analytics, em `sql/` |
| 4 | Otimização no Spark | os passes de cada seleção nas Copas de 2018 e 2022, a partir do feed de eventos, gravados em Parquet em `data/out/` |
| 5 | Escrita e Delta Lake | as partidas e o resumo por seleção como tabelas Delta em `data/out/`, recebendo a Copa de 2026 e uma correção do fornecedor sem reprocessar tudo |

## Estrutura

```
apache-spark-pyspark/
├── Dockerfile           a receita da imagem do curso (Jupyter, Python, Java e Spark 4.2)
├── docker-compose.yml   como subir o container
├── .gitignore           o que não vai para o git (as saídas que o código gera)
├── data/                os dados do fornecedor (veja data/README.md)
├── src/wc_pipeline/     o código do projeto (começa só com os schemas dos arquivos)
└── notebooks/           os notebooks de cada aula, um por vídeo
```

Ao longo do curso aparece a pasta `sql/`, criada pelos notebooks, e as saídas em `data/out/`,
`data/warehouse/` e `data/externas/`. As saídas ficam fora do git: são geradas pelo código e podem ser apagadas e
recriadas a qualquer momento.

## Pré-requisito: Docker

Você não precisa instalar Java, Python nem Spark: eles vêm dentro do container. Só precisa do Docker com o Docker
Compose. O jeito mais simples, em qualquer sistema, é o **Docker Desktop**, que já traz os dois:

| Sistema | O que instalar |
|---|---|
| Windows | [Docker Desktop para Windows](https://docs.docker.com/desktop/setup/install/windows-install/), com o WSL 2 |
| Mac (Apple Silicon ou Intel) | [Docker Desktop para Mac](https://docs.docker.com/desktop/setup/install/mac-install/) |
| Linux | [Docker Desktop para Linux](https://docs.docker.com/desktop/setup/install/linux/), ou o Docker Engine com o [plugin do Compose](https://docs.docker.com/compose/install/linux/) |

Para conferir a instalação, no terminal do seu computador:

```bash
docker --version
docker compose version
```

Os dois comandos devem mostrar uma versão. No Windows e no Mac, o Docker Desktop precisa estar aberto antes de
rodar qualquer comando `docker`.

## Baixar o projeto

O ponto de partida do curso está na branch `aula-0`. Com o git:

```bash
git clone -b aula-0 https://github.com/millenagena/apache-spark-pyspark.git
cd apache-spark-pyspark
```

Sem o git: no GitHub, escolha a branch `aula-0`, use **Code > Download ZIP**, descompacte e abra o terminal dentro
da pasta.

## Subir o ambiente

No terminal do seu computador (PowerShell no Windows, Terminal no Mac e no Linux), dentro da pasta do projeto:

| Quando | Comando | O que faz |
|---|---|---|
| a primeira vez | `docker compose up --build` | monta a imagem e sobe o container (demora alguns minutos) |
| para parar | `Ctrl+C` e depois `docker compose down` | para e remove o container; a imagem e os arquivos continuam |
| das próximas vezes | `docker compose up` | sobe o container a partir da imagem que já existe |
| se o `Dockerfile` mudar | `docker compose up --build` | monta a imagem de novo |

Com o container no ar:

- Jupyter: http://localhost:8888/lab?token=estudo
- Spark UI: http://localhost:4040, enquanto houver uma sessão Spark ativa. Cada notebook aberto tem a sua sessão: a
  segunda usa a porta 4041, a terceira a 4042, até a 4045.

## Onde ficam os seus arquivos

O container enxerga a pasta do projeto como `/home/jovyan/work` (ou `~/work`). `jovyan` é o usuário padrão das
imagens do Jupyter, e `work` é o nome que o `docker-compose.yml` dá para a pasta do projeto dentro do container.
É a mesma pasta, vista de dois lados: o que você salva no Jupyter aparece na pasta do projeto no seu computador, e
continua lá depois do `docker compose down`.

## Conferir o ambiente

No Jupyter, abra `notebooks/01_introducao_spark/02_preparando_o_ambiente.ipynb` e rode as células. Se aparecer
`Spark: 4.2.0`, está tudo certo.

Siga os notebooks na ordem. Cada um termina com `spark.stop()`, que encerra a sessão Spark e libera a memória.

## Onde rodar cada comando

- **Terminal do seu computador:** os comandos `docker` e `git`.
- **Terminal do Jupyter** (File > New > Terminal): os comandos que rodam dentro do container, como `python`. Entre
  antes na pasta do projeto com `cd ~/work`.

## Se algo der errado

| Sintoma | O que fazer |
|---|---|
| `docker: command not found`, ou erro ao conectar com o Docker | abra o Docker Desktop e espere ele terminar de iniciar |
| erro de porta em uso (`port is already allocated`) na 8888 ou na 4040 | outro programa usa a porta (por exemplo, outro Jupyter): feche esse programa e rode `docker compose up` de novo |
| o Jupyter pede uma senha ou um token | use o endereço completo, com `?token=estudo` no fim |
| a Spark UI não abre na 4040 | ela só existe enquanto uma sessão Spark está ativa; com vários notebooks abertos, veja a porta com `spark.sparkContext.uiWebUrl` |
| o Jupyter ficou lento ou a Spark UI foi para outra porta | use Kernel > Shut Down All Kernels para encerrar as sessões antigas |
| na aula 5, `ClassNotFoundException` ao criar a sessão com o Delta Lake | use Kernel > Restart Kernel e rode o notebook de novo a partir da primeira célula |

### Mac e Linux

O ambiente do curso foi gravado e testado no Windows, com o Docker Desktop. Como tudo roda dentro do container, ele
deve funcionar igual no Mac e no Linux, mas cada sistema tem as suas particularidades na instalação do Docker e no
acesso às pastas. Um exemplo no Linux: o container grava na pasta do projeto com o usuário `jovyan`, de id 1000, e
esse usuário precisa de permissão de escrita nela. Se o seu usuário tiver outro id (confira com `id -u`), a gravação
pode falhar com `Permission denied`. A documentação das imagens do Jupyter explica as opções em
[Common Features](https://jupyter-docker-stacks-pt-br.readthedocs.io/pt-br/latest/using/common.html).

Se aparecer um erro na configuração do ambiente que não está nesta tabela, pesquise a mensagem de erro, consulte a
documentação do [Docker](https://docs.docker.com/) e, se quiser, peça apoio a um assistente de IA, como um agente
de código, para diagnosticar e ajustar a configuração. Leia o que ele propõe antes de aplicar e, se tiver dúvida,
traga para o fórum do curso.

## Dados

A pasta `data/` traz os dados que o fornecedor mandou para a Arena Analytics. O `data/README.md` descreve cada
conjunto e as suas colunas.
