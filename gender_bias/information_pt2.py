import csv
import pandas as pd
from pandas.core.dtypes.missing import isna
import numpy as np
import math
import sys
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt
import editdistance

df = pd.read_csv("../openreview.csv") 
gender = df['gender']
authors = df['authors']
results = df['decisions']

def averageAuthorLength(gender_wanted):
    total_authors = 0
    total_first = 0
    array_total_authors=[]

    for idx, list in enumerate(authors):
        if gender[idx].split(";")[0] == gender_wanted:
            curr_list = list.split(";")
            num=0
            for elem in curr_list:
                if elem != '':
                    num += 1
            array_total_authors.append(num)
            total_authors+=num
            total_first += 1
    #return total_first, st.stdev(array_total_authors), total_authors/total_first
    print("n", total_first)
    print("sd", st.stdev(array_total_authors))
    print(total_authors/total_first)

def AuthorDistribution_Percentages():
    #fem same, m same, f diff, m diff
    arr = [0,0,0,0,0,0,0,0]
    for idx, gender_set in enumerate(gender):
        if(len(gender_set.split(";")) > 1):
            if gender_set.split(";")[0] == 'f' and gender_set.split(";")[len(gender_set.split(";"))  - 1] == 'f':
                #print(results[idx])
                if results[idx] != 'Reject' and results[idx] != 'Withdrawn' and results[idx]!='Invite to Workshop Track':
                    arr[0] = arr[0] + 1
                arr[1] = arr[1] + 1
            elif gender_set.split(";")[0] == 'm' and gender_set.split(";")[len(gender_set.split(";"))  - 1] == 'm':
                if results[idx] != 'Reject' and results[idx] != 'Withdrawn' and results[idx]!='Invite to Workshop Track':
                    arr[2] = arr[2] + 1
                arr[3] = arr[3] + 1
            elif gender_set.split(";")[0] == 'f' and gender_set.split(";")[len(gender_set.split(";"))  - 1] == 'm':
                if results[idx] != 'Reject' and results[idx] != 'Withdrawn' and results[idx]!='Invite to Workshop Track':
                    arr[4] = arr[4] + 1
                arr[5] = arr[5] + 1
            elif gender_set.split(";")[0] == 'm' and gender_set.split(";")[len(gender_set.split(";"))  - 1] == 'f':
                if results[idx] != 'Reject' and results[idx] != 'Withdrawn' and results[idx]!='Invite to Workshop Track':
                    arr[6] = arr[6] + 1
                arr[7] = arr[7] + 1
    print(arr)
    print(arr[0]/arr[1])
    print(arr[2]/arr[3])
    print(arr[4]/arr[5])
    print(arr[6]/arr[7])
    '''print('---')
    print((arr[2]+arr[4]+arr[6])/(arr[3]+arr[5]+arr[7]))
    print((arr[3]+arr[5]+arr[7]))
    print('---')
    print((arr[0]+arr[4]+arr[6])/(arr[1]+arr[5]+arr[7]))
    print((arr[1]+arr[5]+arr[7]))
    print('---')
    print((arr[2]+arr[0]+arr[6])/(arr[3]+arr[1]+arr[7]))
    print((arr[3]+arr[1]+arr[7]))
    print('---')
    print((arr[2]+arr[4]+arr[0])/(arr[3]+arr[5]+arr[1]))
    print((arr[3]+arr[5]+arr[1]))'''

def isNaN(string):
    return string != string

def MiddleAuthor_Percentages():
    middle_authors = []
    print(len(authors))
    for index,author_set in enumerate(authors):
        # print(str(author_set) + str(index))
        if author_set == '' or (isinstance(author_set, float) and  math.isnan(author_set)):
            None
        else:
            authors_arr = author_set.split(';')
            for index, author in enumerate(authors_arr):
                if index != 0 and author != '':
                    middle_authors.append(author)
    arr = [0,0,0,0]
    # print(middle_authors)
    for idx, gender_set in enumerate(gender):
        if authors[idx] == '' or (isinstance(authors[idx], float) and  math.isnan(authors[idx])):
            None
        else:
            compAuthor = authors[idx].split(";")[0]
            if gender_set.split(";")[0] == 'f':
                if compAuthor != "" and middle_authors.count(compAuthor) > 0:
                    arr[0] = arr[0] + 1
                arr[1] = arr[1] + 1
            elif gender_set.split(";")[0] == 'm':
                if compAuthor != "" and middle_authors.count(compAuthor) > 0:
                    arr[2] = arr[2] + 1
                arr[3] = arr[3] + 1
    print(arr)
    print("Percent of fem firsts also as middle is: " + str(arr[0]/arr[1]))
    print("Percent of male firsts also as middle is: " + str(arr[2]/arr[3]))
    #print(arr[1])
    #print(arr[3])


def main():
    #averageAuthorLength('m')
    #averageAuthorLength('f')
    #print('- - - - - - - -')
    AuthorDistribution_Percentages()
    #print('- - - - - - - -')
    #MiddleAuthor_Percentages()

if __name__ == "__main__":
    main()