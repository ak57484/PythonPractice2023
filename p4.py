# The task you have to perform is “The Next Palindrome.”
# This task consists of a total of 15 points to evaluate your performance.
#
# Problem Statement:-
# A palindrome is a string that, when reversed, is equal to itself.
# Example of the palindrome includes:
#
# 676, 616, mom, 100001.
#
# You have to take a number as an input from the user.
# You have to find the next palindrome corresponding to that number.
# Your first input should be the number of test cases and then take all the cases as input from the user.
#
# Input:
# 3
#
# 451
#
# 10
#
# 2133
#
# Output:
# Next palindrome for 451 is 454
#
# Next palindrome for 10 is 11
#
# Next palindrome for 2311 is 2222

def strret(n):
    x = len(n)
    i = 0
    while i < x:
        print(n[i],end="")
        i=i+1

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def pornot(n):
    str(n)
    if n==n[::-1]:
        print("this is a palindrome")
    elif n != n[::-1]:
        n = int(n)
        while 


inp = input("How many inputs you want to enter")
i=1
while i<=int(inp):
    n = input(f"Enter your {i} choice")
    while True:
        if (f"{n[0]}{n[1]}{n[2]}") != (f"{n[2]}{n[1]}{n[0]}"):
            n=int(n)
            n=n+1
            n=str(n)
            continue
        elif (f"{n[0]}{n[1]}{n[2]}") == (f"{n[2]}{n[1]}{n[0]}"):
            print(f"{n} is a palindrome")
            break
    i=i+1
    continue

