# Dados do projeto

Os dados que o fornecedor mandou para a Arena Analytics. Tema: Copa do Mundo de futebol (edições, partidas e
jogadores).

| Pasta | O que é | Origem |
|---|---|---|
| `raw/` | o histórico das Copas masculinas em três arquivos CSV: as edições (`WorldCups.csv`), as partidas (`WorldCupMatches.csv`) e os jogadores (`WorldCupPlayers.csv`). São 22 Copas, de 1930 a 2022, com 964 partidas | várias fontes juntas pela data e pelas duas seleções. A Copa de 2026 continua em `raw_2026/` |
| `events/` | os lances em Parquet: 195.747 linhas, no mesmo `MatchID` das partidas | gols, cartões e substituições de todas as partidas; passes, chutes, duelos, faltas e tiros livres nas partidas em que existe um feed lance a lance |
| `raw_2026/` | a Copa do Mundo de 2026, nos mesmos três arquivos CSV: 104 partidas e as escalações | dados da Copa de 2026 |
| `events_2026/` | o feed de eventos de 2026, em Parquet: 312.333 lances de 104 partidas | simulado para o curso a partir de `raw_2026/` |

Em `raw_2026/`, as partidas decididas nos pênaltis (`Win conditions` = `PENALTY_SHOOTOUT`) trazem no placar também os
gols da disputa de pênaltis, porque é assim que a fonte dos dados (football-data.org) registra o placar final. Exemplo:
Germany 4x5 Paraguay foi 1x1 no jogo e 3x4 nos pênaltis.

Em `raw/`, o placar é o do fim do jogo, com a prorrogação quando houve, e sem os gols da disputa de pênaltis. A final
de 2022 fica Argentina 3x3 France, com `Win conditions` = `PENALTY_SHOOTOUT`. Os gols da disputa estão no feed de
eventos, com `event_type` = `Shootout goal`. A soma dos eventos `Goal` de cada partida é o placar do CSV.

Público, intervalo e assistentes vêm das planilhas de 1930 a 2014. Em 2018 e 2022 esses campos ficam vazios. Alemanha
2x0 Argélia, oitavas de 2014, também não tem público na fonte: o `Attendance` de 2014 soma as outras 63 partidas.
A sigla da seleção é o código ISO de três letras (`DEU`, `ENG`, `NLD`), não a sigla da FIFA.

De 1970 a 2022, `WorldCupPlayers.csv` lista quem jogou: `Line-up` = `S` para quem começou e `N` para quem entrou.
Quem ficou no banco e não entrou não aparece. De 1930 a 1966 a ficha é a da planilha antiga, com titulares e reservas.
A coluna `Event` junta os gols e os cartões daquele jogador naquela partida (`G19'`, `OG40'`, `YC70'`, `RC88'`).

O feed de eventos tem as colunas `event_id`, `MatchID`, `period`, `minute`, `event_type`, `team`, `player_id`.
`period` é `1H`, `2H`, `ET` ou `PSO`. Os tipos são `Goal`, `Shootout goal`, `Yellow card`, `Second yellow`,
`Red card`, `Substitution`, `Pass`, `Shot`, `Duel`, `Foul` e `Free kick`. Passe existe em todas as partidas de 2018
e de 2022, e em 19 partidas antigas (1958, 1962, 1970, 1974, 1986 e 1990). Nas outras partidas o feed traz gol,
cartão e substituição, com minuto e jogador.

Fontes, unidas pela data e pelas duas seleções:

- Fjelstul World Cup Database, de Joshua C. Fjelstul, Ph.D. Partidas, placares, escalações desde 1970, gols, cartões
  e substituições, de 1930 a 2022. © 2023 Joshua C. Fjelstul, Ph.D. Licença
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).
  https://github.com/jfjelstul/worldcup
- Planilhas `WorldCups.csv`, `WorldCupMatches.csv` e `WorldCupPlayers.csv` publicadas por Andre Becklas (CC0), de
  1930 a 2014. Público, intervalo, assistentes e a ficha de 1930 a 1966.
- Wyscout, Copa de 2018 inteira: passes, chutes, duelos, faltas e tiros livres. Pappalardo et al., licença
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- StatsBomb Open Data: a Copa de 2022 inteira e 19 partidas mais antigas, com os mesmos tipos de lance.

Como em todo dado que chega de fora, os arquivos do fornecedor não vêm perfeitos. Fique de olho.

Não mude os nomes nem a estrutura das pastas: os notebooks leem os arquivos por esses caminhos.
