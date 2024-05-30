import pandas as pd
import numpy as np

pre_data = pd.read_excel('player_victory_output.xlsx')
mask_data = (pre_data['%_win'] != 'Less than 10 matches played') 
data = pre_data.loc[mask_data]
data.reset_index(inplace=True)

N = len(data)
col = ['email','team_id','se_stat','state_stat','sport']
res = pd.DataFrame(columns=col)
res['email'] = data['profile_email']

for i in range(N):
    num_matches = data['num_matches'][i]
    team_sport = data['team.sport_name'][i]
    mask_sport = (data['team.sport_name']==team_sport) 
    data_sport= data.loc[mask_sport]
    num_profiles_above = len(data_sport[data_sport['num_matches'] > num_matches])
    res['se_stat'][i] = round((num_profiles_above + 1)/len(data_sport),3)*100
    res['sport'][i] = team_sport
    if data['club_state'][i] != '-':
        club_state = data['club_state'][i]
        mask_state = (data['club_state']==club_state) & (data['team.sport_name']==team_sport)
        data_state= data.loc[mask_state]
        num_profiles_above = len(data_state[data_state['num_matches'] > num_matches])
        res['state_stat'][i] = round((num_profiles_above + 1)/len(data_state),3)*100

        
res.to_excel('profiles_global_stat.xlsx')

        
    

