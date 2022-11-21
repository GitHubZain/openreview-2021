import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import math

data = pd.read_csv('./mycsvfile.csv')
#citationData = pd.read_csv('../datasets/authordata2020.csv')
openreview = pd.read_csv('../openreview.csv')

def logistic_regression():
    accepted_indicator=[]
    scores=[]
    gender_indicator=[]
    num_citations=[]
    genderLastAuthor=[]
    firstTime = []
    numCoauthors = []
    gender_of_last_list=[]
    y=[]
    h_index=[]
    count=0
    for author, ratings, papers_accepted, gender, return_2021, first_author, last_author, first_time, gender_of_last in zip(data['author_name'], data['ratings'], data['papers_accepted'], data['gender'], data['return_2021'], data['first_author'], data['last_author'], data['first_time_author'], data['gender_of_last_author']):
        if gender=='-1' or gender =='u' or gender!='f' or int(first_author)!=1:
            continue
        #or int(last_author)==1
        found=False

        if gender_of_last=='m':
            gender_of_last_list.append(1)
        elif gender_of_last=='f':
            gender_of_last_list.append(0)
        else: continue

        #h-index of last author
        '''
        for authors2, year, authors_hindex in zip(openreview['authors'], openreview['year'], openreview['authors_hindex']):
            if year == 2020:
                if authors2.split(';')[0]==author:
                    if int(authors_hindex.split(';')[-1].replace(',', ''))!=-1:
                        found=True
                        h_index.append(int(authors_hindex.split(';')[-1].replace(',', '')))
            if found:break
        if not(found): continue
        '''
        
        
        '''for index, author_names in enumerate(citationData['authors_review']):
            try: 
                for index2, authorCit in enumerate(author_names.split(';')):
                    print(authorCit)
                    if authorCit == author:
                        found=True
                        h_index.append(int(citationData['author_stats'][index].split('}, {')[-1].split(',')[1].split(':')[-1].replace('\'', '')))
                        break
                if found: break
            except: 
                None
        if not(found): continue'''

        #log citations of last author
        '''
        for authors2, year, authors_citations in zip(openreview['authors'], openreview['year'], openreview['authors_citations']):
            if year == 2020:
                if authors2.split(';')[0]==author:
                    if int(authors_citations.split(';')[-1].replace(',', ''))!=-1:
                        found=True
                        try:
                            log = math.log(int(authors_citations.split(';')[-1].replace(',','')), 10)
                            num_citations.append(log)
                        except: 
                            num_citations.append(int(authors_citations.split(';')[-1].replace(',','')))
            if found:break
        if not(found): continue
        '''

        '''
        for index, author_names in enumerate(citationData['authors_review']):
            try: 
                for index2, authorCit in enumerate(author_names.split(';')):
                    if authorCit == author:
                        try: 
                            log = math.log(int(citationData['author_stats'][index].split('}, {')[-1].split(',')[2].split(':')[-1].replace('\'', '')), 10)
                            num_citations.append(log)
                            found=True
                        except: 
                            None
                        
                        break
                if found: break
            except: 
                None
        if not(found): continue
        '''

        #gender of last author
        '''
        lastGender = False
        for authors, year, genderOfLast in zip(openreview['authors'], openreview['year'], openreview['gender']):
            if type(authors) != float:
                found = True
                if year==2020:
                    author_list = authors.split(';')
                    if author == author_list[0]:
                        if genderOfLast[-1]=='m': 
                            lastGender = True
                            genderLastAuthor.append(1)
                            break
                        elif genderOfLast[-1]=='f': 
                            lastGender = True
                            genderLastAuthor.append(0)
                            break
        if not(found) or not(lastGender): continue
        '''
        #number of coauthors
        '''
        found=False
        for authors, year in zip(openreview['authors'], openreview['year']):
            if type(authors) != float:
                found = True
                if year==2020:
                    author_list = authors.split(';')
                    if author == author_list[0]:
                        numCoauthors.append(len(author_list))
                        break
        '''

        #controlling for first time author code
        '''
        first_time = True
        found = False
        for authors, year in zip(openreview['authors'], openreview['year']):
            
            if type(authors) != float:
                found = True
                if year<2020:
                    author_list = authors.split(';')
                    for author_openreview in author_list:
                        if author == author_openreview:
                            first_time = False

        if not(found): continue

        if first_time: firstTime.append(1)
        else: firstTime.append(0)
        '''

        if gender=='m':
            gender_indicator.append(1)
        else:
            gender_indicator.append(0)

        rates = ratings.replace(']', '').replace('[', '').split(',')
        rates = [int(x) for x in rates]
        rating_avg = np.average(rates)
        scores.append(rating_avg)

        if int(papers_accepted) >=1:
            accepted_indicator.append(1)
        else: accepted_indicator.append(0)

        y.append(int(return_2021))
    
    print(len(firstTime))
    X=pd.DataFrame()
    #X['gender indicator']=gender_indicator 
    X['constant']=[1]*len(scores)
    X['mean reviewer score']=scores
    X['gender of last author'] = gender_of_last_list
    #X['num_citations'] = num_citations
    #X['number of coauthors'] = numCoauthors
    #X['gender of last author'] = genderLastAuthor
    #X['first time author'] = firstTime
    #X['h-index'] = h_index
    #X['accepted indicator']=accepted_indicator
    y=np.array(y)

    logreg = sm.Logit(y, X)
    result = logreg.fit()
    summary = result.summary()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression(solver='newton-cg', fit_intercept = True, penalty='none')
    result = logreg.fit(X_train, y_train)
    
    y_pred = result.predict(X_test)
    print(count)
    return summary, logreg.score(X_test, y_test)

def main():
    summary, score = logistic_regression()
    print(summary)
    print('Accuracy: ', score)

if __name__ == '__main__':
    main()

