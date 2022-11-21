import csv
import matplotlib.pyplot as plt
import numpy as np

region_dict = {
    'usa': 'r',
    'asia': 'g',
    'europe': 'b',
    'canada': 'c',
    'australasia': 'm',
    'NAN': 'k',
    'southamerica': 'y'
}
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_ylabel('Average Score')
ax1.set_xlabel('CSRanking')
ax1.set_title('CSRanking of an Institution vs Average Score of Papers from the Institution')
with open('openreview.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    cnt = 0
    for row in csv_reader:
        if cnt > 0:
            arr = row[5].split(';')
            nums = [int(arr[i]) for i in range(len(arr))]
            avg = np.mean(nums)
            ranking_list = row[15].split(';')
            try:
                ranking = int(ranking_list[len(ranking_list) - 1])
            except:
                # continue
                ranking = -100
            try:
                if ranking == -1:
                    # continue
                    ranking = -100
                plt.plot(ranking, avg, region_dict[row[18]] + 'o')
            except:
                continue
        cnt += 1
plt.legend(["US: Red", "Asia: Green", "Europe: Blue", "Canada: Cyan", "Australasia: Magenta", "South America: Yellow", "NAN: Black"], loc='upper right', markerscale=0.01, markerfirst = False)
plt.show()
