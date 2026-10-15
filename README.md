# Apache Spark com PySpark para Big Data

Projeto do curso de Spark com PySpark da Alura. Você faz parte do time de dados da **Arena Analytics**, uma empresa
que produz estatísticas de Copa do Mundo para transmissões de TV e de streaming, e vai construir com Spark o
pipeline que transforma os dados do fornecedor nessas estatísticas.

Este repositório traz o ambiente (Docker), os dados e os notebooks do curso. O código, você escreve junto nas aulas.

## Estrutura

```
apache-spark-pyspark-big-data/
├── Dockerfile           a receita da imagem do curso (Jupyter, Python, Java e Spark 4.2)
├── docker-compose.yml   como subir o container
├── data/                os dados do fornecedor (veja data/README.md)
├── src/wc_pipeline/     o código do projeto (começa com os schemas dos arquivos)
└── notebooks/           os notebooks de cada aula
```

## Pré-requisito

Docker instalado (no Windows, com o WSL 2). Você não precisa instalar Java, Python nem Spark: eles vêm dentro do
container.

## Subir o ambiente

No terminal do seu computador, dentro da pasta do projeto:

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

## Conferir o ambiente

No Jupyter, abra `notebooks/01_introducao_spark/02_preparando_o_ambiente.ipynb` e rode as células. Se aparecer
`Spark: 4.2.0`, está tudo certo.

Siga os notebooks na ordem. Cada um termina com `spark.stop()`, que encerra a sessão Spark e libera a memória.

## Onde rodar cada comando

- **Terminal do seu computador:** os comandos `docker compose`.
- **Terminal do Jupyter** (File > New > Terminal): `python` e `spark-submit`. Entre antes em `~/work`, que é a pasta
  do projeto dentro do container.

## Dados

A pasta `data/` traz os dados que o fornecedor mandou para a Arena Analytics. O `data/README.md` descreve cada
conjunto e as suas colunas.
