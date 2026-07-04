class RecommendationService:

    @staticmethod
    def get_recommendation(probability):

        probability *= 100

        if probability >= 80:

            return {

                "status": "Critical",

                "recommendation":
                "Immediate Maintenance Required",

                "color": "red"

            }

        elif probability >= 60:

            return {

                "status": "Warning",

                "recommendation":
                "Schedule Maintenance Soon",

                "color": "orange"

            }

        else:

            return {

                "status": "Healthy",

                "recommendation":
                "No Maintenance Required",

                "color": "green"

            }
