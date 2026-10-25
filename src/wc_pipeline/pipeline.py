"""Job das partidas da Arena Analytics (construido na aula 5).

Uso, no terminal do Jupyter, dentro de ~/work:
    spark-submit --master "local[*]" --packages io.delta:delta-spark_4.2_2.13:4.4.0 src/wc_pipeline/pipeline.py data/raw
    spark-submit --master "local[*]" --packages io.delta:delta-spark_4.2_2.13:4.4.0 src/wc_pipeline/pipeline.py data/raw_2026
"""
import sys

from pyspark.sql import SparkSession

from wc_pipeline.schemas import MATCHES
from wc_pipeline.transformacoes import limpar_partidas, partidas_por_selecao, resumo_por_selecao

PASTA_RAW = sys.argv[1]
SAIDA = "data/out/producao"

spark = (
    SparkSession.builder
    .appName("arena-job-partidas")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

partidas = limpar_partidas(
    spark.read.option("header", "true").schema(MATCHES).csv(f"{PASTA_RAW}/WorldCupMatches.csv")
)
resumo = resumo_por_selecao(partidas_por_selecao(partidas))

for tabela, df in [("partidas", partidas), ("resumo_selecoes", resumo)]:
    (
        df.repartition("ano").write.format("delta").mode("overwrite")
        .option("partitionOverwriteMode", "dynamic")
        .partitionBy("ano")
        .save(f"{SAIDA}/{tabela}")
    )

print("partidas na saída:", spark.read.format("delta").load(f"{SAIDA}/partidas").count())
spark.stop()
