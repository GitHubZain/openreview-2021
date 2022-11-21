import csv
import pandas as pd
import numpy as np
import math
import sys
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt
import editdistance

df = pd.read_csv("../openreview.csv") 
region = df['regions']
coo = df['COO']
decision = df['decisions']
gender = df['gender']
binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}
mideast = ['bh', 'cy', 'eg','ir','iq','il','jo', 'kw','lb','om','ps','qa','sa','sy','tr','ae','ye']
eastasian = ['cn', 'jp', 'mn', 'kp','kr', 'tw', 'hk']
southasian = ['af','bd','bt', 'in', 'np', 'pk', 'lk','mv','sg']

def diff_acceptance_rate():
    names = ['US', 'Canada', 'South America', 'Australia and New Zealand', 'Mid East', 'UK/Ireland', 'mainland Europe', 'Russia', 'Africa', 'East Asian', 'South Asia']
    percent_arr=[0,0,0,0,0,0,0,0,0,0,0]
    malearr = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    femarr = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    def add_to_array(num, idx):
        if gender[idx].split(';')[-1]=='f':
            femarr[num][-1]+=1
            if binary_decisions[decision[idx]]==1:femarr[num][0]+=1
        elif gender[idx].split(';')[-1]=='m':
            malearr[num][-1]+=1
            if binary_decisions[decision[idx]]==1:malearr[num][0]+=1

    for idx, val in enumerate(region):
        if val != "NAN" and gender[idx].split(';')[-1]!='-1':
            if val =='usa': add_to_array(0,idx)
            elif coo[idx] in eastasian: add_to_array(9,idx)
            elif coo[idx] in southasian: add_to_array(10,idx)
            elif coo[idx] =='au' or coo[idx] == 'nz': add_to_array(3,idx)
            elif coo[idx] in mideast: add_to_array(4,idx)
            elif coo[idx] =='uk' or coo[idx] == 'ie': add_to_array(5,idx)
            elif coo[idx]=='russia': add_to_array(7,idx)
            elif val == 'canada': add_to_array(1,idx)
            elif val == 'southamerica':add_to_array(2,idx)
            elif val == 'europe': add_to_array(6,idx)
            elif val == 'africa': add_to_array(8,idx)
            else: print(coo[idx])

    print(malearr)
    print(femarr)

    for idx, val in enumerate(percent_arr):
        try: 
            male_temp=malearr[idx][0]/malearr[idx][-1]
            print(male_temp)
            fem_temp = femarr[idx][0]/femarr[idx][-1]
            print(fem_temp)
            percent_arr[idx] = male_temp-fem_temp
        except: 
            percent_arr[idx] = 0
    
    print(percent_arr)

    df = pd.DataFrame()
    df['Groups'] = names
    df['Difference in Acceptance Rate'] = percent_arr

    ax = sns.barplot(x='Groups', y='Difference in Acceptance Rate', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    ax.set_title('Difference in Gender Acceptance Rate per Country')
    plt.tight_layout()
    plt.savefig('difference in acceptance rate per country.png')

def main():
    diff_acceptance_rate()

if __name__ == "__main__":
    main()