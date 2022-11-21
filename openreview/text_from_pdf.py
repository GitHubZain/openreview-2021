import os
import csv
import textract
import sys
from tika import parser

'''


file = open('../text_openreview.csv', 'w')
writer = csv.writer(file)
text_byte = textract.process('./iclr_pdfs/1.pdf').replace(b"\n", b" ").strip()
text=text_byte.decode('utf-8')
writer.writerow([text])



file = open('../text_openreview.csv', 'w')
writer = csv.writer(file)
x=range (1, 8643)
for n in x:
    try:
        text_byte = textract.process('./iclr_pdfs/'+str(n)+'.pdf').replace(b"\n", b" ").strip()
        writer.writerow([text_byte.decode('utf-8', errors='ignore')])
    except:
        print(n)
        writer.writerow('')
        continue
'''
file = open('../text_openreview.csv', 'w')
writer = csv.writer(file)
x=range (1, 8643)
for n in x:
    try:
        raw = parser.from_file('./iclr_pdfs/'+str(n)+'.pdf')['content']
        content = str.join('', raw.splitlines())
        writer.writerow([content])
    except:
        print(n)
        writer.writerow('')
        continue