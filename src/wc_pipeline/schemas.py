from pyspark.sql.types import IntegerType, StringType, StructField, StructType

WORLD_CUPS = StructType([
    StructField("Year", IntegerType(), True),
    StructField("Country", StringType(), True),
    StructField("Winner", StringType(), True),
    StructField("Runners-Up", StringType(), True),
    StructField("Third", StringType(), True),
    StructField("Fourth", StringType(), True),
    StructField("GoalsScored", IntegerType(), True),
    StructField("QualifiedTeams", IntegerType(), True),
    StructField("MatchesPlayed", IntegerType(), True),
    StructField("Attendance", StringType(), True),
])

MATCHES = StructType([
    StructField("Year", IntegerType(), True),
    StructField("Datetime", StringType(), True),
    StructField("Stage", StringType(), True),
    StructField("Stadium", StringType(), True),
    StructField("City", StringType(), True),
    StructField("Home Team Name", StringType(), True),
    StructField("Home Team Goals", IntegerType(), True),
    StructField("Away Team Goals", IntegerType(), True),
    StructField("Away Team Name", StringType(), True),
    StructField("Win conditions", StringType(), True),
    StructField("Attendance", StringType(), True),
    StructField("Half-time Home Goals", IntegerType(), True),
    StructField("Half-time Away Goals", IntegerType(), True),
    StructField("Referee", StringType(), True),
    StructField("Assistant 1", StringType(), True),
    StructField("Assistant 2", StringType(), True),
    StructField("RoundID", IntegerType(), True),
    StructField("MatchID", IntegerType(), True),
    StructField("Home Team Initials", StringType(), True),
    StructField("Away Team Initials", StringType(), True),
])

PLAYERS = StructType([
    StructField("RoundID", IntegerType(), True),
    StructField("MatchID", IntegerType(), True),
    StructField("Team Initials", StringType(), True),
    StructField("Coach Name", StringType(), True),
    StructField("Line-up", StringType(), True),
    StructField("Shirt Number", IntegerType(), True),
    StructField("Player Name", StringType(), True),
    StructField("Position", StringType(), True),
    StructField("Event", StringType(), True),
])
