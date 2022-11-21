import csv
import pandas as pd
import numpy as np
import math
import sys
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt
import time

df = pd.read_csv("../openreview.csv") 
gender = df['gender']
schools = df['institution']
decision = df['decisions']
regions = df['regions']
scores = df['ratings']
year = df['year']
COO = df['COO']

binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}

#Afghanistan, Bangladesh, Bhutan, India, Nepal, Pakistan, Sri Lanka and the Maldives
#China, Japan, Mongolia, North Korea, South Korea, and Taiwan
#Bahrain, Cyprus, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Palestine, Qatar, Saudi Arabia, the Syrian Arab Republic, Turkey, the United Arab Emirates and Yemen.
#US, Canada, South America, Australia, Mid East, UK/Ireland, mainland Europe, Russian Block, Africa, East Asian, South Asia.
#Singapore, New Zealand 
mideast = ['bh', 'cy', 'eg','ir','iq','il','jo', 'kw','lb','om','ps','qa','sa','sy','tr','ae','ye']
eastasian = ['cn', 'jp', 'mn', 'kp','kr', 'tw', 'hk']
southasian = ['af','bd','bt', 'in', 'np', 'pk', 'lk','mv','sg']

names = ['US', 'Canada', 'South America', 'Australia and New Zealand', 'Mid East', 'UK/Ireland', 'mainland Europe', 'Russia', 'Africa', 'East Asian', 'South Asia']



