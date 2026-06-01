import json
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
        try:
            with open("users.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(data) + "\n")
        except FileNotFoundError:
            print("File not found!")   