import csv
import pandas as pd

df = pd.read_csv('./mycsvfile.csv')

author = df['author_name']
first_time_author = df['first_time_author']
return_2021 = df['return_2021']
first_author = df['first_author']
last_author = df['last_author']
gender = df['gender']
gender_last = df['gender_of_last_author']

for index, value in enumerate(author):
    try:
        if (first_author[index]==1 and last_author[index]==1) or last_author[index]==1:
            if gender[index]=='m': df.iat[index, 10]=1
            elif gender[index]=='f': df.iat[index, 10]=0
            else: df.iat[index, 10]=-1
        elif first_author[index]==1: 
            if gender[index+1]=='m': df.iat[index, 10]=1
            elif gender[index+1]=='f': df.iat[index, 10]=0
            else: df.iat[index, 10]=-1
        else:
            print('missing')
    except: df.iat[index, 10]=-1

df.to_csv('mycsvfile.csv', encoding='utf-8', index=False)

