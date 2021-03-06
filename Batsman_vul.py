import pandas as pd
import os
import time

start=time.time()
files = os.listdir('ipl_csv')
files.remove('README.txt')
colnames = ['ball','innings_number','over and ball','Batting Team Name','Batsman','non-striker','Bowler','runs-off bat','extras','kind_of_wicket','dismissed_player_name']
not_wanted = ['version','info']
wicket_type = ['caught','bowled','lbw','stumped','caught and bowled']
Batsman_vul_dict={}
for file in files:
    print(file)
    df = pd.read_csv('ipl_csv/'+file,names=colnames,header=None)
    df = df[~df['ball'].isin(not_wanted)]
    for index,row in df.iterrows():
        Batsman = row['Batsman'] 
        Bowler = row['Bowler'] 
        Wicket = row['kind_of_wicket']
        if Wicket in wicket_type:    
            if Batsman in Batsman_vul_dict:
                if Bowler in Batsman_vul_dict[Batsman]:
                    Batsman_vul_dict[Batsman][Bowler]+=1
                else:
                    Batsman_vul_dict[Batsman][Bowler]=1
            else:
                Batsman_vul_dict[Batsman]={}
                Batsman_vul_dict[Batsman][Bowler]=1

Batsman_vul = []
for batsman in Batsman_vul_dict:
    items = [(v,k) for k, v in Batsman_vul_dict[batsman].items()]
    items.sort()
    items.reverse()
    items = [(k,v) for v, k in items]
    Batsman_vul.append((items[0][1],batsman+":"+items[0][0]))

Batsman_vul.sort()
Batsman_vul.reverse()
Most_vul = Batsman_vul[0]
print(Most_vul)
end=time.time()
print("The time taken to calculate the batsman most vulnerable",end-start)
