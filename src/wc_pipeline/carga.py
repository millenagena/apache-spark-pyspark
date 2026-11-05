from pyspark.sql import DataFrame, SparkSession

from wc_pipeline.schemas import MATCHES
from wc_pipeline.transformacoes import limpar_partidas, partidas_por_selecao, resumo_por_selecao


def ler_partidas(spark: SparkSession, pasta: str) -> DataFrame:
    return limpar_partidas(
        spark.read.option("header", "true").schema(MATCHES).csv(f"{pasta}/WorldCupMatches.csv")
    )


def gravar(df: DataFrame, caminho: str) -> None:
    (
        df.write.format("delta").mode("overwrite")
        .option("partitionOverwriteMode", "dynamic")
        .partitionBy("ano")
        .save(caminho)
    )


def carregar_copa(spark: SparkSession, pasta: str, saida: str) -> None:
    partidas = ler_partidas(spark, pasta)
    gravar(partidas, f"{saida}/partidas")
    gravar(resumo_por_selecao(partidas_por_selecao(partidas)), f"{saida}/resumo_selecoes")
