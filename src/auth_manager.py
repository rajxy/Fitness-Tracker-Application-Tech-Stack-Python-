import json
import os
import hashlib

class AuthManager:
    """Manages user profiles and secure authentication persistent storage."""

    def __init__(self, profile_file="data/users.json"):
        self.profile_file = profile_file
        self._init_storage()

    def _init_storage(self):
        os.makedirs(os.path.dirname(self.profile_file), exist_ok=True)
        if not os.path.exists(self.profile_file):
            with open(self.profile_file, "w") as f:
                json.dump({}, f)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, username, password, weight, height, age, target_calories=500):
        with open(self.profile_file, "r") as f:
            users = json.load(f)

        if username in users:
            return False, "Username already exists."

        users[username] = {
            "password": self._hash_password(password),
            "weight": weight,
            "height": height,
            "age": age,
            "target_calories": target_calories
        }

        with open(self.profile_file, "w") as f:
            json.dump(users, f, indent=4)

        return True, "User registered successfully."