def distribution():
    names = ['US', 'Canada', 'South America', 'Australia and New Zealand', 'Mid East', 'UK/Ireland', 'mainland Europe', 'Russia', 'Africa', 'East Asian', 'South Asia']
    arr=[0,0,0,0,0,0,0,0,0,0,0]

    total = 0
    misc = 0
    for idx,val in enumerate(gender):
        # for author in val.split(';'):
            # if author == 'm':
        if(regions[idx] != "NAN"):
            if(regions[idx] == "usa"):
                arr[0] = arr[0] + 1
            elif(COO[idx] in eastasian):
                arr[9] = arr[9] + 1
            elif(COO[idx] in southasian):
                arr[10] = arr[10] + 1
            elif(COO[idx] == 'au' or COO[idx] == 'nz'):
                arr[3] = arr[3] + 1
            elif(COO[idx] in mideast):
                arr[4] = arr[4] + 1
            elif(COO[idx] == 'uk' or COO[idx] == 'ie'):
                arr[5] = arr[5] + 1
            elif(COO[idx] == 'russia'):
                print("added 1 to russia")
                arr[7] = arr[7] + 1
            elif(regions[idx] == 'canada'):
                arr[1] = arr[1] + 1
            elif(regions[idx] == 'southamerica'):
                arr[2] = arr[2] + 1
            elif(regions[idx] == 'europe'):
                arr[6] = arr[6] + 1
            elif(regions[idx] == 'africa'):
                arr[8] = arr[8] + 1
            else:
                print(COO[idx])
            total= total + 1

    
    print(arr)
    for i in range(len(arr)):
        arr[i] = arr[i]/total
        arr[i] = 100* round(arr[i],10)

    df = pd.DataFrame()
    df['Groups'] = names
    df['Distribution'] = arr 

    print(df.head(3))

    ax = sns.barplot(x='Groups', y='Distribution', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

    plt.tight_layout()
    plt.savefig('overall distribution of country submission.png')

    print(sum(arr))
    print(total)
    print(names)
    print(arr)

def acceptanceRate():
    names = ['US', 'Canada', 'South America', 'Australia and New Zealand', 'Mid East', 'UK/Ireland', 'mainland Europe', 'Russia', 'Africa', 'East Asian', 'South Asia']
    arr=[0,0,0,0,0,0,0,0,0,0,0]
    arr2=[0,0,0,0,0,0,0,0,0,0,0]

    for idx,val in enumerate(schools):
        #if year[idx]!=2021:
            if(regions[idx] != "NAN"):
                if(regions[idx] == "usa"): 
                    arr[0]+=1 
                    if binary_decisions[decision[idx]]==1: arr2[0]+=1
                elif(COO[idx] in eastasian): 
                    arr[9]+=1 
                    if binary_decisions[decision[idx]]==1: arr2[9]+=1
                elif(COO[idx] in southasian):
                    arr[10]+=1
                    if binary_decisions[decision[idx]]==1: arr2[10]+=1
                elif(COO[idx] == 'au' or COO[idx] == 'nz'):
                    arr[3]+=1
                    if binary_decisions[decision[idx]]==1: arr2[3]+=1
                elif(COO[idx] in mideast):
                    arr[4]+=1
                    if binary_decisions[decision[idx]]==1: arr2[4]+=1
                elif(COO[idx] == 'uk' or COO[idx] == 'ie') :
                    arr[5]+=1
                    if binary_decisions[decision[idx]]==1: arr2[5]+=1
                elif(COO[idx] == 'russia'):
                    arr[7]+=1
                    if binary_decisions[decision[idx]]==1: arr2[7]+=1
                elif(regions[idx] == 'canada'):
                    arr[1]+=1
                    if binary_decisions[decision[idx]]==1: arr2[1]+=1
                elif(regions[idx] == 'southamerica'):
                    arr[2]+=1
                    if binary_decisions[decision[idx]]==1: arr2[2]+=1
                elif(regions[idx] == 'europe'):
                    arr[6]+=1
                    if binary_decisions[decision[idx]]==1: arr2[6]+=1
                elif(regions[idx] == 'africa'):
                    arr[8]+=1
                    if binary_decisions[decision[idx]]==1: arr2[8]+=1

    print(sum(arr))
    print(names)
    print(arr2)
    print(arr)

    for i in range(len(arr)):
        print(arr2[i]/arr[i])
    #colors = sns.color_palette('pastel')[0:5]

    #csfont = {'fontname':'Times New Roman'}
    #hfont = {'fontname':'Helvetica'}

    #plt.title('Pie Chart Showing Where Accepted Papers Come From',**csfont)

    #plt.pie(arr, labels = names, autopct='%.0f%%')
    #plt.show()
    # for i in range(len(arr2)):
    #     try: arr2[i]= arr2[i]/arr[i]
    #     except: arr2[i]=0.0
    # print(arr2)

    # df_acceptance_rate = pd.DataFrame()
    # df_acceptance_rate['Countries'] = names
    # df_acceptance_rate['Acceptance Rate'] = arr2

    # ax_acceptance_rate = sns.barplot(x='Countries', y='Acceptance Rate', data = df_acceptance_rate)
    # ax_acceptance_rate.set_xticklabels(ax_acceptance_rate.get_xticklabels(), rotation=40, ha="right")
    # ax_acceptance_rate.set_title('Acceptance Rate per Country')

    # plt.tight_layout()
    # plt.savefig('acceptance rate of country submission.png')

def getStats():
    names = ['US', 'Canada', 'South America', 'Australia and New Zealand', 'Mid East', 'UK/Ireland', 'mainland Europe', 'Russia', 'Africa', 'East Asian', 'South Asia']
    arr=[[],[],[],[],[],[],[],[],[],[],[]]
    mean_values=[0,0,0,0,0,0,0,0,0,0,0]
    std_values=[0,0,0,0,0,0,0,0,0,0,0]

    for idx,val in enumerate(schools):
        if(regions[idx] != "NAN"):
            if(regions[idx] == "usa"):
                arr[0].append(getMeanScore(scores[idx].split(';')))
            elif(COO[idx] in eastasian):
                arr[9].append(getMeanScore(scores[idx].split(';')))
            elif(COO[idx] in southasian):
                arr[10].append(getMeanScore(scores[idx].split(';')))
            elif(COO[idx] == 'au' or COO[idx] == 'nz'):
                arr[3].append(getMeanScore(scores[idx].split(';')))
            elif(COO[idx] in mideast):
                arr[4].append(getMeanScore(scores[idx].split(';')))
            elif(COO[idx] == 'uk' or COO[idx] == 'ie'):
                arr[5].append(getMeanScore(scores[idx].split(';')))
            elif(COO[idx] == 'russia'):
                arr[7].append(getMeanScore(scores[idx].split(';')))
            elif(regions[idx] == 'canada'):
                arr[1].append(getMeanScore(scores[idx].split(';')))
            elif(regions[idx] == 'southamerica'):
                arr[2].append(getMeanScore(scores[idx].split(';')))
            elif(regions[idx] == 'europe'):
                arr[6].append(getMeanScore(scores[idx].split(';')))
            elif(regions[idx] == 'africa'):
                arr[8].append(getMeanScore(scores[idx].split(';')))
            else:
                print(COO[idx])

    for idx,array in enumerate(arr):
        try:
            mean_values[idx] = sum(array)/len(array)
        except:
            mean_values[idx] = 0
        try:
            std_values[idx] = st.stdev(array)
        except:
            std_values[idx] = 0

    
    print(mean_values)
    print(std_values)

def histograms():
    names = ['US', 'Canada', 'South America', 'Australia and New Zealand', 'Mid East', 'UK and Ireland', 'mainland Europe', 'Russia', 'Africa', 'East Asian', 'South Asia']
    arr=[[],[],[],[],[],[],[],[],[],[],[]]

    for idx,val in enumerate(schools):
        if(regions[idx] != "NAN"):
            if(regions[idx] == "usa"):
                for elem in scores[idx].split(';'):
                    arr[0].append(elem)
            elif(COO[idx] in eastasian):
                for elem in scores[idx].split(';'):
                    arr[9].append(elem)
            elif(COO[idx] in southasian):
                for elem in scores[idx].split(';'):
                    arr[10].append(elem)
            elif(COO[idx] == 'au' or COO[idx] == 'nz'):
                for elem in scores[idx].split(';'):
                    arr[3].append(elem)
            elif(COO[idx] in mideast):
                for elem in scores[idx].split(';'):
                    arr[4].append(elem)
            elif(COO[idx] == 'uk' or COO[idx] == 'ie'):
                for elem in scores[idx].split(';'):
                    arr[5].append(elem)
            elif(COO[idx] == 'russia'):
                for elem in scores[idx].split(';'):
                    arr[7].append(elem)
            elif(regions[idx] == 'canada'):
                for elem in scores[idx].split(';'):
                    arr[1].append(elem)
            elif(regions[idx] == 'southamerica'):
                for elem in scores[idx].split(';'):
                    arr[2].append(elem)
            elif(regions[idx] == 'europe'):
                for elem in scores[idx].split(';'):
                    arr[6].append(elem)
            elif(regions[idx] == 'africa'):
                for elem in scores[idx].split(';'):
                    arr[8].append(elem)
            else:
                print(COO[idx])
    for i in range(len(names)):
        for idx in range (len(arr[i])):
            arr[i][idx] = int(arr[i][idx])
        arr[i].sort()
        print(arr[i])
        ax = sns.displot(x=arr[i], kde=True,bins=10, kind='hist',binwidth=1,stat='density').set(title=names[i] + ' distribution')
        time.sleep(1)
        plt.tight_layout()
        plt.savefig(names[i] + '_distribution.png')
        plt.clf()

def getMeanScore(arr):
    total = 0
    val = 0
    for elem in arr:
        if isinstance(int(elem),int):
            total += 1
            val += int(elem)
    return val/total


def main():
    # distribution()
    acceptanceRate()
    # getStats()
    #histograms()

if __name__ == "__main__":
    main()



