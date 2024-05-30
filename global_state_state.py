import pandas as pd
import numpy as np

data = pd.read_excel('time_data.xlsx')
N = len(data)
col = ['email','se_stat','state_stat','sport']
res = pd.DataFrame(columns=col)
res['email'] = data['profile.email']

for i in range(N):
    num_events = data['team.num_events'][i]
    team_sport = data['sport_name'][i]
    mask_sport = (data['sport_name']==team_sport) 
    data_sport= data.loc[mask_sport]
    num_clubs_above = len(data_sport[data_sport['team.num_events'] > num_events])
    res['se_stat'][i] = round((num_clubs_above + 1)/len(data_sport),3)*100
    res['sport'][i] = team_sport
    if data['club_state'][i] != '-':
        club_state = data['club_state'][i]
        mask_state = (data['club_state']==club_state) & (data['sport_name']==team_sport) 
        data_state= data.loc[mask_state]
        num_clubs_above = len(data_state[data_state['team.num_events'] > num_events])
        res['state_stat'][i] = round((num_clubs_above + 1)/len(data_state),3)*100

        
res.to_excel('global_stat.xlsx')

        
    

