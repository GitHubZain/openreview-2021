import csv
import editdistance
import pandas as pd
import ast

'''file = open('../openreview2.csv', 'w')
writer = csv.writer(file)

openreview = open('../openreview.csv', 'r')
openreview_reader = csv.reader(openreview)
emily_lines = open('../emily_institution.csv', 'r').readlines()

val=0
hi=False
for row in openreview_reader:
    for row2 in emily_lines:
        if row[1]=='2021':
            inst_initial=row2.split(',')[13].strip()
            title=row2.split(',')[2]
            if (editdistance.eval(title, row[2])<=2):
                row[13]=inst_initial
                val+=1
                hi=True
    writer.writerow(row)
print(val)'''

file = open('../openreviewnew.csv', 'w')
writer = csv.writer(file)

openreview = open('../openreview.csv', 'r')
openreview_reader = csv.reader(openreview)

for row in openreview_reader:
    '''
    paper_citations=0
    paper_highly_influential=0
    paper_background_citations=0
    paper_methods_citations=0
    paper_results_citations=0
    '''
    authors_citations = ''
    authors_publications=''
    authors_hindex=''
    authors_highly_influencial_papers=''
    '''
    try: 
        dict = ast.literal_eval(row[21].replace('[', '').replace(']', ''))
        try: paper_citations = int(dict['Citations'])
        except: paper_citations = -1
        try: paper_highly_influential = int(dict['Highly Influential Citations'])
        except: paper_highly_influential = -1
        try: paper_background_citations = int(dict['Background Citations'])
        except: paper_background_citations = -1
        try: paper_methods_citations = int(dict['Methods Citations'])
        except: paper_methods_citations = -1
        try: paper_results_citations = int(dict['Results Citations'])
        except: paper_results_citations = -1
    except:
        paper_citations = -1
        paper_highly_influential = -1
        paper_background_citations = -1
        paper_methods_citations = -1
        paper_results_citations = -1
    '''
    authors_citations = ''
    authors_publications=''
    authors_hindex=''
    authors_highly_influencial_papers=''
    if len(row[26])>5: 
        authors_list = ast.literal_eval(row[26])
        print(authors_list)
        
        for idx, n in enumerate(authors_list):
            try: 
                if idx != len(authors_list)-1: authors_citations += str(n['Citations']) +';'
                else: authors_citations += str(n['Citations'])
            except: 
                if idx != len(authors_list)-1: authors_citations += '-1;'
                else: authors_citations += '-1'
            try: 
                if idx != len(authors_list)-1: authors_publications += str(n['Publications']) +';'
                else: authors_publications += str(n['Publications'])
            except: 
                if idx != len(authors_list)-1: authors_publications += '-1;'
                else: authors_publications += '-1'
            try: 
                if idx != len(authors_list)-1: authors_hindex += str(n['h-index']) +';'
                else: authors_hindex += str(n['h-index'])
            except: 
                if idx != len(authors_list)-1: authors_hindex += '-1;'
                else: authors_hindex += '-1'
            try: 
                if idx != len(authors_list)-1: authors_highly_influencial_papers += str(n['Highly Influential Citations']) +';'
                else: authors_highly_influencial_papers += str(n['Highly Influential Citations'])
            except: 
                if idx != len(authors_list)-1: authors_highly_influencial_papers += '-1;'
                else: authors_highly_influencial_papers += '-1'
    else:
        for idx in range(len(row[3].split(';'))):
            if idx != len(row[3].split(';'))-1: 
                authors_citations += '-1;'
                authors_publications +='-1;'
                authors_hindex +='-1;'
                authors_highly_influencial_papers +='-1;'
            else: 
                authors_citations += '-1'
                authors_publications +='-1'
                authors_hindex +='-1'
                authors_highly_influencial_papers +='-1'


    #row[21]=paper_citations
    #row[22]=paper_highly_influential
    #row[23]=paper_background_citations
    #row[24]=paper_methods_citations
    #row[25]=paper_results_citations
    row[26]=authors_citations
    row[27]=authors_publications
    row[28]=authors_hindex
    row[29]=authors_highly_influencial_papers
    writer.writerow(row)    