import joblib


class Predictor:

    def __init__(self):

        self.model = joblib.load("model.pkl")

    def predict(self, dataframe):

        prediction = self.model.predict(dataframe)

        probability = self.model.predict_proba(dataframe)

        return {

            "prediction": int(prediction[0]),

            "failure_probability": float(

                probability[0].max()

            )

        }
