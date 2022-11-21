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
titles = df['paper']
scores = df['ratings']
gender = df['gender']
year = df['year']
decision = df['decisions']

df_final = pd.read_csv("../dataset_final.csv")
gender_final = df_final['genders']
citations_final = df_final['authors_citations']

df_2021 = pd.read_csv("../openreview_2021.csv")
gender_2021 = df_2021['gender']
title_2021 = df_2021['paper']

author_data_2021 = pd.read_csv("../semanticScholar/authordata2021.csv")
author_stats_2021 = author_data_2021['author_stats']
paper_title_2021 = author_data_2021['paper_title']

binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}

def getStats():
    names = ['Male First', 'Male Last', 'Female First', 'Female Last']
    arr = [[],[],[],[]]
    mean_values=[0,0,0,0]
    std_values=[0,0,0,0]

    arr2=[[],[]]
    mean=[0,0]
    std=[0,0]

    for index, value in enumerate(titles):
        if year[index]==2021:
            gender_list = gender[index].split(';')[0]
            if gender_list =='m':arr2[0].append(getMeanScore(scores[index].split(';')))
            elif gender_list=='f':arr2[1].append(getMeanScore(scores[index].split(';')))
            #for g in gender_list:
            #    if g =='m': arr2[0].append(getMeanScore(scores[index].split(';')))
            #    elif g =='f': arr2[1].append(getMeanScore(scores[index].split(';')))

    for index, value in enumerate(titles):
        gender_list = gender[index].split(';')
        if year[index]==2020:
            if (gender_list[0]!='-1' and gender_list[0]!='u'):
                if (gender_list[0]=='m'):
                    arr[0].append(getMeanScore(scores[index].split(';')))
                elif (gender_list[0]=='f'):
                    arr[2].append(getMeanScore(scores[index].split(';')))
                else:
                    print(value)
            if (gender_list[-1]!='-1' and gender_list[-1]!='u'):
                if (gender_list[-1]=='m'):
                    arr[1].append(getMeanScore(scores[index].split(';')))
                elif (gender_list[-1]=='f'):
                        arr[3].append(getMeanScore(scores[index].split(';')))
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

    for index, array in enumerate(arr2):
        try:
            mean[index]=sum(array)/len(array)
        except:
            mean[index] = 0
        try:
            std[index] = st.stdev(array)
        except:
            std[index] = 0
    
    #print(mean_values)
    #print(std_values)
    print(mean)
    #print(arr2)
    print((mean[0])-(mean[1]))
    print(std)
    count1=0
    count2=0
    print(len(arr2[0]))
    print(len(arr2[1]))

def acceptanceRate():
    names = ['Male First', 'Male Last', 'Female First', 'Female Last']
    arr=[0,0,0,0]
    arr2=[0,0,0,0]

    for index, value in enumerate(titles):
        gender_list = gender[index].split(';')
        if (gender_list[0]!='-1' and gender_list[0]!='u'):
            if gender_list[0]=='m':
                arr[0]+=1
                if binary_decisions[decision[index]]==1: arr2[0]+=1
            elif gender_list[0]=='f':
                arr[2]+=1
                if binary_decisions[decision[index]]==1: arr2[2]+=1
            else: print(value)
        if (gender_list[-1]!='-1' and gender_list[-1]!='u'):
            if gender_list[-1]=='m':
                arr[1]+=1
                if binary_decisions[decision[index]]==1: arr2[1]+=1
            elif gender_list[-1]=='f':
                arr[3]+=1
                if binary_decisions[decision[index]]==1: arr2[3]+=1
            else: print(value)
    for i in range(0, len(arr2)):
        arr2[i]=arr2[i]/arr[i]
    
    df = pd.DataFrame()
    df['gender indicator'] = names
    df['acceptance rate'] = arr2

    ax = sns.barplot(x='gender indicator', y='acceptance rate', data = df).set_title('Acceptance Rate on Gender')
    plt.tight_layout()
    plt.savefig('acceptance rate for gender.png')

