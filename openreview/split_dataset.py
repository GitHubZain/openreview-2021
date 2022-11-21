import csv

def split_dataset(dataset, num_row, emily_data, keshav_data, zain_data):
    div_three = int(num_row/3)
    num_left = num_row - div_three - div_three
    emily = open(emily_data, 'w')
    keshav = open(keshav_data, 'w')
    zain = open(zain_data, 'w')
    emily_writer = csv.writer(emily)
    keshav_writer = csv.writer(keshav)
    zain_writer = csv.writer(zain)
    for i in range(div_three):
        with open(dataset) as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            emily_writer.writerow(rows[i])
    for i in range(div_three):
        with open(dataset) as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            keshav_writer.writerow(rows[div_three+i])
    for i in range(num_left):
        with open(dataset) as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            zain_writer.writerow(rows[div_three+div_three+i])

def no_institution(new):
    writer = csv.writer(new)
    with open('../openreview.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[1] == '2021':
                x=row[3].split(';')
                y=row[13].split(';')
                leny = 0
                for institute in y:
                    if not(institute==""):
                        leny+=1
                if not(leny==len(x)):
                    if y[0]=='' or y[-1] == '':
                        writer.writerow(row)

if __name__  == "__main__":
    f = open('../no_institutions.csv', 'w')
    no_institution_data = no_institution(f)
    with open('../no_institutions.csv') as f_split:
        row_count_institution = sum(1 for line in f_split)
    split_dataset('../no_institutions.csv', row_count_institution, '../emily_institution.csv', '../keshav_institution.csv', '../zain_institution.csv')

    f2 = open('../no_gender.csv', 'w')
    writer_gender = csv.writer(f2)
    with open('../openreview.csv', 'r') as openreview:
        datareader = csv.reader(openreview)
        for row in datareader:
            if row[1]=='2021':
                writer_gender.writerow(row)
    with open('../no_gender.csv') as f_split2:
        row_count_gender = sum(1 for line in f_split2)
    split_dataset('../no_gender.csv', row_count_gender, '../emily_gender.csv', '../keshav_gender.csv', '../zain_gender.csv')

