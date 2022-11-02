from joblib import load

class PredictionModel:

    def __init__(self):
        self.model = load("models/model-v1.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
