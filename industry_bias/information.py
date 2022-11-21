import csv
from os import stat
import pandas as pd
import numpy as np
import math
import sys
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../openreview.csv") 
titles = df['paper']
scores = df['ratings']
institution = df['institution']
year = df['year']
decision = df['decisions']
gender=df['gender']

binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}

def gender_bias():
    g=0
    gnot=0
    m=0
    mnot=0
    f=0
    fnot=0
    other =0
    othernot=0

    for idx, val in enumerate(institution):
        if (year[idx])==2021:
            if ('Google' in val.split(';')[0] or 'DeepMind' in val.split(';')[0] or 'Deep Mind' in val.split(';')[0]):
                gnot+=1
                if gender[idx].split(';')[0]=='f': g+=1
            elif 'Microsoft' in val.split(';')[-1]:
                mnot+=1
                if gender[idx].split(';')[0]=='f': m+=1
            elif 'Facebook' in val.split(';')[-1]:
                fnot+=1
                if gender[idx].split(';')[0]=='f': f+=1
            else:
                othernot+=1
                if gender[idx].split(';')[0]=='f': other+=1
    print(g/gnot)
    print(m/mnot)
    print(f/fnot)
    print((g+m+f)/(gnot+mnot+fnot))
    print(other/othernot)

def acceptance():
    g=0
    gcount=0
    f=0
    fcount=0
    m=0
    mcount=0

    for idx, val in enumerate(institution):
        if (year[idx]==2021):
            if 'Google' in val.split(';')[-1] or 'DeepMind' in val.split(';')[-1] or 'Deep Mind' in val.split(';')[-1]:
                g+=1
                if binary_decisions[decision[idx]]==1: gcount+=1
            elif 'Microsoft' in val.split(';')[-1]:
                m+=1
                if binary_decisions[decision[idx]]==1: mcount+=1
            elif 'Facebook' in val.split(';')[-1]:
                f+=1
                if binary_decisions[decision[idx]]==1: fcount+=1

    print(gcount/g)
    print(mcount/m)
    print(fcount/f)

    print(g, gcount, m, mcount, f, fcount)

def getStats():
    names = ['Google', 'Microsoft', 'Facebook']
    arr = [[],[],[]]
    mean_values=[0,0,0]
    std_values=[0,0,0]

    for index, value in enumerate(institution):
        if (year[index]==2021):
            for inst in value.split(';'):
                if 'Google' in inst or 'DeepMind' in inst or 'Deep Mind' in inst:
                    arr[0].append(getMeanScore(scores[index].split(';')))
                elif 'Microsoft' in inst:
                    arr[1].append(getMeanScore(scores[index].split(';')))
                elif 'Facebook' in inst:
                    arr[2].append(getMeanScore(scores[index].split(';')))
    
    for index, array in enumerate(arr):
        try:
            mean_values[index]=sum(array)/len(array)
        except:
            mean_values[index] = 0
        try:
            std_values[index] = st.stdev(array)
        except:
            std_values[index] = 0
    
    print(mean_values)
    print(std_values)

