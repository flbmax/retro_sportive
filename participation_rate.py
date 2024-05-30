import pandas as pd
import numpy as np

data = pd.read_excel('participation_rate.xlsx')
col = ['team_id','team_mean_grade','max_participation','first_name_max_participation','last_name_max_participation','max_participation_2','first_name_max_participation_2','last_name_max_participation_2','max_participation_3','first_name_max_participation_3','last_name_max_participation_3']
res = pd.DataFrame(columns=col)
res['team_id'] = np.unique(data['team.id'])
N=len(res)

for i in range(N):
    team_id=res['team_id'][i]
    mask_team=(data['team.id']==team_id)
    data_team=data.loc[mask_team]
    
    index_1 = data_team['participation_rate'].nlargest(1).index[-1]
    index_2 = data_team['participation_rate'].nlargest(2).index[-1]
    index_3 = data_team['participation_rate'].nlargest(3).index[-1]
    
    res['max_participation'][i]=round(data_team['participation_rate'][index_1],2)*100
    res['first_name_max_participation'][i]=data_team['profile.first_name'][index_1]
    res['last_name_max_participation'][i]=data_team['profile.last_name'][index_1]

    
    res['max_participation_2'][i]=round(data_team['participation_rate'][index_2],2)*100
    res['first_name_max_participation_2'][i]=data_team['profile.first_name'][index_2]
    res['last_name_max_participation_2'][i]=data_team['profile.last_name'][index_2]

    
    res['max_participation_3'][i]=round(data_team['participation_rate'][index_3],2)*100
    res['first_name_max_participation_3'][i]=data_team['profile.first_name'][index_3]
    res['last_name_max_participation_3'][i]=data_team['profile.last_name'][index_3]

    res['team_mean_grade'][i]=round(np.mean(list(filter(lambda val: val != '-', data_team['mean_grade']))),1)
    
res.to_excel('team_participation_rate.xlsx')


