class FitnessCalculator:
    """Calculates automated calorie burn, BMR, and TDEE based on physical activities."""

    MET_VALUES = {
        "Running (8 km/h)": 8.3,
        "Running (11 km/h)": 11.5,
        "Cycling (Moderate)": 6.8,
        "Weightlifting": 5.0,
        "Walking (Brisk)": 3.8,
        "Swimming": 7.0,
        "Yoga": 2.5
    }

    @staticmethod
    def calculate_bmr(weight_kg, height_cm, age, gender):
        """Mifflin-St Jeor Equation for BMR."""
        if gender.lower() == 'male':
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
        else:
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    @classmethod
    def calculate_calories_burned(cls, activity_name, duration_minutes, weight_kg):
        """
        Calorie Burn Formula: Calories = MET * Weight (kg) * (Duration (mins) / 60)
        """
        met = cls.MET_VALUES.get(activity_name, 4.0)
        calories = met * weight_kg * (duration_minutes / 60.0)
        return round(calories, 2)
