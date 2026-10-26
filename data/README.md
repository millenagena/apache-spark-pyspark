# Dados do projeto

Os dados que o fornecedor mandou para a Arena Analytics. Tema: Copa do Mundo masculina de futebol, de 1930 a 2026.

| Pasta | O que tem |
|---|---|
| `raw/` | o histórico: 22 Copas, de 1930 a 2022, em três arquivos CSV (edições, partidas e escalações) |
| `events/` | o feed de eventos do histórico: os lances das partidas, em Parquet |
| `raw_2026/` | a Copa de 2026, nos mesmos três arquivos CSV do histórico |
| `raw_2026_correcao/` | o lote de correção de 2026: as 4 partidas decididas nos pênaltis, com o placar do jogo |
| `events_2026/` | o feed de eventos de 2026, em Parquet |

## O que tem em cada arquivo

### `raw/WorldCups.csv`: as edições

Cada linha é uma Copa.

| Coluna | O que é |
|---|---|
| `Year` | o ano da Copa |
| `Country` | o país-sede (em 2002, `Japan / South Korea`) |
| `Winner`, `Runners-Up`, `Third`, `Fourth` | campeão, vice, terceiro e quarto colocados |
| `GoalsScored` | total de gols da Copa, sem os gols de disputa de pênaltis |
| `QualifiedTeams` | quantas seleções jogaram |
| `MatchesPlayed` | quantas partidas teve |
| `Attendance` | público total, com vírgula de milhar (`590,549`). Vazio em 2018 e 2022 |

### `raw/WorldCupMatches.csv`: as partidas

Cada linha é uma partida.

| Coluna | O que é |
|---|---|
| `Year`, `RoundID` | o ano da Copa |
| `MatchID` | o código da partida, a chave que liga as partidas às escalações e ao feed de eventos |
| `Datetime` | data e hora, no formato `13 Jul 1930 - 15:00` |
| `Stage` | a fase: grupos, oitavas, quartas, semifinal, disputa de terceiro lugar e final |
| `Stadium`, `City` | estádio e cidade |
| `Home Team Name`, `Away Team Name` | as duas seleções. `Home` é o mandante definido pela organização, mesmo em campo neutro |
| `Home Team Initials`, `Away Team Initials` | a sigla de cada seleção, no código ISO de três letras (`DEU`, `ENG`, `NLD`) |
| `Home Team Goals`, `Away Team Goals` | o placar no fim do jogo, com a prorrogação quando houve |
| `Half-time Home Goals`, `Half-time Away Goals` | o placar do intervalo |
| `Win conditions` | `EXTRA_TIME` quando o jogo foi para a prorrogação, `PENALTY_SHOOTOUT` quando foi decidido nos pênaltis; vazio nos outros jogos |
| `Attendance` | público da partida, com vírgula de milhar (`4,444`) |
| `Referee`, `Assistant 1`, `Assistant 2` | árbitro e assistentes |

O placar não inclui os gols da disputa de pênaltis: a final de 2022 fica Argentina 3x3 France, com `Win conditions` =
`PENALTY_SHOOTOUT`. Público, intervalo e assistentes vêm das planilhas de 1930 a 2014; em 2018 e 2022 ficam vazios.

### `raw/WorldCupPlayers.csv`: as escalações

Cada linha é um jogador numa partida.

| Coluna | O que é |
|---|---|
| `RoundID`, `MatchID` | o ano da Copa e a partida |
| `Team Initials` | a sigla da seleção do jogador, a mesma das partidas |
| `Coach Name` | o técnico da seleção |
| `Line-up` | `S` para quem começou jogando; `N` para quem entrou durante o jogo (de 1930 a 1966, para os reservas) |
| `Shirt Number`, `Player Name`, `Position` | número da camisa, nome e posição (`goal keeper`, `defender`, `midfielder`, `forward`...), nem sempre preenchidos |
| `Event` | gols e cartões do jogador naquela partida, com o minuto: `G19'` (gol), `OG40'` (gol contra), `P42'` (gol de pênalti), `YC70'` (amarelo), `RC88'` (vermelho) |

De 1970 a 2022, aparece só quem jogou. De 1930 a 1966, a lista é a das planilhas antigas, com titulares e reservas.
A coluna `Event` usa também os códigos dessas planilhas (`Y` e `R` para os cartões).

### `events/`: o feed de eventos

Um arquivo Parquet. Cada linha é um lance de uma partida.

