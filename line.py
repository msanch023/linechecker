# %%
from stats import player_stats, team_stats

def pred_line(player_name, team_name):
    pstats = player_stats(player_name)
    tstats = team_stats(team_name)

    avg_pts = pstats[1]/pstats[0]

    team_avg = tstats[0]
    team_l3 = tstats[1]
    team_location_avg = tstats[2]

    opp_avg_allowed = tstats[3]
    opp_l3_allowed = tstats[4]
    opp_location_avg = tstats[5]

    pct = avg_pts / (team_avg + team_l3 + team_location_avg)

    line = pct * (opp_avg_allowed + opp_l3_allowed + opp_location_avg)

    return line
