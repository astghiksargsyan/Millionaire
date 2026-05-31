#Question class only
class Questions:
    def __init__(self, question, answers):
        self.text = question
        self.answers = answers
        self.correct = answers[0]