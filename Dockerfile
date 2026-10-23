# syntax=docker/dockerfile:1
# Imagem de estudo: Spark 4.2 com o jar do Delta ja baixado (armazenamento 100% local)
# Base fixada pelo digest, que nunca muda: quay.io/jupyter/pyspark-notebook (Spark 4.2.0, Python 3.13), baixada em 08/10/2026
FROM quay.io/jupyter/pyspark-notebook@sha256:7cad53570e4d168b17a453d190601c677a08836992f8b04888a627a5532e3614

USER root
# "python -m pip" garante que as bibliotecas vao para o mesmo python que usamos depois
# pandas 3 ainda nao e totalmente suportado pelo PySpark 4.2 (ele avisa)
RUN python -m pip install --no-cache-dir "pandas<3" pyspark==4.2.0 importlib_metadata==8.7.1 \
 && python -m pip install --no-cache-dir delta-spark==4.4.0 --no-deps
USER ${NB_UID}

# Baixa uma vez o jar do Delta para o cache do Ivy dentro da imagem, com a mesma funcao que as sessoes da aula 5 usam:
# configure_spark_with_delta_pip escolhe o pacote certo para o Spark instalado (io.delta:delta-spark_4.2_2.13:4.4.0).
# Depois disso o notebook resolve o pacote pelo cache, sem internet.
RUN python - <<'PY'
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
configure_spark_with_delta_pip(SparkSession.builder.master("local[1]")).getOrCreate().stop()
PY
