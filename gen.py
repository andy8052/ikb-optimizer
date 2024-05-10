from pydfs_lineup_optimizer import LineupOptimizer, AfterEachExposureStrategy
from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.sites.draftkings.classic.importer import DraftKingsCSVImporter
import csv

# don't change this stuff
class CustomSettings(BaseSettings):
    site = 'IKB'
    sport = 'NBA'
    budget = 50000  # budget you want to use
    max_from_one_team = None  # if needed
    min_teams = 2  # if needed
    min_games = None  # if needed
    csv_importer = DraftKingsCSVImporter  # If player will be imported using load_players_from_csv method
    positions = [
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'PF', 'SF', 'C'))
    ]

optimizer = LineupOptimizer(CustomSettings)
optimizer.load_players_from_csv("players.csv")

# this sets the number of repeating players from the previous lineup
optimizer.set_max_repeating_players(5)

# change number here to set the number of teams you require
optimizer.set_total_teams(min_teams=3)

# copy the below line and add a player to set custom players to remove
# optimizer.player_pool.remove_player('Jarrett Allen')

# below lets you set custom min and max exposure for a given player
# player = optimizer.player_pool.get_player_by_name('Tom Brady')
# player.max_exposure = 0.5  # set 50% max exposure
# player.min_exposure = 0.3  # set 30% min exposure

fields = ["player_1","player_2","player_3","player_4","player_5","player_6","player_7"]

with open("results.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    # change N to be number of teams
    # change max_exposure for max exposure generally for any player
    for lineup in optimizer.optimize(n=30, max_exposure=0.5):
        row = [lineup.players[0].id, lineup.players[1].id, lineup.players[2].id, lineup.players[3].id, lineup.players[4].id, lineup.players[5].id, lineup.players[6].id]
        
        writer.writerow(row)
        print(lineup)
        print(lineup.players)  # list of players
        print(lineup.fantasy_points_projection)
        print(lineup.salary_costs)
        