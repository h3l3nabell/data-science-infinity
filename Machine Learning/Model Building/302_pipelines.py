# -*- coding: utf-8 -*-
"""
@author: helen

Pipelines Basic
"""

# import required packages

import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# import data
my_df = pd.read_csv("data/pipeline_data.csv")

# separate input and output data
X = my_df.drop(["purchase"], axis=1)
y = my_df["purchase"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# specify numeric and categorical features

numeric_features = ["age", "credit_score"]
categorical_features = ["gender"]

#####################################################
# Set up Pipelines
#####################################################

# numeric feature transformer

numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer()),
                                      ("scaler", StandardScaler())])

# Categorical feature transformer
categorical_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="constant", fill_value="U")),
                                          ("ohe", OneHotEncoder(handle_unknown="ignore"))])

# preprocessing pipeline

preprocessing_pipeline = ColumnTransformer(transformers=[("numeric", numeric_transformer, numeric_features),
                                                         ("categorical", categorical_transformer, categorical_features)])

#####################################################
# Apply the Pipeline - compare 2 models in 1 pipeline
#####################################################

# Logistic Regression
clf = Pipeline(steps=[("preprocessing_pipeline", preprocessing_pipeline),
                      ("classifier", LogisticRegression(random_state=42))])

clf.fit(x_train, y_train)

y_pred_class = clf.predict(x_test)
accuracy_score(y_test, y_pred_class)

# Random Forest Classifier
clf = Pipeline(steps=[("preprocessing_pipeline", preprocessing_pipeline),
                      ("classifier", RandomForestClassifier(random_state=42))])

clf.fit(x_train, y_train)

y_pred_class = clf.predict(x_test)
accuracy_score(y_test, y_pred_class)

#####################################################
# Save the Pipeline
#####################################################

joblib.dump(clf, "data/model.joblib")

#####################################################
# restart kernel
# Use the saved Pipeline - import and predict on new data
#####################################################

# import required packages again - np, pd and joblib

clf = joblib.load("data/model.joblib")

# create new data

new_data = pd.DataFrame({"age":  [25, np.nan, 50],
                         "gender": ["M", "F", np.nan],
                         "credit_score": [200, 100, 500]})

# pass in new data and get predictions

y_pred_class = clf.predict(new_data)
