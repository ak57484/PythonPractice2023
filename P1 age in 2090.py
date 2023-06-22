# The task you have to perform is “Your Age In 2090”.
# This task consists of a total of 10 points to evaluate your performance.
#
# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable.
# Your program should detect whether the entered input is age or year of birth and
# tell the user when they will turn 100 years old. (5 points).
# Here are a few instructions that you must have to follow:
#
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sorts of errors like :            (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!
#
while True:
    i = input("Tell your age or Year of Birth")
    try:
        if (int(i))<150:
            print (f"Your birth year is {2023-int(i)}")
            r = input("Do you want to know your age in any year y or n")
            if r == 'y':
                w = input("Which Year?")
                z= int(w)-2023
                print(f"Your age in {w} will be {int(i)+z}")
            elif r=="n":
                print("tata")
                exit()
        elif int(i)>1900 and int(i)<2024:
            print (f"Your age is {2023-int(i)}")
            r = input("Do you want to know your age in any year y or n")
            if r == 'y':
                w = input("Which Year?")
                z= int(w)-int(i)
                print(f"Your age in {w} will be {z}")
            elif r=="n":
                print("tata")
                exit()
        else:
            print("invalid input")
    except Exception as e:
        print(e)
    continue