def histograms():
    names = ['Male First', 'Male Last', 'Female First', 'Female Last']
    arr = [[],[],[],[]]

    for index, value in enumerate(titles):
        gender_list = gender[index].split(';')
        if year[index] == 2021:
            if (gender_list[0]!='-1' and gender_list[0]!='u'):
                if (gender_list[0]=='m'):
                    for elem in scores[index].split(';'):
                        arr[0].append(elem)
                elif (gender_list[0]=='f'):
                    for elem in scores[index].split(';'):
                        arr[2].append(elem)
                else:
                    print(value)
            if (gender_list[-1]!='-1' and gender_list[-1]!='u'):
                if (gender_list[-1]=='m'):
                    for elem in scores[index].split(';'):
                        arr[1].append(elem)
                elif (gender_list[-1]=='f'):
                    for elem in scores[index].split(';'):
                        arr[3].append(elem)
                else:
                    print(value)
    for i in range (len(arr)):
        for idx in range (len(arr[i])):
            arr[i][idx] = int(arr[i][idx])
        arr[i].sort()


    print(sum(arr[0])/len(arr[0]))
    print(sum(arr[1])/len(arr[1]))
    print(sum(arr[2])/len(arr[2]))
    print(sum(arr[3])/len(arr[3]))
    plt.title('First Author Distribution', fontsize=22)
    sns.histplot(x=arr[0], kde=False,bins=10,binwidth=1,stat='density',label='male first').set(title='first author distribution')
    sns.histplot(x=arr[2], kde=False,bins=10,binwidth=1,stat='density',label='female first', color="red").set(title='first author distribution')
    plt.legend()
    plt.savefig('first_author_distribution.png')
    plt.clf()

    plt.title('Last Author Distribution', fontsize=22)
    sns.histplot(x=arr[1], kde=False,bins=10,binwidth=1,stat='density',label='male last').set(title='last author distribution')
    sns.histplot(x=arr[3], kde=False,bins=10,binwidth=1,stat='density',label='female last', color="red").set(title='last author distribution')
    plt.legend()
    plt.savefig('last_author_distribution.png')
    plt.clf()

def avgPublications(): 
    fem_first_count = 0
    fem_first_publications = 0
    fem_pub_array = []
    male_first_count = 0
    male_first_publications = 0
    male_pub_array=[]
    count=0
    idxes = []
    count2=0
    idxes2 = []

    for idx, val in enumerate(gender_final):
        gender_list = gender_final[idx].split(';')
        if gender_list[0]=='f':
            if int(df_final['authors_publications'][idx].split(';')[-1])!=-1:
                fem_first_count+=1
                fem_first_publications+=int(df_final['authors_publications'][idx].split(';')[-1])
                fem_pub_array.append(int(df_final['authors_publications'][idx].split(';')[-1]))
        elif gender_list[0]=='m':
            if int(df_final['authors_publications'][idx].split(';')[-1])!=-1:
                male_first_count+=1
                male_first_publications+=int(df_final['authors_publications'][idx].split(';')[-1])
                male_pub_array.append(int(df_final['authors_publications'][idx].split(';')[-1]))
    
    for idx, val in enumerate(title_2021):
        gender_list = gender_2021[idx].split(';')
        if gender_list[0]=='f':
            for idx2, val2 in enumerate(paper_title_2021):
                if editdistance.eval(val2, val)<=2:
                    try: 
                        if int(author_stats_2021[idx2].split('}, {')[-1].split(',')[0].split(':')[-1].replace('\'', ''))!=-1:
                            fem_first_count +=1
                            fem_first_publications+=int(author_stats_2021[idx2].split('}, {')[-1].split(',')[0].split(':')[-1].replace('\'', ''))
                            fem_pub_array.append(int(author_stats_2021[idx2].split('}, {')[-1].split(',')[0].split(':')[-1].replace('\'', '')))
                        break
                    except:
                        count+=1
                        idxes.append(idx2)
                        break
        elif gender_list[0]=='m':
            for idx2, val2 in enumerate(paper_title_2021):
                if editdistance.eval(val2, val)<=2:
                    try: 
                        if int(author_stats_2021[idx2].split('}, {')[-1].split(',')[0].split(':')[-1].replace('\'', ''))!=-1:
                            male_first_count +=1
                            male_first_publications+=int(author_stats_2021[idx2].split('}, {')[-1].split(',')[0].split(':')[-1].replace('\'', ''))
                            male_pub_array.append(int(author_stats_2021[idx2].split('}, {')[-1].split(',')[0].split(':')[-1].replace('\'', '')))
                            break
                    except:
                        count2+=1
                        idxes2.append(idx2)
                        break
            
    print('female invalid count', count)
    print('male invalid count', count2)
    print('avg num of publications for last authors with first fem authors:', fem_first_publications/fem_first_count)
    print('avg num of publications for last authors with first male authors:', male_first_publications/male_first_count)
    print('sd fem:', st.stdev(fem_pub_array))
    print('sd fem:', st.stdev(male_pub_array))
    print(len(fem_pub_array))
    print(len(male_pub_array))
    for idx in idxes:
        if author_stats_2021[idx]!='[]': print(author_stats_2021[idx])
    for idx in idxes2:
        if author_stats_2021[idx]!='[]': print(author_stats_2021[idx])

