import base64
import pickle
import pandas as pd
import numpy as np

data = pd.read_excel('player_victory.xlsx')
N = len(data)
dict = {}
my_list = [None for _ in range(N)]

for i in range(N):
    serialized_value = data['etosd.data'][i]
    dict[i] = pickle.loads(base64.b64decode(serialized_value.encode()))
    try:
        my_list[i] = dict[i]['match_outcome']
    except KeyError:
        pass

data['match_outcome'] = my_list


col = ['profile_email','team_id','%_win','num_matches','club_state']
res = pd.DataFrame(columns=col)
df_team = data[['profile.email', 'team.id','club_state','team.sport_name']].drop_duplicates()
df_team.reset_index(inplace=True)
n_team = len(df_team)
res[['profile_email','team_id','club_state','team.sport_name']] = df_team[['profile.email','team.id','club_state','team.sport_name']]


for i in range(n_team):
    profile_email = df_team['profile.email'][i]
    team_id = df_team['team.id'][i]
    mask_team = (data['team.id']==team_id) & (data['profile.email']==profile_email)
    data_team = data.loc[mask_team]
    res['num_matches'][i] = sum(data_team['match_outcome'] != None)
    if res['num_matches'][i] > 9:
        res['%_win'][i] = round(sum(data_team['match_outcome']=='victory')/sum(data_team['match_outcome'] != None),2)*100
    else:
        res['%_win'][i] = 'Less than 10 matches played'
            
res.to_excel('player_victory_output.xlsx')


    

