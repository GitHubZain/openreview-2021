import csv
import pandas as pd

df = pd.read_csv('./mycsvfile.csv')
openreview = pd.read_csv('../openreview.csv')

author = df['author_name']
first_time_author = df['first_time_author']
return_2021 = df['return_2021']
first_author = df['first_author']
last_author = df['last_author']
gender2 = df['gender']

for index, value in enumerate(author):
    first_time = True
    for authors, year in zip(openreview['authors'], openreview['year']):
        if type(authors) != float:
            if year<2020:
                author_list = authors.split(';')
                for author_openreview in author_list:
                    if value == author_openreview: 
                        first_time=False
                        break
    if first_time: df.iat[index,9]='1'
    else: df.iat[index,9]='0'

df.to_csv('mycsvfile.csv', encoding='utf-8', index=False)

