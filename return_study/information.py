import csv
import pandas as pd
import math
import sys
import statistics as st
import time


df = pd.read_csv("mycsvfile.csv") 
submission = df['papers_submitted']
acceptance = df['papers_accepted']
rejections = df['papers_rejected']
returns = df['return_2021']
first = df['first_author']
last = df['last_author']
gender = df['gender']


print(gender)
total = 0
repeats = 0
double = 0


cnt = 0
for idx, elem in enumerate(submission):
    if first[idx] == 1:
        if elem == 1:
            cnt += 1
print("1 papers are: " + str(cnt))


for idx, value in enumerate(rejections):
    if first[idx] == 1:
        if gender[idx] == 'f':
            if value > 0 and returns[idx] == 1:
                repeats += 1
            total += 1

print(double)
print(total)
print(repeats)
print(repeats/total)