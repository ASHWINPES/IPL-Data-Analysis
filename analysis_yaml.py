#import pandas as pd
#df = pd.read_csv("C:/Users/HP PC/Desktop/BD_2018/Batsmen_vulnerability_to_bowler.csv")
'''
import yaml

with open("C:/Users/HP PC/Batsman_vul_data.yaml", 'r') as stream:
    try:
        batsman_dict = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
Batsman_vul = []
for batsman in batsman_dict:
    items = [(v,k) for k, v in batsman_dict[batsman].items()]
    items.sort()
    items.reverse()
    items = [(k,v) for v, k in items]
    Batsman_vul.append((items[0][1],batsman+":"+items[0][0]))

Batsman_vul.sort()
Batsman_vul.reverse()
Most_vul = Batsman_vul[0]
print(Most_vul)
'''

#import pandas as pd
#df = pd.read_csv("C:/Users/HP PC/Desktop/BD_2018/Batsmen_vulnerability_to_bowler.csv")

import yaml

with open("C:/Users/HP PC/Bowler_vul_data.yml", 'r') as stream:
    try:
        batsman_dict = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
Batsman_vul = []
for batsman in batsman_dict:
    items = [(v,k) for k, v in batsman_dict[batsman].items()]
    items.sort()
    items.reverse()
    items = [(k,v) for v, k in items]
    Batsman_vul.append((items[0][1],batsman+":"+items[0][0]))

Batsman_vul.sort()
Batsman_vul.reverse()
Most_vul = Batsman_vul[0]
print(Most_vul)
