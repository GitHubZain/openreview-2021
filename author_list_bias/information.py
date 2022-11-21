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
authors = df['authors']
decision = df['decisions']
scores = df['ratings']
year = df['year']
gender = df['gender']

binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}

def genderBias():
    fem=0
    femcount=0
    male=0
    malecount=0
    for idx, val in enumerate(authors):
        if not(type(val)==float):
            if gender[idx].split(';')[0]=='f':
                fem+=len(val.split(';'))
                femcount+=1
            elif gender[idx].split(';')[0]=='m':
                male+=len(val.split(';'))
                malecount+=1

    print(fem/femcount)
    print(male/malecount)

def getStats():
    categories = ['1', '2','3','4','5','6','7','8+']
    arr = [[],[],[],[],[],[],[],[]]
    mean_values = [0,0,0,0,0,0,0,0]
    std_values = [0,0,0,0,0,0,0,0]

    for idx, val in enumerate(authors):
        if not(type(val)==float):
            numAuthors = len(val.split(';'))
            if int(numAuthors)==1:
                arr[0].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)==2:
                arr[1].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)==3:
                arr[2].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)==4:
                arr[3].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)==5:
                arr[4].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)==6:
                arr[5].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)==7:
                arr[6].append(getMeanScore(scores[idx].split(';')))
            elif int(numAuthors)>=8:
                arr[7].append(getMeanScore(scores[idx].split(';')))
            else:
                print(numAuthors)
        else:
            print(val)

    for idx,array in enumerate(arr):
        try:
            mean_values[idx] = sum(array)/len(array)
        except:
            mean_values[idx] = 0
        try:
            std_values[idx] = st.stdev(array)
        except:
            std_values[idx] = 0

    df = pd.DataFrame()
    df['Author List Lenghts'] = categories
    df['Mean Reviewer Score'] = mean_values

    ax = sns.barplot(x='Author List Lenghts', y='Mean Reviewer Score', data=df)
    ax.set_title('Mean Reviewer Score for Each Author Category')
    plt.tight_layout()
    plt.savefig('mrs_author_distribution.png')
    plt.clf()
    print(mean_values)
    print(std_values)

def acceptanceRate():
    categories = ['1', '2','3','4','5','6','7','8+']
    arr = [0,0,0,0,0,0,0,0]
    arr2 = [0,0,0,0,0,0,0,0]

    for idx, val in enumerate(authors):
        if not(type(val)==float):
            numAuthors = len(val.split(';'))
            if int(numAuthors) == 1:
                arr[0]+=1
                if binary_decisions[decision[idx]]==1: arr2[0]+=1
            elif int(numAuthors) == 2:
                arr[1]+=1
                if binary_decisions[decision[idx]]==1: arr2[1]+=1
            elif int(numAuthors) == 3:
                arr[2]+=1
                if binary_decisions[decision[idx]]==1: arr2[2]+=1
            elif int(numAuthors) == 4:
                arr[3]+=1
                if binary_decisions[decision[idx]]==1: arr2[3]+=1
            elif int(numAuthors) == 5:
                arr[4]+=1
                if binary_decisions[decision[idx]]==1: arr2[4]+=1
            elif int(numAuthors) == 6:
                arr[5]+=1
                if binary_decisions[decision[idx]]==1: arr2[5]+=1
            elif int(numAuthors) == 7:
                arr[6]+=1
                if binary_decisions[decision[idx]]==1: arr2[6]+=1
            elif int(numAuthors) >=8:
                arr[7]+=1
                if binary_decisions[decision[idx]]==1: arr2[7]+=1
            else:
                print(numAuthors)

    for i in range(0, len(arr2)):
        arr2[i] = arr2[i]/arr[i]
    
    df = pd.DataFrame()
    df['number of authors'] = categories
    df['acceptance rate'] = arr2

    ax = sns.barplot(x='number of authors', y='acceptance rate', data = df).set(title = 'Acceptance Rate vs. Number of Authors')

    plt.tight_layout()
    plt.savefig("acceptance_rate_vs._number_of_authors.png")
    


def histograms():
    categories = ['1', '2','3','4','5','6','7','8+']
    arr = [[],[],[],[],[],[],[],[]]

    total=0

    for idx, val in enumerate(authors):
        if not(type(val)==float):
            numAuthors = len(val.split(';'))
            if int(numAuthors) == 1:
                for elem in scores[idx].split(';'):
                    arr[0].append(elem)
            elif int(numAuthors) == 2:
                for elem in scores[idx].split(';'):
                    arr[1].append(elem)
            elif int(numAuthors) == 3:
                for elem in scores[idx].split(';'):
                    arr[2].append(elem)
            elif int(numAuthors) == 4:
                for elem in scores[idx].split(';'):
                    arr[3].append(elem)
            elif int(numAuthors) == 5:
                for elem in scores[idx].split(';'):
                    arr[4].append(elem)
            elif int(numAuthors) == 6:
                for elem in scores[idx].split(';'):
                    arr[5].append(elem)
            elif int(numAuthors) == 7:
                for elem in scores[idx].split(';'):
                    arr[6].append(elem)
            elif int(numAuthors) >=8:
                for elem in scores[idx].split(';'):
                    arr[7].append(elem)
            else:
                print(numAuthors)

    for i in range(len(categories)):
        for idx in range (len(arr[i])):
            arr[i][idx] = int(arr[i][idx])
        arr[i].sort()
        plt.title(categories[i] + ' Author(s)', fontsize=22)
        sns.histplot(x=arr[i],binwidth=1,stat='density')
        plt.tight_layout()
        plt.savefig(categories[i] + '_author(s)_distribution.png')
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
    getStats()
    #acceptanceRate()
    #genderBias()

if __name__ == "__main__":
    main()