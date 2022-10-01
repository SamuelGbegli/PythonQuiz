def quiz():
    score = 0
    score += intQuestion(score)
    score += floatQuestion(score)
    score += boolQuestion(score)
    score += strQuestion(score)
    score += listQuestion(score)
    score += setQuestion(score)
    score += tupleQuestion(score)
    score += addQuestion(score)
    score += lowerQuestion(score)
    score += concatQuestion(score)
    score += commentQuestion(score)
    score += whileQuestion(score)
    score += forQuestion(score)
    score += falseLowerQuestion(score)
    score += elifQuestion(score)
    print("Your final score is " + str(score) + " out of 15.")

def intQuestion(score):
    answer = input("Give the variable type of this: 200\n")
    if answer.lower() == "int" or answer.lower() == "integer":
         print("Correct.")
         return 1
    else:
        print("Incorrect. The correct answer is integer.")
        return 0
        
def floatQuestion(score):
    answer = input("Give the variable type of this: 3.5\n")
    if answer.lower() == "float":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is float.")
        return 0
        
def boolQuestion(score):
    answer = input("Give the variable type of this: True\n")
    if answer.lower() == "boolean" or answer.lower() == "bool":
        print ("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is boolean.")
        return 0
    
def strQuestion(score):
    answer = input("Give the variable type of this: 'apple'\n")
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
    answer = input("Give the output of this code block:\nstring = 'Hello'\nstring = string.lower()\nprint(string)\n")
    if answer =="hello":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is hello (change in capitalisation.")
        return 0

def falseLowerQuestion(score):
    answer = input("Give the output of this code block:\nstring = 'Hello'\nstring.lower()\nprint(string)\n")
    if answer =="Hello":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is Hello (no change in capitalisation.")
        return 0

def concatQuestion(score):
    answer = input('Give the value of x:\nx = "' + str(10) + '" + "' + str(2) + '"\n')
    if answer == "102":
        print("Correct.")
        return 1
    else:
        print("Incorrect. The correct answer is 105 (string concatenation).")
        return 0
        
def addQuestion(score):
    answer = input("Give the value of x:\nx = 10 + 2\n")
    try:
        if int(answer) == 12:
            print("Correct.")
            return 1
        else:
            print("Incorrect. The correct answer is 12.")
            return 0
    except:
        print("Incorrect. The correct answer is 12.")
        return 0
    
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