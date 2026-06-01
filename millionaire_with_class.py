
import random
from Question import Questions
import json
#add user function

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
user = User()
# helping option section
def leave_two_options(question, answers):
    correct = answers[0]
    wrong_answers = answers[1:]
    if not wrong_answers:
        return answers
    random_wrong = random.choice(wrong_answers)
    remaining = [correct, random_wrong]
    random.shuffle(remaining)
    print("50:50 used!")
    for i, ans in enumerate(remaining):
        print(f"{i+1}. {ans}")
    return remaining

def ask_the_audience(question, answers):
    correct = answers[0]
    print("Audience results:")
    print(f"{correct} - 60%")
    if len(answers) > 1:
        print(f"{answers[1]} - 20%")
    if len(answers) > 2:
        print(f"{answers[2]} - 10%")
    if len(answers) > 3:
        print(f"{answers[3]} - 10%")
    return None

def change_question(question, answers):
    new_question = random.choice(question_list)
    print("New question:")
    print(new_question.text + "?")
    for i, ans in enumerate(new_question.answers):
        print(f"{i+1}. {ans}")
    return None


helping_options = (
    ("1", "50:50", leave_two_options),
    ("2", "Ask the Audience", ask_the_audience),
    ("3", "Change Question", change_question),
)


# Ready.. Get from file 
def get_questions():
    with open("questions.txt", encoding = "utf-8") as f:
        question_list = f.readlines()
        return question_list  


def create_question(question_list):
    my_question_list = []
    for el in question_list:
        if "?" not in el:
            continue
        question, raw_answers = el.split("?")
        answers = raw_answers.split(",")
        my_question_list.append(Questions(question, answers))
    random.shuffle(my_question_list)
    return my_question_list

# display question
def display_question(question_list):
    correct_answers = 0
    for question_obj in question_list[:3]:
        answers = question_obj.answers[:]
        correct = answers[0]
        random.shuffle(answers)
        print(question_obj.text + "?")
        for i, ans in enumerate(answers):
            print(f"{i+1}. {ans}")
        print("Help options:")
        for num, name, _ in helping_options:
            print(f"{num}. {name}")
        user_answer = input("Your answer (1-3 or help option): ")
        for num, _, func in helping_options:
            if user_answer == num:
                result = func(question_obj.text, answers)
                if result:
                    answers = result
                    correct = answers[0]
                break
        if user_answer == correct:
            print("Correct!")
            correct_answers += 1      
        else:
            print("Wrong! Correct answer:", correct)
            user.save_to_file()
            return correct_answers
    return correct_answers


#Add question. Ready
def add_question():
    question = input("Enter your question: ")
    correct_answer = input("Enter the correct answer: ")
    answers = input("Comma-separated wrong answers: ")
    full_question = question + "?" + correct_answer + "," + answers
    try:
        with open("questions.txt", "a", encoding="utf-8") as f:
            f.write(full_question + "\n")
    except FileNotFoundError:
        print("File not found!")

# Ready Start game condition section
def start_game():
    score = display_question(question_list)
    print("Game Over!")
    print("Your score:", score)


def start_game_condition():

    user.ask_name()
    print("Choose an option:")
    for num, name, _ in start_game_menu:
        print(f"{num}. {name}")
    choice = input("Enter choice: ")
    for num, _, func in start_game_menu:
        if choice == num:
            func()
            return
    print("Invalid choice!")

start_game_menu = (
    ("1", "Add question", add_question),
    ("2", "Start game", start_game),
)

question_list = create_question(get_questions())
start_game_condition()