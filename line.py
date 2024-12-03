# %%
from stats import whole_team, team_stats
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def pred_line(team_name, location):
    pstats = whole_team(team_name)
    tstats = team_stats(team_name, location)

    team_avg = tstats[0]
    team_l3 = tstats[1]
    team_location_avg = tstats[2]

    opp_avg_allowed = tstats[3]
    opp_l3_allowed = tstats[4]
    opp_location_avg = tstats[5]

    lines = {}

    for player in pstats:
        pct = pstats[player] / (team_avg + team_l3 + team_location_avg)
        lines[player] = float(pct * (opp_avg_allowed + opp_l3_allowed + opp_location_avg))

    return lines

pred_line('lakers', 'Home')
