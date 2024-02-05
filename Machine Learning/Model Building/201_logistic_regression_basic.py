# -*- coding: utf-8 -*-
"""
@author: helen

Logistic Regression Basic
"""

# import required packages
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in data
my_df = pd.read_csv("data\sample_data_classification.csv")

# separate input and output data
X = my_df.drop(["output"], axis=1)
y = my_df["output"]

# split out test set and training set
# stratify =y means our train and test sets contain the same proportion of
# classification values in the output variable (1 and 0)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# create classifier object
clf = LogisticRegression(random_state=42)

# train model
clf.fit(x_train, y_train)

# test the regressors prediction with r2 score
y_pred = clf.predict(x_test)
accuracy_score(y_test, y_pred)

# predict the probability that each datapoint will fall into either class
y_pred_prob = clf.predict_proba(x_test)

# confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

plt.style.available
plt.style.use("seaborn-v0_8-poster")
plt.matshow(conf_matrix, cmap="coolwarm")
plt.gca().xaxis.tick_bottom()
plt.title("Confusion Matrix")
plt.ylabel("Actual Class")
plt.xlabel("Predicted Class")

# center the numbers in the matrix
for (i, j), corr_value in np.ndenumerate(conf_matrix):
    plt.text(j, i, corr_value, ha="center", va="center", fontsize=20)
plt.show()
