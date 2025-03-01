#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

### -- STUDENT ADDITION: Changed the Variable HIGH_SCORE to high_score b/c of case sensitive variables.
high_score = 95
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
### -- STUDENT ADDITION: Test 3 was used to calculate the average before it was defined.
test3 = input('Enter the score for test 3: ')
# Calculate the average test score.
average = test1 + test2 + test3 / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
### -- STUDENT ADDITION: Establishing 4 different inputs for each of the necessary variables.
l1 = input('Enter the length for rectangle 1 (Please only enter numeric values):')
w1 = input('Enter the width for rectangle 1 (Please only enter numeric values):')
l2 = input('Enter the length for rectangle 2 (Please only enter numeric values):')
w2 = input('Enter the width for rectangle 2 (Please only enter numeric values):')
### --- STUDENT ADDITION: Adding a try and except for the input variable calculations. 
try:
    a1 = float(l1)*float(w1)
    print(f"The area of rectangle 1 is {round(a1,4)}")
    a2 = float(l2)*float(w2)
    print(f"The area of rectangle 2 is {round(a2,4)}")
except Exception as e:
    print("ERROR: ",e)
    print("Please ensure the entered values are numeric.")


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

### -- STUDENT ADDITION: Asking for the user to input two mandated variables. 
user_first = input("User's First Name:")
user_age = input("User's Age:")
## -- Adding a try and excep in order to handle error for potential data type or other issues. 
try:
    user_first = str(user_first)
    user_age = int(user_age)
    #Using the variables name and age, print a message to the user stating something along the lines of:
    # "Happy birthday, name!  You are age years old today!"
    print(f"Happy birthday, name!  You are {str(user_age)} years old today!")
except Exception as e:
    print(e)
    print("Please ensure the entered values are correct, specifically with age being only whole number numeric values.")


