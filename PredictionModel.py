from joblib import load
import numpy as np
from sklearn.metrics import mean_squared_error

class PredictionModel:
    def __init__(self):
        self.model = load('assets/modelo.joblib')
        self.r2 = 0
        self.rmse = 0

    def make_prediction(self, data):
        return self.model.predict(data)

    def fit(self, data):
        X = data.drop(columns=['Admission Points'])
        y = data['Admission Points']
        self.model.fit(X, y)
        self.r2 = self.model.score(X, y)
        self.rmse = np.sqrt(mean_squared_error(y, self.model.predict(X)))