| Coluna | O que é |
|---|---|
| `event_id` | o código do lance |
| `MatchID` | a partida, o mesmo código de `WorldCupMatches.csv` |
| `period` | `1H` (primeiro tempo), `2H` (segundo tempo), `ET` (prorrogação) ou `PSO` (disputa de pênaltis) |
| `minute` | o minuto do lance |
| `event_type` | o tipo do lance: `Goal`, `Shootout goal`, `Yellow card`, `Second yellow`, `Red card`, `Substitution`, `Pass`, `Shot`, `Duel`, `Foul` e `Free kick` |
| `team` | o nome da seleção, como em `Home Team Name` e `Away Team Name` |
| `player_id` | o código do jogador, quando o lance tem um jogador |

Gols, cartões e substituições estão em todas as partidas. Passes, chutes, duelos, faltas e tiros livres estão em todas
as partidas de 2018 e 2022 e em 19 partidas mais antigas (1958, 1962, 1970, 1974, 1986 e 1990). A soma dos lances
`Goal` de cada partida é o placar do CSV; os gols da disputa de pênaltis são `Shootout goal`.

### `raw_2026/`: a Copa de 2026

Os mesmos três arquivos e as mesmas colunas do histórico, com 104 partidas. Diferenças em relação a `raw/`:

- nas partidas decididas nos pênaltis, o placar inclui os gols da disputa, porque é assim que a fonte
  (football-data.org) registra o placar final. Exemplo: Germany 4x5 Paraguay foi 1x1 no jogo e 3x4 nos pênaltis;
- a sigla da seleção é a da FIFA (`GER`, `NED`, `POR`), e não o código ISO;
- em `WorldCupPlayers.csv`, cada partida traz a lista de inscritos de cada seleção, com a posição por extenso
  (`Goalkeeper`, `Defence`, `Midfield`, `Offence`).

### `raw_2026_correcao/`: o lote de correção de 2026

Só o `WorldCupMatches.csv`, com as mesmas colunas, e só as 4 partidas de 2026 decididas nos pênaltis
(`PENALTY_SHOOTOUT`). O placar é o do jogo, sem os gols da disputa, como no histórico: Germany 1x1 Paraguay,
Netherlands 1x1 Morocco, Australia 1x1 Egypt e Switzerland 0x0 Colombia. As outras colunas são as mesmas de
`raw_2026/`. Com a correção, 2026 fica com 308 gols.

### `events_2026/`: o feed de eventos de 2026

Simulado para o curso a partir de `raw_2026/`, com as mesmas colunas do feed do histórico. Aqui `period` é um número
(1 ou 2), `team` é a sigla da seleção e `player_id` é um código gerado.

## Fontes e licenças

Os arquivos do histórico juntam várias fontes, unidas pela data e pelas duas seleções:

- Fjelstul World Cup Database, de Joshua C. Fjelstul, Ph.D. Partidas, placares, escalações desde 1970, gols, cartões
  e substituições, de 1930 a 2022. © 2023 Joshua C. Fjelstul, Ph.D. Licença
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).
  https://github.com/jfjelstul/worldcup
- Planilhas `WorldCups.csv`, `WorldCupMatches.csv` e `WorldCupPlayers.csv` publicadas por Andre Becklas no Kaggle
  (conjunto "FIFA World Cup", CC0), de 1930 a 2014. Público, intervalo, assistentes e a ficha de 1930 a 1966.
- Wyscout, Copa de 2018 inteira: passes, chutes, duelos, faltas e tiros livres. Pappalardo et al. (2019), "A public
  data set of spatio-temporal match events in soccer competitions", Scientific Data. Licença
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- StatsBomb Open Data: a Copa de 2022 inteira e 19 partidas mais antigas, com os mesmos tipos de lance. Fonte dos
  dados: StatsBomb. Uso sujeito ao acordo de uso do StatsBomb Open Data (`LICENSE.pdf` do repositório), que pede para
  citar a StatsBomb como fonte e usar o logo dela ao publicar análises feitas com esses dados.
  https://github.com/statsbomb/open-data
- Football-data.org: a Copa de 2026 em `raw_2026/`. https://www.football-data.org

Os arquivos de `raw/` e `events/` foram montados a partir dessas fontes, com mudanças de formato para o curso. Como
incluem dados do Fjelstul World Cup Database, eles são distribuídos sob a mesma licença,
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

Como em todo dado que chega de fora, os arquivos do fornecedor não vêm perfeitos. Fique de olho.

Não mude os nomes nem a estrutura das pastas: os notebooks leem os arquivos por esses caminhos.
