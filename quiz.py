# a dictionary that stores questions and answers 
# have a variable that tracks the score of the player 
#loop the dictionary using the key value pairs
# display each question to the user and allow them to answer 
# tell them if they are right or wrong
# show the final result when quix completed

quiz = {
    "question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    "question2":{
        "question":"what is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"what is the capital of Nepal?",
        "answer":"Kathmandu"
    },
    "question4":{
        "question":"what is the capital of Italy?",
        "answer":"Rome"
    },
    "question5":{
        "question":"what is the capital of Spain?",
        "answer":"Madrid"
    },
    "question6":{
        "question":"what is the capital of Portugal?",
        "answer":"Lisbon"
    },
    "question7":{
        "question":"what is the capital of Switzerland?",
        "answer":"Bern"
    },
    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("answer?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your Score is :" + str(score))
        print

    else :
        print("wrong!")
        print("the answer is :" + value['answer'])
        print("your score is:"+ str(score))
