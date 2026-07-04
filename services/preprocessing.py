import pandas as pd

from sklearn.preprocessing import StandardScaler


class PreprocessingService:

    def __init__(self):

        self.scaler = StandardScaler()

    def clean_data(self, df):

        """
        Handle missing values.
        """

        df = df.copy()

        df.fillna(df.mean(numeric_only=True), inplace=True)

        df.drop_duplicates(inplace=True)

        return df

    def scale_features(self, df):

        """
        Standardize numerical features.
        """

        scaled = self.scaler.fit_transform(df)

        return pd.DataFrame(

            scaled,

            columns=df.columns

        )

    def preprocess(self, df):

        """
        Complete preprocessing pipeline.
        """

        cleaned = self.clean_data(df)

        processed = self.scale_features(cleaned)

        return processed