def acceptanceRate(author):
    if author: 
        idx=0
        title = 'acceptance rate of industry (first author).png'
        title2 = 'Acceptance Rate per Industry (first author)'
    else: 
        idx=-1
        title = 'acceptance rate of industry (last author).png'
        title2 = 'Acceptance Rate per Industry (last author)'
    
    names = ['Google', 'Microsoft', 'Facebook', 'Google', 'Microsoft', 'Facebook']
    years = ['2020', '2020', '2020', '2021', '2021', '2021']
    arr=[0,0,0,0,0,0]
    arr2=[0,0,0,0,0,0]


    for index, value in enumerate(institution):
        if (year[index]!=2021):
            if institution[index][idx]!='':
                if 'Google' in value.split(';')[idx] or 'DeepMind' in value.split(';')[idx] or 'Deep Mind' in value.split(';')[idx]:
                    arr[0]+=1
                    if binary_decisions[decision[index]]==1:
                        arr2[0]+=1
                elif 'Microsoft' in value.split(';')[idx]:
                    arr[1]+=1
                    if binary_decisions[decision[index]]==1:
                        arr2[1]+=1
                elif 'Facebook' in value.split(';')[idx]:
                    arr[2]+=1
                    if binary_decisions[decision[index]]==1:
                        arr2[2]+=1
        if institution[index][idx]!='':
            if 'Google' in value.split(';')[idx] or 'DeepMind' in value.split(';')[idx] or 'Deep Mind' in value.split(';')[idx]:
                arr[3]+=1
                if binary_decisions[decision[index]]==1:
                    arr2[3]+=1
            elif 'Microsoft' in value.split(';')[idx]:
                arr[4]+=1
                if binary_decisions[decision[index]]==1:
                    arr2[4]+=1
            elif 'Facebook' in value.split(';')[idx]:
                arr[5]+=1
                if binary_decisions[decision[index]]==1:
                    arr2[5]+=1
    
    for i in range(len(arr2)):
        arr2[i]= arr2[i]/arr[i]
    
    df = pd.DataFrame()
    df['industry'] = names
    df['year'] = years
    df['acceptance rate'] = arr2

    ax = sns.barplot(x='industry', y='acceptance rate', hue='year', data = df).set(title=title2)
    
    plt.tight_layout()
    plt.savefig(title)

def histograms():
    arr=[[],[],[],[],[],[]]

    for index, value in enumerate(institution):
        if 'Google' in value.split(';')[0] or 'DeepMind' in value.split(';')[0] or 'Deep Mind' in value.split(';')[0]:
            for elem in scores[index].split(';'):
                arr[0].append(int(elem))
        elif 'Microsoft' in value.split(';')[0]:
            for elem in scores[index].split(';'):
                arr[1].append(int(elem))
        elif 'Facebook' in value.split(';')[0]:
            for elem in scores[index].split(';'):
                arr[2].append(int(elem))
        if 'Google' in value.split(';')[-1] or 'DeepMind' in value.split(';')[-1]or 'Deep Mind' in value.split(';')[-1]:
            for elem in scores[index].split(';'):
                arr[3].append(int(elem))
        elif 'Microsoft' in value.split(';')[-1]:
            for elem in scores[index].split(';'):
                arr[4].append(int(elem))
        elif 'Facebook' in value.split(';')[-1]:
            for elem in scores[index].split(';'):
                arr[5].append(int(elem))
    
    plt.title('Google Distribution', fontsize=22)
    sns.histplot(x=arr[0], kde=False,bins=10,binwidth=1,stat='density',label='first author').set(title='google distribution')
    sns.histplot(x=arr[3], kde=False,bins=10,binwidth=1,stat='density',label='last author', color="red").set(title='google distribution')
    plt.legend()
    plt.savefig('google_distribution.png')
    plt.clf()

    plt.title('Microsoft Distribution', fontsize=22)
    sns.histplot(x=arr[1], kde=False,bins=10,binwidth=1,stat='density',label='first author').set(title='microsoft distribution')
    sns.histplot(x=arr[4], kde=False,bins=10,binwidth=1,stat='density',label='last author', color="red").set(title='microsoft distribution')
    plt.legend()
    plt.savefig('microsoft_distribution.png')
    plt.clf()

    plt.title('Facebook Distribution', fontsize=22)
    sns.histplot(x=arr[2], kde=False,bins=10,binwidth=1,stat='density',label='first author').set(title='facebook distribution')
    sns.histplot(x=arr[5], kde=False,bins=10,binwidth=1,stat='density',label='last author', color="red").set(title='facebook distribution')
    plt.legend()
    plt.savefig('facebook_distribution.png')
    plt.clf()

def getMeanScore(arr):
    total=0
    val=0
    for ele in arr:
        if isinstance(int(ele), int):
            total+=1
            val+=int(ele)
    return (val/total)

def main():
    #histograms()
    #getStats()
    #acceptanceRate(True)
    #acceptance()
    gender_bias()

if __name__ == "__main__":
    main()