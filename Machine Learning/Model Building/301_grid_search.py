# -*- coding: utf-8 -*-
"""
@author: helen

Grid Search Basic
"""

# import required packages

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd

# read in data
my_df = pd.read_csv("data/sample_data_regression.csv")

# separate input and output data

X = my_df.drop(["output"], axis=1)
y = my_df["output"]

# Instantiate GridSearch object
gscv = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid={"n_estimators": [10, 50, 100, 500],
                "max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None]},
    cv=5,
    scoring="r2",
    n_jobs=-1
)

# fit to data (in practice you'd split into test and train, and fit to train)

gscv.fit(X, y)

# get the best mean cross validation score

gscv.best_score_

# get the best optimal parameters

gscv.best_params_

# so get me the best configured regressor...

regressor = gscv.best_estimator_
