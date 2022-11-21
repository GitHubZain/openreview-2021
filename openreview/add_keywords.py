import openreview
import pandas as pd
import csv
import editdistance
import json
import editdistance

# sign in to Open Review
client = openreview.Client(baseurl='https://api.openreview.net',username="",password="")

papers_invi = {2017: "ICLR.cc/2017/conference/-/submission", \
                   2018: "ICLR.cc/2018/Conference/-/Blind_Submission", \
                   2019: "ICLR.cc/2019/Conference/-/Blind_Submission", \
                   2020: "ICLR.cc/2020/Conference/-/Blind_Submission", \
                   2021: "ICLR.cc/2021/Conference/-/Blind_Submission"}

papers_invi2 = {2017: "ICLR.cc/2017/Conference/-/Withdrawn_Submission", \
        2018: "ICLR.cc/2018/Conference/-/Withdrawn_Submission", \
        2019: "ICLR.cc/2019/Conference/-/Withdrawn_Submission", \
        2020: "ICLR.cc/2020/Conference/-/Withdrawn_Submission", \
        2021: "ICLR.cc/2021/Conference/-/Withdrawn_Submission"}

file = open('../openreview2.csv', 'w')
writer = csv.writer(file)

def scrapeKeywords(df):
    """Returns an openreview dataset after matching institution to author"""
    with open (df) as data:
        csv_reader = csv.reader(data)
        lines=[]
        row0=next(csv_reader)
        row0.append('keywords')
        lines.append(row0)
        for row in csv_reader:
            year = row[1]
            found=False
            for note in openreview.tools.iterget_notes(client, invitation=papers_invi[int(year)]):
                title = note.content['title']
                if (editdistance.eval(title, row[2])<=2):
                    keywords_list = note.content['keywords']
                    keywords = ''
                    listlen = len(keywords_list)-1
                    for index, i in enumerate(keywords_list):
                        if index == listlen:
                            keywords +=i
                        else:
                            keywords += i + ';'
                    row.append(keywords)
                    found=True
            if not(found):
                for note in openreview.tools.iterget_notes(client, invitation=papers_invi2[int(year)]):
                    title = note.content['title']
                    if (editdistance.eval(title, row[2])<=2):
                        keywords_list = note.content['keywords']
                        keywords = ''
                        listlen = len(keywords_list)
                        for index, i in enumerate(keywords_list):
                            if index == listlen:
                                keywords +=i
                            else:
                                keywords += i + ';'
                        row.append(keywords)
                        found=True
            elif not(found):
                print(note.content['title'])
            #print(row)
            writer.writerow(row)

if __name__ == "__main__":
    keywords = scrapeKeywords("../openreview.csv")