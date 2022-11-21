import csv
import pandas as pd
import string

def add_theorem(text):
    file = open('./theorem.csv','w')
    writer = csv.writer(file)

    openreview = open(text, 'r')
    csv.field_size_limit(100000000)
    openreview_reader = csv.reader(openreview)

    for row in openreview_reader:
        theorem = 'n'
        try:
            words = row[0].split()
            if len(words)<50:
                theorem = 'pdf miss'
            else:
                for i in range(len(words)):
                    if words[i] == 'Theorem:' or words[i] == 'Proposition:' or words[i] == 'Lemma:':
                        theorem = 'y'
                    try:
                        word = words[i+1].translate(str.maketrans('','',string.punctuation))
                        if (words[i] == 'Theorem' or words[i] == 'Proposition' or words[i] == 'Lemma')and word.isnumeric():
                            theorem = 'y'
                    except:
                        continue
        except:
            theorem = 'pdf miss'
        writer.writerow([theorem])

if __name__ == "__main__":
    add_theorem('../text_openreview.csv')
