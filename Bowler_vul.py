import pandas as pd
import os
import time

start=time.time()
files = os.listdir('ipl_csv')
files.remove('README.txt')
#print(files)
colnames = ['ball','innings_number','over and ball','Batting Team Name','Batsman','non-striker','Bowler','runs-off bat','extras','kind_of_wicket','dismissed_player_name']
not_wanted = ['version','info']
Bowler_dict={}
for file in files:
    print(file)
    df = pd.read_csv('ipl_csv/'+file,names=colnames,header=None)
    df = df[~df['ball'].isin(not_wanted)]
    for index,row in df.iterrows():
        Batsman = row['Batsman'] 
        Bowler = row['Bowler'] 
        Runs = int(row['runs-off bat'])
        if Bowler in Bowler_dict:
            if Bowler in Bowler_dict[Bowler]:
                Bowler_dict[Bowler][Batsman]+=Runs
            else:
                Bowler_dict[Bowler][Batsman]=Runs
        else:
            Bowler_dict[Bowler]={}
            Bowler_dict[Bowler][Batsman]=Runs

Bowler_vul = []
for bowler in Bowler_dict:
    items = [(v,k) for k, v in Bowler_dict[bowler].items()]
    items.sort()
    items.reverse()
    items = [(k,v) for v, k in items]
    Bowler_vul.append((items[0][1],bowler+":"+items[0][0]))

Bowler_vul.sort()
Bowler_vul.reverse()
Most_vul = Bowler_vul[0]
print(Most_vul)
end=time.time()
print("The time taken to calculate the bowler most vulnerable",end-start)