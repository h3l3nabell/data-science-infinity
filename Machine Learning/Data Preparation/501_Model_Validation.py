# -*- coding: utf-8 -*-
"""
@author: helen

Model Validation
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold

# Test Train Split
my_df = pd.read_csv("feature_selection_sample_data.csv")

X = my_df.drop(["output"], axis=1)
y = my_df["output"]

# by default it shuffles the data, which is important so the test set
# contains a similar profile to the training set
# Regression Model
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Classification Model
# x_train, x_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify= y)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
r2_score(y_test, y_pred)

# Cross Validation
cv_scores = cross_val_score(regressor, X, y, cv=4, scoring="r2")
print(cv_scores.mean())

# Cross validation method doesnt shuffle or randomise order though
# to do that we can use k fold

# Regression

cv = KFold(n_splits=4, shuffle=True, random_state=42)
cv_scores = cross_val_score(regressor, X, y, cv=cv, scoring="r2")
print(cv_scores.mean())

# Classification
cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
cv_scores = cross_val_score(classifier, X, y, cv=cv, scoring="accuracy")
print(cv_scores.mean())
