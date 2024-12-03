# %%
import requests
import pandas as pd

def data(url):
    response = requests.get(url)
    response.raise_for_status()
    tables = pd.read_html(response.text)

    return tables[0]

# %%
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

    team_avg = team_ppg_df.loc[team_ppg_df['Team'].str.contains(team_name, case=False), '2024'].values[0]
    team_l3 = team_ppg_df.loc[team_ppg_df['Team'].str.contains(team_name, case=False), 'Last 3'].values[0]
    team_location_avg = team_ppg_df.loc[team_ppg_df['Team'].str.contains(team_name, case=False), location].values[0]
    opp_avg_allowed = opp_ppg_df.loc[opp_ppg_df['Team'].str.contains(team_name, case=False), '2024'].values[0]
    opp_l3_allowed = opp_ppg_df.loc[opp_ppg_df['Team'].str.contains(team_name, case=False), 'Last 3'].values[0]
    opp_location_avg = opp_ppg_df.loc[opp_ppg_df['Team'].str.contains(team_name, case=False), opp_location].values[0]

    return team_avg, team_l3, team_location_avg, opp_avg_allowed, opp_l3_allowed, opp_location_avg

# %%
def whole_team(team_name):
    url = 'https://www.teamrankings.com/nba/player-stat/points'
    df = data(url)
    team_data = df[df['Team'].str.contains(team_name, case=False)].values

    lines = {}

    for player in team_data:
        lines[player[1]] = player[4]

    return lines
