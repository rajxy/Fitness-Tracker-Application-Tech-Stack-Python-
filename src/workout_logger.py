import os
import pandas as pd
from datetime import datetime

class WorkoutLogger:
    def __init__(self, storage_path="data/workout_logs.csv"):
        self.storage_path = storage_path
        self.columns = ["date", "username", "activity", "duration_mins", "calories_burned", "notes"]
        self._initialize_storage()

    def _initialize_storage(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.storage_path, index=False)

    def log_workout(self, username, activity, duration_mins, calories_burned, notes=""):
        """Logs a workout entry using Pandas dataframe append operations."""
        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "username": username,
            "activity": activity,
            "duration_mins": duration_mins,
            "calories_burned": calories_burned,
            "notes": notes
        }
        df = pd.read_csv(self.storage_path)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(self.storage_path, index=False)
        return new_entry

    def get_user_logs(self, username):
        """Retrieves and filters user logs into a Pandas DataFrame."""
        df = pd.read_csv(self.storage_path)
        if df.empty:
            return pd.DataFrame(columns=self.columns)
        return df[df["username"] == username]
