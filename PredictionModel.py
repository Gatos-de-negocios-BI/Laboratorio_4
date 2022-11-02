from joblib import load

class PredictionModel:
    def __init__(self):
        self.model = load('assets/modelo.joblib')

    def make_prediction(self, data):
        return self.model.predict(data)

    def fit(self, data):
        X = data.drop(columns=['Admission Points'])
        y = data['Admission Points']
        self.model.fit(X, y)
        self.r2 = self.model.score(X, y)
        self.rmse = np.root(mean_squared_error(y, self.model.predict(X)))
