# variables
questionsList = ["What is the data type used to represent whole numbers in Python?",
                 "Which of the following is a valid variable name in Python?", 
                 "In Python, how do you check if two variables are equal?",
                 "How do you define a function in Python?",
                 "What will be the result of the expression `True and False`?",
                 "Which keyword is used to handle exceptions in Python?",
                 "How do you add a single-line comment in Python?",
                 "In Python, which operator is commonly used for string concatenation?",
                 "How do you remove an element from a list by its value in Python?",
                 "Which of the following methods is used to convert a string to uppercase in Python?"]

answersList = [["A. Integer", "B. Float", "C. String", "D. Boolean"],
               ["A. my_variable", "B. 123_variable", "C. variable-name", "D. my variable"],
               ["A. x = y", "B. x == y", "C. x === y", "D. x !=y"],
               ["A. func my_function()", "B. def my_function()", "C. function my_function()", "D. define my_function()"],
               ["A. True", "B. False", "C. None", "D. Error"],
               ["A. try", "B. catch", "C. handle", "D. except"],
               ["A. // comment", "B. /* comment */", "C. # comment", "D. <!-- comment -->"],
               ["A. -", "B. *", "C. /", "D. +"],
               ["A. list.append(element)", "B. list.delete(element)", "C. list.remove(element)", "D. list.push(element)"],
               ["A. str.caseupper()", "B. str.toUpper()", "C. str.uppercase()", "D. str.upper()"]]
               
correctAnswers = ["A", "A", "B", "B", "B", "A", "C", "D", "C", "D"]
userAnsers = []
score = 0
questionNumber = 0

option = input(f"Do you want to play the quiz game?(y/n)")
if(option.lower() != "y"):
    quit()

print("...................Welcome to the quiz game................")
for question in questionsList:
    print("\n------------------------------------------------------------\n")
    print(f"Question - {questionNumber+1} : {question}")

    for option in answersList[questionNumber]:
        print(f"\t-{option}")
    answer = input("Enter the answer (A, B, C, D) : ").upper()
    userAnsers.append(answer)

    if (answer == correctAnswers[questionNumber]):
        score+= 1
        print(f"Correct")
    else : 
        print(f"InCorrect!!!")
        print(f"Correct answer is {correctAnswers[questionNumber]}")
    questionNumber+=1

print("\b#########################Results########################\b")
print(f"Your score is {score/10 *100} %")
