import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv('../openreview.csv')

# convert decision to binary classes accept, reject
decision_to_binary = {'Accept (Poster)': 1, 'Accept (Oral)': 1, 'Accept (Talk)': 1, 'Accept (Spotlight)': 1, 'Invite to Workshop Track': 0, 'Withdrawn': 0, 'Reject': 0}

# fit logistic regression model with either first or last author genders
def logistic_regression(author):
    if author:
        index=0
    else:
        index=-1
        
    scores = []
    gender_indicator = []
    
    y = []
    for ratings, decision, year, gender in zip(data['ratings'], data['decisions'], data['year'], data['gender']):
        #if year != 2020:
        if year != 2021:
            continue
        
        # get decision
        binary_decision = decision_to_binary.get(decision)
        
        # get genders, omit unlablled authors
        genders = gender.split(';')
        if genders[index] == '-1' or genders[index] == 'u':
            continue
        
        # compute gender indicator
        if genders[index] == 'm':
            gender_indicator.append(1)
        else:
            gender_indicator.append(0)
        
        # get mean reviewer score
        rates = ratings.split(';')
        rates = [int(x) for x in rates]
        rating_avg = np.average(rates)

        scores.append(rating_avg)
        y.append(binary_decision)


    X = pd.DataFrame()
    X['mean review score'] = scores
    X['gender indicator'] = gender_indicator
    X['constant'] = [1] * len(scores)
    y = np.array(y)
    
    # fit logistic regression model
    logreg = sm.Logit(y, X)
    result = logreg.fit()
    summary = result.summary()
    
    # compute test accuracy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression(solver='newton-cg', fit_intercept = True, penalty='none')
    result = logreg.fit(X_train, y_train)
    
    # return summary and accuracy
    y_pred = result.predict(X_test)
    return summary, logreg.score(X_test, y_test)

# fit logistic regression model with either first or last author genders
def logistic_regression2(author):
    if author:
        index=0
    else:
        index=-1
        
    scores = []
    gender_indicator = []
    
    y = []
    for ratings, decision, year, gender in zip(data['ratings'], data['decisions'], data['year'], data['gender']):
        #if year != 2020:
        if year != 2021:
            continue
        
        # get decision
        binary_decision = decision_to_binary.get(decision)
        
        # get genders, omit unlablled authors
        genders = gender.split(';')
        if genders[index] == '-1' or genders[index] == 'u':
            continue
        
        # compute gender indicator
        if genders[index] == 'm':
            gender_indicator.append(1)
        else:
            gender_indicator.append(0)
        
        # get mean reviewer score
        rates = ratings.split(';')
        rates = [int(x) for x in rates]
        rating_avg = np.average(rates)

        scores.append(rating_avg)
        y.append(binary_decision)


    X = pd.DataFrame()
    X['gender indicator'] = gender_indicator
    X['constant'] = [1] * len(scores)
    y = np.array(y)
    
    # fit logistic regression model
    logreg = sm.Logit(y, X)
    result = logreg.fit()
    summary = result.summary()
    
    # compute test accuracy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression(solver='newton-cg', fit_intercept = True, penalty='none')
    result = logreg.fit(X_train, y_train)
    
    # return summary and accuracy
    y_pred = result.predict(X_test)
    return summary, logreg.score(X_test, y_test)

print('First author\n')
summary_first, score_first = logistic_regression(True)
print(summary_first)
print('Accuracy: ', score_first)
print('Last author\n')
summary_last, score_last = logistic_regression(False)
print(summary_last)
print('Accuracy: ', score_last)

print('First author\n')
summary_first, score_first = logistic_regression2(True)
print(summary_first)
print('Accuracy: ', score_first)
print('Last author\n')
summary_last, score_last = logistic_regression2(False)
print(summary_last)
print('Accuracy: ', score_last)