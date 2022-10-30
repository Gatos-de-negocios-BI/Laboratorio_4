from joblib import load

class Model:
    def __init__(self,columns):
        self.model = load('assets/modelo.joblib')

    def make_prediction(self, data):
        return self.model.predict(data)
