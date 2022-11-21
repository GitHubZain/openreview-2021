import csv
import pandas as pd
import numpy as np
import math
import sys

def distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

print(distance('hello', 'bello'))

df = pd.read_csv("openreview.csv") 
papers = df['paper']
institutions = df['institution']

df2 = pd.read_csv("countryinfo.csv") 

compSchools = df2['institution']
region_values = df2['region']
COO_values = df2['countryabbrv']


COO = []
regions = []

count = 0

NUM_TO_COMPLETE = len(institutions);

for index,schools in enumerate(institutions):
    added = False
    try:
        school = schools.split(';')[len(schools.split(';')) - 1]
        for idx,elem in enumerate(compSchools):
            if abs(distance(school, elem)) < 4:
                if COO_values[idx] == 'russia':
                    print('russian school')
                    print(school)
                    print('- - - - -')
                COO.append(COO_values[idx])
                regions.append(region_values[idx])
                added = True
                count += 1
                break
        if added == False:
            COO.append('NAN')
            regions.append('NAN')
        added = False
    except:
        COO.append('NAN')
        regions.append('NAN')
    if index % 100 == 0:
        print(index)
        print(count/(index + 1))
for elem in COO:
    if elem == 'russia':
        print('entered russia')
final = pd.DataFrame({'paper': papers,'schools': institutions, 'regions':regions, 'COO': COO})
final.to_csv('country_mapping.csv')
print(final)


            
# C:\Users\kgana\Desktop\GitHub Repos\an-open-review-of-openreview-pt2\country