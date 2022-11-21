import csv
import matplotlib.pyplot as plt
import numpy as np
import collections

withdrawn_cnt = 0
all_names = []
this_dict = {

}
binary_decisions = {'Accept (Oral)':1, 'Accept (Poster)':1, 'Accept (Spotlight)':1, 'Accept (Talk)':1, 'Withdrawn':0, 'Reject':0, 'Invite to Workshop Track':0}

with open('openreview_2020.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        names = row[3].split(';')
        ratings = row[5].split(';')
        nums = [int(i) for i in ratings]
        decision = row[7]
        genders = row[17].split(';')
        firstLastAuthor = [names[0], names[-1]]
        otherAuthors = names[1:-1]
        for index, name in enumerate(firstLastAuthor):
            if name not in this_dict:
                this_dict[name] = [[nums], [], [], [1],[], 0, 0, 0]
                if binary_decisions[decision] == 0:
                    this_dict[name][1] = [0]
                    this_dict[name][2] = [1]
                else:
                    this_dict[name][1] = [1]
                    this_dict[name][2] = [0]
                this_dict[name][4]=genders[index]
            else:
                this_dict[name][0].append(nums)
                if binary_decisions[decision] == 0:
                    this_dict[name][2][0]+=1
                else:
                    this_dict[name][1][0]+=1
                this_dict[name][3][0] += 1
            if index==0: this_dict[name][6]=1
            else: this_dict[name][7]=1
            
        for name2 in otherAuthors:
            if name2 in this_dict:
                this_dict[name2][0].append(nums)
                if binary_decisions[decision] == 0:
                    this_dict[name2][2][0]+=1
                else:
                    this_dict[name2][1][0]+=1
                this_dict[name2][3][0] += 1

with open('openreview_2021.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        names = row[3].split(';')
        for name in names:
            if name in this_dict: this_dict[name][5]=1

with open('mycsvfile.csv','w', encoding='utf8') as f:
    w = csv.writer(f)
    for key in this_dict:
        string = str(key) + ";" + str(this_dict[key][0]) + ";" + str(this_dict[key][1][0]) + ";" + str(this_dict[key][2][0]) + ';' + str(this_dict[key][3][0]) + ';' + str(this_dict[key][4]) + ';' + str(this_dict[key][5])+ ';' + str(this_dict[key][6])+ ';' + str(this_dict[key][7])
        w.writerow([string])
    #w.writerows(this_dict.items())

'''
    for name in names:
        if name not in this_dict:
            this_dict[name] = [[nums], [], [], [1]]
            if binary_decisions[decision] == 0:
                this_dict[name][1] = [0]
                this_dict[name][2] = [1]
            else:
                this_dict[name][1] = [1]
                this_dict[name][2] = [0]
        else:
            this_dict[name][0].append(nums)
            if decision == 'Reject':
                this_dict[name][2][0] += 1
            elif decision == 'Withdrawn':
                withdrawn_cnt += 1
            else:
                this_dict[name][1][0] += 1
            this_dict[name][3][0] += 1
'''