def highlyCitedLastAuthor():
    fem_first_count = 0
    fem_highly_cited=0
    male_first_count = 0
    male_highly_cited=0

    count=0
    idxes = []
    count2=0
    idxes2 = []
    
    for idx, val in enumerate(gender_final):
        gender_list = gender_final[idx].split(';')
        if gender_list[0]=='f':
            fem_first_count+=1
            if int(citations_final[idx].split(';')[-1])>=100: fem_highly_cited+=1
        elif gender_list[0]=='m':
            male_first_count+=1
            if int(citations_final[idx].split(';')[-1])>=100: male_highly_cited+=1
    
    for idx, val in enumerate(title_2021):
        gender_list = gender_2021[idx].split(';')
        if gender_list[0]=='f':
            
            for idx2, val2 in enumerate(paper_title_2021):
                if editdistance.eval(val2, val)<=2:
                    try: 
                        fem_first_count +=1
                        if int(author_stats_2021[idx2].split('}, {')[-1].split(',')[2].split(':')[-1].replace('\'', '')) >=100: 
                            fem_highly_cited+=1
                        break
                    except:
                        count+=1
                        idxes.append(idx2)
                        break
        elif gender_list[0]=='m':
            for idx2, val2 in enumerate(paper_title_2021):
                if editdistance.eval(val2, val)<=2:
                    try: 
                        male_first_count +=1
                        if int(author_stats_2021[idx2].split('}, {')[-1].split(',')[2].split(':')[-1].replace('\'', '')) >=100: 
                            male_highly_cited+=1
                        break
                    except:
                        count2+=1
                        idxes2.append(idx2)
                        break
    
    print('female invalid count', count)
    print('male invalid count', count2)
    print('percent of first author females with highly cited last authors: ',fem_highly_cited/fem_first_count)
    print('percent of first author males with highly cited last authors: ',male_highly_cited/male_first_count)
    print(fem_first_count)
    print(male_first_count)

    for idx in idxes:
        if author_stats_2021[idx]!='[]': print(author_stats_2021[idx])
    for idx in idxes2:
        if author_stats_2021[idx]!='[]': print(author_stats_2021[idx])

def getMeanScore(arr):
    total=0
    val=0
    for ele in arr:
        if isinstance(int(ele), int):
            total+=1
            val+=int(ele)
    return (val/total)

def main():
    #highlyCitedLastAuthor()
    #avgPublications()
    #acceptanceRate()
    #histograms()
    getStats()

if __name__ == "__main__":
    main()