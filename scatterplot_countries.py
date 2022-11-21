import csv
import matplotlib.pyplot as plt
import numpy as np

mideast = ['bh', 'cy', 'eg', 'ir', 'iq', 'il', 'jo', 'kw', 'lb', 'om', 'ps', 'qa', 'sa', 'sy', 'tr', 'ae', 'ye']
eastasian = ['cn', 'jp', 'mn', 'kp', 'kr', 'tw', 'hk']
southasian = ['af', 'bd', 'bt', 'in', 'np', 'pk', 'lk', 'mv', 'sg']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_ylabel('Average Score')
ax1.set_xlabel('CSRanking')
ax1.set_title('CSRanking of an Institution vs Average Score of Papers from the Institution')

arra = [[], [], [], [], [], [], [], [], [], [], []]

with open('openreview.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    cnt = 0
    for row in csv_reader:
        if cnt < 1:
            cnt += 1
            continue
        arr = row[5].split(';')
        nums = [int(arr[i]) for i in range(len(arr))]
        avg = np.mean(nums)
        ranking_list = row[15].split(';')
        try:
            ranking = int(ranking_list[len(ranking_list) - 1])
        except:
            # continue
            ranking = -100
        if ranking == -1:
            ranking = -100

        region = row[18]
        coo = row[19]
        if coo == 'usa':
            arra[0].append([ranking, avg])
        elif coo in eastasian:
            arra[1].append([ranking, avg])
        elif coo in southasian:
            arra[2].append([ranking, avg])
        elif coo == 'au' or coo == 'nz':
            arra[3].append([ranking, avg])
        elif coo in mideast:
            arra[4].append([ranking, avg])
        elif coo == 'uk' or coo == 'ie':
            arra[5].append([ranking, avg])
        elif coo == 'russia':
            arra[6].append([ranking, avg])
        elif coo == 'ca':
            arra[7].append([ranking, avg])
        elif coo == 'br' or coo == 'cl':
            arra[8].append([ranking, avg])
        elif region == 'europe' and (coo != 'uk' and coo != 'ie'):
            arra[9].append([ranking, avg])
        elif region == 'africa':
            arra[10].append([ranking, avg])

for pair in arra[0]:
    plt.plot(pair[0], pair[1], color='r', marker='o')
for pair in arra[1]:
    plt.plot(pair[0], pair[1], color='g', marker='o')
for pair in arra[2]:
    plt.plot(pair[0], pair[1], color='b', marker='o')
for pair in arra[3]:
    plt.plot(pair[0], pair[1], color='y', marker='o')
for pair in arra[4]:
    plt.plot(pair[0], pair[1], color='m', marker='o')
for pair in arra[5]:
    plt.plot(pair[0], pair[1], color='c', marker='o')
for pair in arra[6]:
    plt.plot(pair[0], pair[1], color='k', marker='o')
for pair in arra[7]:
    plt.plot(pair[0], pair[1], color='tab:orange', marker='o')
for pair in arra[8]:
    plt.plot(pair[0], pair[1], color='sienna', marker='o')
for pair in arra[9]:
    plt.plot(pair[0], pair[1], color='cadetblue', marker='o')
for pair in arra[10]:
    plt.plot(pair[0], pair[1], color='navy', marker='o')

plt.show()
