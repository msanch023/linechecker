# %%
import requests
import pandas as pd

def data(url):
    response = requests.get(url)
    response.raise_for_status()
    tables = pd.read_html(response.text)

    return tables[0]

def player_stats(player_name):

    urls = {
        'player_stats': 'https://www.teamrankings.com/nba/player/' + player_name
    }

    games_played = data(urls['player_stats'])

    player_games_played = games_played.loc[0]['G']
    player_total_points = games_played.loc[0]['PTS']

    return player_games_played, player_total_points


def team_stats(team_name, location='Home'):

    urls = {
        'team_points_per_game': 'https://www.teamrankings.com/nba/stat/points-per-game',
        'opponent_points_per_game': 'https://www.teamrankings.com/nba/stat/opponent-points-per-game'
    }

    team_ppg_df = data(urls['team_points_per_game'])
    opp_ppg_df = data(urls['opponent_points_per_game'])

    opp_location = 'Home'
    if location == 'Home':
        opp_location = 'Away'

    team_avg = team_ppg_df.loc[team_ppg_df['Team'] == team_name, '2024'].values[0]
    team_l3 = team_ppg_df.loc[team_ppg_df['Team'] == team_name, 'Last 3'].values[0]
    team_location_avg = team_ppg_df.loc[team_ppg_df['Team'] == team_name, location].values[0]
    opp_avg_allowed = opp_ppg_df.loc[opp_ppg_df['Team'] == team_name, '2024'].values[0]
    opp_l3_allowed = opp_ppg_df.loc[opp_ppg_df['Team'] == team_name, 'Last 3'].values[0]
    opp_location_avg = opp_ppg_df.loc[opp_ppg_df['Team'] == team_name, opp_location].values[0]

    return team_avg, team_l3, team_location_avg, opp_avg_allowed, opp_l3_allowed, opp_location_avg
