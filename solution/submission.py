from sklearn.ensemble import HistGradientBoostingClassifier
import pandas as pd
import numpy as np


def get_model():

    class Model:

        def __init__(self):
            self.model = HistGradientBoostingClassifier(
                max_depth=8,
                max_iter=100,
                random_state=42
            )
            self.selected_features = None
            self.missing_codes = [-1, -2, -4, -5]

        def preprocess_base(self, X):
            # Replace special missing codes with NaN
            X = X.replace(self.missing_codes, np.nan)

            # Keep numeric columns only
            X = X.select_dtypes(include=[np.number])

            return X

        def fit(self, X, y):

            # Remove rows where target is missing
            mask = y.notna()
            X = X[mask]
            y = y[mask]

            X = self.preprocess_base(X)

            # Feature selection via Spearman correlation
            correlations = X.corrwith(y, method="spearman").abs()
            top_features = correlations.sort_values(
                ascending=False
            ).head(40).index

            self.selected_features = top_features

            X = X[self.selected_features]
            X = X.astype("float32")

            self.model.fit(X, y)

            return self

        def predict(self, X):

            X = self.preprocess_base(X)
            X = X[self.selected_features]
            X = X.astype("float32")

            return self.model.predict(X)

        def predict_proba(self, X):

            X = self.preprocess_base(X)
            X = X[self.selected_features]
            X = X.astype("float32")

            return self.model.predict_proba(X)

    return Model()