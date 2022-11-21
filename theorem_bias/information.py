import csv
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
theorems = df['theorem']
decision = df['decisions']
gender=df['gender']

binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}

def genderBias():
    fem=0
    femcount=0
    male=0
    malecount=0
    for idx, val in enumerate(theorems):
        if theorems[idx]!='pdf miss':
            if gender[idx].split(';')[0]=='f':
                femcount+=1
                if theorems[idx]=='y': fem+=1
            elif gender[idx].split(';')[0]=='m':
                malecount+=1
                if theorems[idx]=='y': male+=1
    
    print(fem/femcount)
    print(male/malecount)
    print(fem, femcount, male, malecount)

def getStats():
    names = ['Has Theorem ', 'No Theorem ']
    arr=[[],[]]
    mean_values=[0,0]
    std_values=[0,0]

    for index, value in enumerate(titles):
        if (theorems[index]!='pdf miss'):
            if (theorems[index]=='y'):
                arr[0].append(getMeanScore(scores[index].split(';')))
            elif (theorems[index]=='n'):
                arr[1].append(getMeanScore(scores[index].split(';')))
            else:
                print(value)
    
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

def acceptanceRate():
    names = ['Has Theorem', 'No Theorem']
    arr=[0,0]
    arr2=[0,0]

    for idx, val in enumerate(titles):
        if theorems[idx]!='pdf miss':
            if theorems[idx]=='y':
                arr[0]+=1
                if binary_decisions[decision[idx]]==1: arr2[0]+=1
            elif theorems[idx]=='n':
                arr[1]+=1
                if binary_decisions[decision[idx]]==1: arr2[1]+=1
            else:
                print(val)
    
    for i in range(0, len(arr2)):
        arr2[i]=arr2[i]/arr[i]
    
    df = pd.DataFrame()
    df['theorem indicator'] = names
    df['acceptance rate'] = arr2

    ax = sns.barplot(x='theorem indicator', y='acceptance rate', data = df).set_title("Acceptance Rate on Theorems")
    plt.tight_layout()
    plt.savefig('acceptance rate for theorem.png')


def histograms():
    names = ['Has Theorem ', 'No Theorem ']
    arr=[[],[]]

    for index, value in enumerate(titles):
        if (theorems[index]!='pdf miss'):
            if (theorems[index]=='y'):
                for elem in scores[index].split(';'):
                    arr[0].append(int(elem))
            elif (theorems[index]=='n'):
                for elem in scores[index].split(';'):
                    arr[1].append(int(elem))
            else:
                print(value)
    for i in range(len(names)):
        for idx in range (len(arr[i])):
            arr[i][idx] = int(arr[i][idx])
        arr[i].sort()

    print(sum(arr[1])/len(arr[1]))
    print(sum(arr[0])/len(arr[0]))

    df = pd.DataFrame()
    score = []
    hue = []
    for elem in arr[1]:
        score.append(elem)
        hue.append('Not Theorem')
    for elem in arr[0]:
        score.append(elem)
        hue.append('Theorem')

    df['Score'] = score
    df['Legend'] = hue

    sns.set_theme()
    sns.set_context("paper", rc={"font.size":18,"axes.titlesize":18,"axes.labelsize":18})  
    sns.set_style(style='white')
    sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})
    sns.displot(df, x='Score',bins=10,binwidth=1,hue='Legend',stat="density",common_norm=False).set(title='Score Distribtion Theorem vs Non-Theorem')
        # sns.set_title(names[i] + " Score Distribution", fontsize=50)
    # plt.xlabel('Scores', fontsize=18)
    # plt.ylabel('Distribution', fontsize=18)
    plt.tight_layout()
    plt.savefig('theorem_distribution.pdf')
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
    # acceptanceRate()
    histograms()
    #getStats()
    #genderBias()

if __name__ == "__main__":
    main()