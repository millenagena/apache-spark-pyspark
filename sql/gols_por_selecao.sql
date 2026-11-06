WITH linhas_por_selecao AS (
    SELECT 
        ano, 
        mandante AS selecao,
        gols_mandante AS gols_pro,
        gols_visitante AS gols_contra
    FROM partidas
    UNION ALL
    SELECT 
        ano, 
        visitante AS selecao,
        gols_visitante AS gols_pro,
        gols_mandante AS gols_contra
    FROM partidas
)

SELECT ano,
       selecao,
       COUNT(*)                                                AS jogos,
       SUM(CASE WHEN gols_pro > gols_contra THEN 1 ELSE 0 END) AS vitorias,
       SUM(CASE WHEN gols_pro = gols_contra THEN 1 ELSE 0 END) AS empates,
       SUM(CASE WHEN gols_pro < gols_contra THEN 1 ELSE 0 END) AS derrotas,
       SUM(gols_pro)                                           AS gols_pro,
       SUM(gols_contra)                                        AS gols_contra,
       SUM(gols_pro) - SUM(gols_contra)                        AS saldo
FROM linhas_por_selecao
GROUP BY ano, selecao
