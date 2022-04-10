import pandas as pd
import numpy as np
import seaborn as sns


data = pd.read_csv('datasets/data.csv')

X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# SKLearn
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC

# Logistic regression
logreg = LogisticRegression()
logreg.fit(X, y)
guesses = logreg.predict(X)
acc = accuracy_score(y, guesses)
rmse = mean_squared_error(y, guesses)
error = mean_absolute_error(y, guesses)
print(guesses)
print('error:', error)
print('acc:',acc)
print('rmse:', rmse)


# Decision tree
# dtc = DecisionTreeClassifier()
# dtc.fit(X, y)

# Support Vector Machine
# svm = SVC(verbose=1)
# svm.fit(X, y)
