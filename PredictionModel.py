from joblib import load

class PredictionModel:
    def __init__(self):
        self.model = load('assets/modelo.joblib')

    def make_prediction(self, data):
        return self.model.predict(data)
