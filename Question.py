#Question class only
import random
class Question:
    def __init__(self, question, answers):
        self.text = question
        self.answers = answers
        self.correct = answers[0]
    def display_question(self):
        random.shuffle(self.answers)
        print(self.text + "?")
        for i, ans in enumerate(self.answers):
            print(f"{i+1}. {ans}")
    def ask_the_audience(self):
        print("Audience results:")
        print(f"{self.correct} - 60%")
        if len(self.answers) > 1:
            print(f"{self.answers[1]} - 20%")
        if len(self.answers) > 2:
            print(f"{self.answers[2]} - 10%")
        if len(self.answers) > 3:
            print(f"{self.answers[3]} - 10%")

    
    def leave_two_options(self):
        wrong_answers = self.answers[1:]
        random_wrong = random.choice(wrong_answers)
        remaining = [self.correct, random_wrong]
        random.shuffle(remaining)
        print("50:50 used!")
        for i, ans in enumerate(remaining):
            print(f"{i+1}. {ans}")
        return remaining
    