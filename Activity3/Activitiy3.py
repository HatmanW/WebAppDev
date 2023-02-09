'''This is for activity 3 for ISQA 3900.
Objectives
This assignment provides an introduction and/or review of basic Python features and good programming practice,
including:
● Initializing variables and assigning data
● Python syntax for displaying simple output messages
● Python user input functions
● Boolean expressions
● Selection statements - If, Elif and Else
● Repetition structure (while loop)
● Defining and calling Python functions
● Recovering from user input errors, including recovering when non-numeric values are entered for numeric data.
● Debugging errors found in a simple python program
● Good programming practice, including:
    ○ Descriptive variable and function names
    ○ Simple comments including the following REQUIRED program file header at the top of the Python file:
        ■ Your name
        ■ The course name and date
        ■ A short description of the code in the file (i.e. purpose of the program)

normal commands will be the call out for when an objective should be met.
'''



def display_title():
    '''Displays the title of the program when called.

    Description: Print's the program title.
    input: N/A
    function: N/A
    Output: Print statement
    '''
    print("Welcome to the Grade Calculator.") #Print's the program title.


def get_totalPoints():
    '''Initial comment: This function prompts the user for and reads the total points earned. If the user enters a value
    that is less than 0 or greater than 1000, report an error and ask the user to reenter the value.
    Continue to read and validate the total points until the user enters an acceptable value. Once
    an acceptable value is entered, return the value to the main method. Use a repetition
    structure.
    The program should not crash if the user enters a non-numeric value for the score.

    Description:
    Prompts user for a range between 0-1000, if out of range re-prompts the user for correct input.
    If the user enters the wrong data type, Value error catches to re-prompt the user for correct input.
    input: value between 0-1000.
    function: Catch incorrect input, or restrict the range of the of value variable to be 0-1000.
    Output: returned correctly entered value. (0-1000)
    '''

    while True:
        try:
            value = int(input("Enter the total score (0-1000): ")) #takes the user's
            if value < 0 or value > 1000: #THIS NEEDS TO BE AN OR DANG NAB IT Range needs to be between 0 and 1000.
                print()
                print("Value entered must be between 0-1000. Try again.") #reprompting user
                print()
            else:
                return value
        except ValueError: #value error catch to reprompt user to enter proper interger range.
            print("you must enter an interger value >=0 and <= 1000. Try again.") #reprompt
            print()



def get_letterGrade(averageEarned): #takes averageEarned variable from main
    '''Initial comment: This functions receives the average grade from the main() and returns the letter grade based
    on the average earned. Use if, elif, else to determine the correct letter grade based on the
    averageEarned.

    Description:
    takes the earned average variable from the main function, executes through and If/Elif/Else tree with the desired letter
    grades.
    Returns the accompanying letter grade from the formula in the main statement: totalpoints/1000 * 100.
    Further detail of formula below in main statement.
    Input: averageEarned variable
    function: process variable through If tree
    output: return lettergrade variable
    '''

    if averageEarned >= 92:
        lettergrade = 'A'
    elif 88 <= averageEarned <91.99:
        lettergrade = 'B+'
    elif 82 <= averageEarned <87.99:
        lettergrade = 'B'
    elif 78 <= averageEarned <81.99:
        lettergrade = 'C+'
    elif 70 <= averageEarned <77.99:
        lettergrade = 'C'
    elif 60 <= averageEarned <69.99:
        lettergrade = 'D'
    else:
        lettergrade = 'F'
    return lettergrade #result is later recorded as grade


def main():
    '''Initial comment:
    1. The main function first calls the display_title function which displays the title.
    2. Next, the main function calls the get_totalPoints function to get the total points earned.
    3. Next, the main function then passes the percentage grade earned
    (total_points/1000*100) to the get_letterGrade function which will return the earned
    letter grade.
    4. Next the main function prints the letter grade for the student.
    5. Next, the main function asks the user if the program should continue.  If yes, repeat steps
    2-4 or if no, end the program. Use a repetition structure.

    Description: should meet Initial comment's requirements.
    1. prints program title
    2. uses the input checking methods in get_totalPoints
    3. Initial variable of choice is 'y' for prompt checking.
    A) takes the entered score (get_totalPoints) and passes to a new variable. (total_points)
    B) Applies the formula to the variable total_points(0-1000)/1000*100 to a new variable, averageEarned.
    C) Applies the value from averaged earned into the function for get_letterGrade, and assigns to the variable grade
    4. Applies the print varibles averageEarned, and grade to the print statement.
    5. Reprompts the user in a while loop that can only be exited upon typing 'n'.
    input prompt statement informs user of condition.
    '''


    display_title()
    choice = "y"
    while True:
        if choice.lower() == "y":
            total_points = get_totalPoints()
            averageEarned = total_points/1000*100
            grade = get_letterGrade(averageEarned)
            print(f"You earned an average of {averageEarned} Letter grade earned: {grade}")
            print()
            choice = input("would you like to enter another score (y/n)?: ")
        elif choice.lower() == 'n':
            print()
            print("Thank you")
            break
        else:
            print("Please enter (y/n)")
            print()
            choice = input("would you like to enter another score (y/n)?: ")

if __name__ == "__main__":
    '''Normal Dunder statement. '''
    main()
