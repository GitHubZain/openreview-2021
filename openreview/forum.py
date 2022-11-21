import openreview
import csv


c = openreview.Client(baseurl='https://api.openreview.net')

f = open('./forum.csv', 'w')
writer_f=csv.writer(f)

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

for year in papers_invi.keys():
    for note in openreview.tools.iterget_notes(c, invitation=papers_invi[year]):
        authors = ''
        for i in range(len(note.content['authors'])):
            if i==(len(note.content['authors'])-1):
                authors+=note.content['authors'][i]
            else:
                authors+=(note.content['authors'][i]+';')
        row = note.content['title'] + '\t' + note.forum+ '\t' + authors
        writer_f.writerow([row])
    

for year in papers_invi.keys():
    for note in openreview.tools.iterget_notes(c, invitation=papers_invi2[year]):
        authors = ''
        for i in range(len(note.content['authors'])):
            if i==(len(note.content['authors'])-1):
                authors+=note.content['authors'][i]
            else:
                authors+=(note.content['authors'][i]+';')
        row = note.content['title'] + '\t' + note.forum+ '\t' + authors
        writer_f.writerow([row])
    