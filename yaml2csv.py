import os
import yaml
import pandas as pd

files = os.listdir('ipl_yaml')
files.remove('README.txt')
#print(files)
#print(files[0])
#op1 = open('Batsmen_vulnerability_to_bowler.txt','w')
#op2 = open('Bowler_vulnerability_to_batsmen.txt','w')

hit=[]
out=[]
'''
with open('ipl_yaml/501265.yaml','r') as f:
    try:
        main_dictionary=(yaml.load(f))
        innings=main_dictionary['innings']
        #print(innings,file=op)
        #print(innings[0].keys(),innings[1].keys())
        if(len(innings)>0):
            innings1=innings[0]['1st innings']
            innings1_deliveries=innings1['deliveries']
            for ball_info in innings1_deliveries:
                for delivery in ball_info:
                    values=[v for v in ball_info[delivery].values()]
                    if(len(values)==4):
                        hit.append([values[0],values[1],values[3]['total']])
                    elif(len(values)==5):
                        print('check1')
                        if(isinstance(values[2],str) and not('role' in values[3].keys())):
                            print('check2')
                        if('kind' in values[4].keys()):
                                if not(values[4]['kind']=='run out'):
                                    print('check3')
                                    out.append([values[0],values[1],values[4]['kind']])
                                    print(out)
        if(len(innings)==2):
            innings2=innings[1]['2nd innings']
            innings2_deliveries=innings2['deliveries']
            for ball_info in innings2_deliveries:
                for delivery in ball_info:
                    values=[v for v in ball_info[delivery].values()]
                    if(len(values)==4):
                        hit.append([values[0],values[1],values[3]['total']])
                    elif(len(values)==5):
                        print('check1')
                        if(isinstance(values[2],str) and not('role' in values[3].keys())):
                            print('check2')
                            if('kind' in values[4].keys()):
                                if not(values[4]['kind']=='run out'):
                                    print('check3')
                                    out.append([values[0],values[1],values[4]['kind']])
                                    print(out)
    except yaml.YAMLError as exc:
        print(exc)
'''

for file in files:
    print(file)
    with open('ipl_yaml/'+file,'r') as f:
        try:
            main_dictionary=(yaml.load(f))
            innings=main_dictionary['innings']
            #print(innings,file=op)
            #print(innings[0].keys(),innings[1].keys())
            if(len(innings)>0):
                innings1=innings[0]['1st innings']
                innings1_deliveries=innings1['deliveries']
                for ball_info in innings1_deliveries:
                    for delivery in ball_info:
                        values=[v for v in ball_info[delivery].values()]
                        if(len(values)==4):
                            hit.append([values[0],values[1],values[3]['total']])
                        elif(len(values)==5):
                            if(isinstance(values[2],str) and not('role' in values[3].keys())):
                                if('kind' in values[4].keys()):
                                    if not(values[4]['kind']=='run out'):
                                        out.append([values[0],values[1],values[4]['kind']])
            if(len(innings)==2):
                innings2=innings[1]['2nd innings']
                innings2_deliveries=innings2['deliveries']
                for ball_info in innings2_deliveries:
                    for delivery in ball_info:
                        values=[v for v in ball_info[delivery].values()]
                        if(len(values)==4):
                            hit.append([values[0],values[1],values[3]['total']])
                        elif(len(values)==5):
                            if(isinstance(values[2],str) and not('role' in values[3].keys())):
                                if('kind' in values[4].keys()):
                                    if not(values[4]['kind']=='run out'):
                                        out.append([values[0],values[1],values[4]['kind']])
        except yaml.YAMLError as exc:
            print(exc)

#op1.close()
#op2.close()

Out = pd.DataFrame(out)
Out.to_csv('Batsmen_vulnerability_to_bowler.csv')
Hit = pd.DataFrame(hit)
Hit.to_csv('Bowler_vulnerability_to_batsmen.csv')