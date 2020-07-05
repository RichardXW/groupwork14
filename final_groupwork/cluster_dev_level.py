#!/usr/bin/env python3
# -*- coding: iso8859-1 -*-
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB

'''
regressor = DecisionTreeRegressor(criterion='mse', max_depth=40,
                            max_features=None, max_leaf_nodes=None, min_samples_leaf=1,
                            min_samples_split=2, min_weight_fraction_leaf=0.0,
                            presort=False, random_state=None, splitter='best')
'''

developer = pd.read_csv("../out.csv",encoding="iso8859-1")
df = pd.DataFrame(developer)
factors = [
    "duration(day)",
    "Commit_times"
]
score = df[["Score"]].apply(lambda x:int(x/10) , axis=1)

X_train,X_test,y_train,y_test = train_test_split(df[factors],score,test_size=0.3,random_state=0)

'''
Try with decisionTreeClassifier
'''

X_ax = np.arange(len(y_test))
classifier = DecisionTreeClassifier(max_depth=20)
clf = classifier.fit(X_train,y_train)
predict_X = classifier.predict(X_test)
score= classifier.score(X_test,y_test)
print(score)
plt.scatter(X_ax,predict_X,c="red",label="predict_X")
plt.scatter(X_ax,y_test,c="blue",label="y_test")
plt.legend()
plt.show()


"""
Try with GaussianNB 
"""
#Fit model
model_sk = GaussianNB(priors = None)
model_sk.fit(X_train,y_train)
predict_X = model_sk.predict(X_test)
score = model_sk.score(X_test,y_test)

print(score)
plt.scatter(X_ax,predict_X,c="red",label="predict_X")
plt.scatter(X_ax,y_test,c="blue",label="y_test")
plt.legend()
plt.show()
