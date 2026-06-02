import json
import os
FILE = "users.json"
class User:
    def __init__(self, name=None, score=0):
        self.name = name
        self.score = score
    def ask_name(self):
        self.name = input("Enter your name: ")
        return self.name
    def save_to_file(self):
        data = {
            "name": self.name,
            "score": self.score
        }
        if not os.path.exists(FILE):
            print("No data file—starting fresh!")
            return []
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Corrupted data—starting fresh!")
            return []
        except Exception as e:
            print(f"Error loading: {e}")
            return []
    def save_to_json(self):
        data = User.save_to_file(self)
        with open(FILE, 'w') as f:
            json.dump(data, f, indent = 4)