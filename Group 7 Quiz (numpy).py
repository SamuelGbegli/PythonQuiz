from numpy import random

def quiz():
    score = 0
    listA = [1,2,3,4,5,6,7]
    random.shuffle(listA)
    for i in range(5):
        if listA[i] == 1:
            score += intQuestion(score)
        if listA[i] == 2:
            score += floatQuestion(score)
        if listA[i] == 3:
            score += boolQuestion(score)
        if listA[i] == 4:
            score += strQuestion(score)
        if listA[i] == 5:
            score += listQuestion(score)
        if listA[i] == 6:
            score += setQuestion(score)
        if listA[i] == 7:
            score += tupleQuestion(score)
    listA = [1,2,3,4,5,6]
    random.shuffle(listA)
    for i in range(5):
        if listA[i] == 1:
            score += addQuestion(score)
        if listA[i] == 2:
            score += commentQuestion(score)
        if listA[i] == 3:
            score += whileQuestion(score)
        if listA[i] == 4:
            score += forQuestion(score)
        if listA[i] == 5:
            score += lowerQuestion(score)
        if listA[i] == 6:
            score += elifQuestion(score)
    print("Your final score is " + str(score) + " out of 10.")

def intQuestion(score):
    answer = input("Give the variable type of this: " + str(random.randint(100))+ "\n")
    if answer.lower() == "int" or answer.lower() == "integer":
         print("Correct.")
         return 1
    else:
        print("Incorrect. The correct answer is integer.")
        return 0
        
def floatQuestion(score):
    answer = input("Give the variable type of this: " + str(random.randint(1,9)/10) + "\n")
    if answer.lower() == "float":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is float.")
        return 0
        
def boolQuestion(score):
    boolean = "True"
    if random.randint(2) == 0:
        boolean = "False"
    answer = input("Give the variable type of this: " + boolean + "\n")
    if answer.lower() == "boolean" or answer.lower() == "bool":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is boolean.")
        return 0
    
def strQuestion(score):
    out = ""
    string = ["a","b","c","apple", "banana", "cherry"]
    index = random.randint(7)
    if index <= 2:
        out = "'" + string[index] + "'"
    else:
        out = '"' + string[index] + '"'
    answer = input("Give the variable type of this: " + out + "\n")
    if answer.lower() == "string" or answer.lower() == "str":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is string.")
        return 0
        
def listQuestion(score):
    answer = input('Give the variable type of this: ["apple", "banana", "cherry"] \n')
    if answer.lower() == "list":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is list.")
        return 0
        
def setQuestion(score):
    answer = input('Give the variable type of this: {"apple", "banana", "cherry"} \n')
    if answer.lower() == "set":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is set.")
        return 0
        
def tupleQuestion(score):
    answer = input('Give the variable type of this: ("apple", "banana", "cherry") \n')
    if answer.lower() == "tuple":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is tuple.")
        return 0

def lowerQuestion(score):
    question = random.randint(2)
    if question == 0:
        answer = input("Give the output of this code block:\nstring = 'Hello'\nstring.lower()\nprint(string)\n")
        if answer =="Hello":
            print("Correct.")
            return 1
        else:
            print("Incorrect. The correct answer is Hello (no change in capitalisation.")
            return 0
    else:
        answer = input("Give the output of this code block:\nstring = 'Hello'\nstring = string.lower()\nprint(string)\n")
        if answer =="hello":
            print("Correct.")
            return 1
        else:
            print("Incorrect. The correct answer is hello (change in capitalisation.")
            return 0

def addQuestion(score):
    x = random.randint(1,11)
    y = random.randint(1,11)
    question = random.randint(2)
    if question == 0:
        answer = input('Give the value of x:\nx = "' + str(x) + '" + "' + str(y) + '"\n')
        if answer == str(x) + str(y):
            print("Correct.")
            return 1
        else:
            print("Incorrect. The correct answer is " + str(x) + str(y) + " (string concatenation).")
            return 0
    else:
        answer = input("Give the value of x:\nx = " + str(x) + " + " + str(y) + "\n")
        try:
            if int(answer) == x + y:
                print("Correct.")
                return 1
            else:
                print("Incorrect. The correct answer is " + str(x + y) + ".")
                return 0
        except:
            print("Incorrect. The correct answer is " + str(x + y) + ".")
    
def commentQuestion(score):
    answer = input("Give the character needed for a single line comment in Python:\n")
    if answer == "#":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is '#'.")
        return 0
        
def whileQuestion(score):
    answer = input("Give the name of the loop that can accept boolean values:\n")
    if answer.lower() == "while" or answer.lower() == "while loop":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct loop is while.")
        return 0
    
def forQuestion(score):
    answer = input("Give the name of the loop that can iterate through a list:\n")
    if answer.lower() == "for" or answer.lower() == "for loop":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct loop is for.")
        return 0
        
def elifQuestion(score):
    answer = input("Give the keyword that can be used between if and else in an if/else statement:\n")
    if answer.lower() == "elif":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct keyword is elif.")
        return 0
   
reset = True    
while reset:
    quiz()
    retry = input("To try again, enter 'yes' or 'y':\n")
    if retry.lower() == "yes" or retry.lower() == "y":
        reset = True
    else:
        reset = False