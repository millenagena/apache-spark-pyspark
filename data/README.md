# Dados do projeto

Os dados que o fornecedor mandou para a Arena Analytics. Tema: Copa do Mundo de futebol (edições, partidas e
jogadores).

| Pasta | O que é | Origem |
|---|---|---|
| `raw/` | o histórico das Copas em três arquivos CSV: as edições (`WorldCups.csv`), as partidas (`WorldCupMatches.csv`) e as escalações (`WorldCupPlayers.csv`). São 18 edições, de 1950 a 2018 | amostra **sintética**, gerada para o curso: os nomes das seleções são reais, mas os resultados e os jogadores foram sorteados |
| `events/` | o feed de eventos das partidas, lance a lance, em Parquet: 1.688.542 lances de 562 partidas | simulado para o curso. Os gols batem com o placar de cada partida |
| `raw_2026/` | a Copa do Mundo de 2026, nos mesmos três arquivos CSV: 104 partidas e as escalações | dados da Copa de 2026 |
| `events_2026/` | o feed de eventos de 2026, em Parquet: 312.333 lances de 104 partidas | simulado para o curso a partir de `raw_2026/` |

Em `raw_2026/`, as partidas decididas nos pênaltis (`Win conditions` = `PENALTY_SHOOTOUT`) trazem no placar também os
gols da disputa de pênaltis, porque é assim que a fonte dos dados (football-data.org) registra o placar final. Exemplo:
Germany 4x5 Paraguay foi 1x1 no jogo e 3x4 nos pênaltis.

Colunas do feed de eventos: `event_id`, `MatchID`, `period`, `minute`, `event_type`, `team`, `player_id`. Os tipos de
evento são passe, disputa de bola, falta, chute, corte, escanteio e gol.

Como em todo dado que chega de fora, os arquivos do fornecedor não vêm perfeitos. Fique de olho.

Não mude os nomes nem a estrutura das pastas: os notebooks leem os arquivos por esses caminhos.
