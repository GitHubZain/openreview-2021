import csv

with open('../openreview.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[1]=='2021':
            #print(row[12])
            '''
            if 'Hey that\'s not an ODE' in row[2]:
                line="\"Hey, that's not an ODE\'\": Faster ODE Adjoints with 12 Lines of Code, " + row[12]+", "
            else:
                line=row[2] +', ' +row[12]+", "
            with open('paper_titles_2021.csv', 'a') as f:
                f.write(line+"\n")    
            '''
            if 'Hey that\'s not an ODE' in row[2]:
                line="\"Hey, that's not an ODE\'\": Faster ODE Adjoints with 12 Lines of Code"
            else:
                line=row[2]
            with open('paper_titles_2021.csv', 'a') as f:
                f.write(line+"\n")   