import random
import json
def leave_two_options(question, answers):
    correct = answers[0]
    wrong_answers = answers[1:]
    random_wrong = random.choice(wrong_answers)
    remaining = [correct, random_wrong]
    random.shuffle(remaining)
    for i, ans in enumerate(remaining):
        print(f"{i+1}. {ans}")
    return remaining
def ask_the_audience(question, answers):
        correct = answers[0]
        print(f"{correct} 60%")
        print(f"{answers[1]} 20%")
        print(f"{answers[2]} 10%")
        print(f"{answers[3]} 10%")
def change_question(question, answers):
    new_question = random.choice(question_list)
    print(new_question[0] + "?")
    for i, ans in enumerate(new_question[1]):
        print(f"{i+1}. {ans}")
#Ready. function for adding a question to questions.txt
def add_question():
    question = input("Enter your question: ")
    correct_answer = input("Enter the corect answer: ")
    answers = input("Comma-separate the rest of the options: ")
    full_question = question+"?"+correct_answer+","+answers
    with open("questions.txt", "a", encoding = "utf-8") as f:
        f.write(full_question +"\n" )

#Ready. This function creates a list from the questions.txt
def get_questions():
    with open("questions.txt", encoding = "utf-8") as f:
        question_list = f.readlines()
        return question_list  

#Ready. This function creates a questions from the  get_questions()
def create_question(question_list):
    my_question_list = []
    for el in question_list:   
        el = el.strip() 
        if not el or "?" not in el:
            continue 
        el = el.split("?")
        question = el[0]
        answers = el[1].split(",")
        my_question_list.append([question, answers])
        random.shuffle(my_question_list)
    return my_question_list

question_list = create_question(get_questions())
def get_user():
    name = input("Enter your name: ")
    return name
def display_question(question_list):
    correct_answers = 0
    for question, answers in question_list[:3]:
        correct = answers[0]        
        random.shuffle(answers)
        print(question + "?")
        for i, ans in enumerate(answers):
            print(f"{i+1}. {ans}")
        print("You can use one of the following available options. Just enter 1, 2, 3")
        for number, name, func in helping_options:
            print(f"{number}. {name}")
        user_answer = input("Your answer: ")   
        for num, _, func in helping_options:
            if user_answer == num:
                result = func(question, answers)
                if result:
                    answers = result
        if user_answer == correct:
            print("Correct!")
            correct_answers += 1      
        else:
            print("Wrong! Correct answer:", correct)
            return correct_answers
    get_user()    
#display_question(create_question(question_list))   

#This is the inital part of the game
def strat_game_condition():
    print("Choose an option:")

    for num, name, _ in start_game_condition:
        print(f"{num}. {name}")

    choice = input("Enter 1 or 2: ")

    for num, _, func in start_game_condition:
        if choice == num:
            func()
            return
    print("Invalid choice!")

def start_game():
    display_question(question_list)

#Finished Collect user data 
def user_info():
    name = get_user()
    score = display_question(question_list)
    #name = input("Ener your name: ")
    #score = display_question(question_list)
    user = {
        name: score,
    }
    with open("top_players.txt", "a") as f:
        f.write(str(user) + "\n")
        return user


#This function is not finished
def sort_user(users):
    users = []
    with open("top_players.json", "r", encoding="utf-8") as f:
        for line in f:
            users.append(json.loads(line.strip()))
    sorted_users = sorted(users, key=lambda x: x["score"], reverse=True)
    print(sorted_users)


# menu part
helping_options  = (
    ("1", "50:50", leave_two_options),
    ("2", "Ask the Audience", ask_the_audience),
    ("3", "Change Question", change_question),
)
start_game_condition = (
    ("1", "Add question", add_question),
    ("2", "Start game ", start_game),
)

strat_game_condition()
users = user_info()
sort_user(users)