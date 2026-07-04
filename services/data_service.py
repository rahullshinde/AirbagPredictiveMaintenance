import pandas as pd


class DataService:

    @staticmethod
    def load_csv(file):

        """
        Load uploaded CSV file.
        """

        return pd.read_csv(file)


    @staticmethod
    def create_dataframe(vehicle_data):

        """
        Convert manual input dictionary into DataFrame.
        """

        return pd.DataFrame([vehicle_data])


    @staticmethod
    def validate(df):

        """
        Validate required columns.
        """

        required_columns = [

            "VehicleAge",
            "Mileage",
            "BatteryVoltage",
            "Temperature",
            "Humidity",
            "WarningEvents",
            "CrashHistory",
            "SensorVoltage",
            "ECUHealth"

        ]

        missing = []

        for column in required_columns:

            if column not in df.columns:

                missing.append(column)

        return missing
