from pyspark.sql import DataFrame, functions as F

FORMATO_DATA = "dd MMM yyyy - HH:mm"

def limpar_partidas(partidas_brutas: DataFrame) -> DataFrame:
    # video 2.1: limpeza
    partidas_limpas = (
        partidas_brutas
        .filter(F.col("MatchID").isNotNull())
        .dropDuplicates(["MatchID"])
    )

    # video 2.2: padronizacao
    partidas = partidas_limpas.select(
        F.col("Year").alias("ano"),
        F.col("MatchID").alias("match_id"),
        F.col("Stage").alias("fase"),
        F.col("Home Team Name").alias("mandante"),
        F.col("Home Team Goals").alias("gols_mandante"),
        F.col("Away Team Goals").alias("gols_visitante"),
        F.col("Away Team Name").alias("visitante"),
        F.col("Attendance").alias("publico"),
        F.col("Datetime").alias("data_partida"),
    )

    partidas = partidas.withColumn(
        "publico",
        F.regexp_replace("publico", ",", "").cast("int"),
    )

    partidas = partidas.withColumn(
        "data_partida",
        F.to_timestamp("data_partida", FORMATO_DATA),
    )

    partidas = (
        partidas
        .withColumn("total_gols", F.col("gols_mandante") + F.col("gols_visitante"))
        .withColumn(
            "resultado",
            F.when(F.col("gols_mandante") > F.col("gols_visitante"), "mandante")
             .when(F.col("gols_mandante") < F.col("gols_visitante"), "visitante")
             .otherwise("empate"),
        )
    )
    return partidas


def partidas_por_selecao(partidas: DataFrame) -> DataFrame:
    como_mandante = partidas.select(
        "ano",
        F.col("mandante").alias("selecao"),
        F.col("gols_mandante").alias("gols_pro"),
        F.col("gols_visitante").alias("gols_contra"),
    )
    como_visitante = partidas.select(
        "ano",
        F.col("visitante").alias("selecao"),
        F.col("gols_visitante").alias("gols_pro"),
        F.col("gols_mandante").alias("gols_contra"),
    )
    por_selecao = como_mandante.unionByName(como_visitante)

    por_selecao = por_selecao.withColumn(
        "resultado",
        F.when(F.col("gols_pro") > F.col("gols_contra"), "V")
         .when(F.col("gols_pro") < F.col("gols_contra"), "D")
         .otherwise("E"),
    )
    return por_selecao


def resumo_por_selecao(por_selecao: DataFrame) -> DataFrame:
    tabela_selecoes = (
        por_selecao.groupBy("ano", "selecao")
        .agg(
            F.count("*").alias("jogos"),
            F.sum(F.when(F.col("resultado") == "V", 1).otherwise(0)).alias("vitorias"),
            F.sum(F.when(F.col("resultado") == "E", 1).otherwise(0)).alias("empates"),
            F.sum(F.when(F.col("resultado") == "D", 1).otherwise(0)).alias("derrotas"),
            F.sum("gols_pro").alias("gols_pro"),
            F.sum("gols_contra").alias("gols_contra"),
        )
        .withColumn("saldo", F.col("gols_pro") - F.col("gols_contra"))
    )
    return tabela_selecoes
