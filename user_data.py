import base64
import pickle
import pandas as pd
import numpy as np

data = pd.read_excel('user_data.xlsx')
N = len(data)
dict = {}
score_for = np.zeros(N)
my_list = [None for _ in range(N)]

for i in range(N):
    serialized_value = data['etosd_data'][i]
    dict[i] = pickle.loads(base64.b64decode(serialized_value.encode()))
    try:
        score_for[i] = dict[i]['{sport_name}_score_for']
        my_list[i] = dict[i]['match_outcome']
    except KeyError:
        pass

data['score_for'] = score_for
data['match_outcome'] = my_list


col = ['team_id','score_for','%_win','num_matches']
res = pd.DataFrame(columns=col)
list_team = np.unique(data['team_id'])
n_team = len(list_team)
res['team_id'] = list_team
    
for i in range(n_team):
    team_id = list_team[i]
    mask_team = (data['team_id']==team_id)
    data_team = data.loc[mask_team]
    res['score_for'][i] = sum(data_team['score_for'])
    res['num_matches'][i] = sum(data_team['match_outcome'] != None)
    res['%_win'][i] = round(sum(data_team['match_outcome']=='victory')/sum(data_team['match_outcome'] != None),2)*100

res.to_excel('team_score.xlsx')


    

