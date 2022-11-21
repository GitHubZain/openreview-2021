import csv
from os import stat
import pandas as pd
import numpy as np
import math
import sys
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../return_study/mycsvfile.csv") 
gender = df['gender']
papers_submitted = df['papers_submitted']

def getavg(gender):
    print('do nothing')

def getAvgSubmission(gender_wanted):
    total_submitted = 0
    total_sub_array=[]
    submitted_people = 0
    for idx, elem in enumerate(gender):
        if str(elem) == str(gender_wanted):
            submitted_people = submitted_people + 1
            total_submitted = total_submitted + papers_submitted[idx]
            total_sub_array.append(papers_submitted[idx])
    print(gender_wanted)
    print(total_submitted)
    print(submitted_people)
    print('sd:', st.stdev(total_sub_array))
    print(total_sub_array)
    print(total_submitted/submitted_people)

def main():
    getAvgSubmission('m')
    getAvgSubmission('f')

if __name__ == "__main__":
    main()
