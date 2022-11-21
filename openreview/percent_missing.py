import pandas as pd
import csv

col_list = ['authors', 'institution', 'year']

df = pd.read_csv('../openreview_again.csv', usecols=col_list)
authors_count=0
institution_count=0
diff = 0
entire = 0

with open('../openreview_again.csv', 'r') as csvfile:
    datareader=csv.reader(csvfile)
    for row in datareader:
        if row[1]=='2021':
            x=row[3].split(';')
            authors_count+=len(x)
            y=row[13].split(';')
            leny = 0
            for institute in y:
                if not(institute==""):
                    leny+=1
            print(len(x))
            print(leny)
            institution_count+=leny
            if leny==len(x):
                diff+=1
                entire+=1
            else: 
                entire+=1

print(1-institution_count/authors_count)
print(authors_count-institution_count)
print(authors_count)
print(entire)
print(diff)

