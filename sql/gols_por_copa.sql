SELECT ano,
       COUNT(*)                   AS partidas,
       SUM(total_gols)            AS gols,
       ROUND(AVG(total_gols), 2)  AS media_gols,
       ROUND(AVG(publico), 0)     AS publico_medio
FROM partidas
GROUP BY ano
ORDER BY ano
