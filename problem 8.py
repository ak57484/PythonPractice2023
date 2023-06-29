'''
Fake Multiplication Tables
Author : Anil Kaushik
Purpose : Practice
'''

import random


def rohandastable(n):
    multiplyresult = []

    i = 1
    while i <= 10:
        multiplyresult.append(i * n)
        i += 1

    k = random.randint(1, 9)
    multiplyresult[k] = multiplyresult[k] + random.randint(1,n-1)
    print( multiplyresult )

    def iscorrect(table, n):
        for item in multiplyresult:
            if item % n != 0:
                print(f"Wrong element in this table is {item}")
                a=item
                break
            else:
                continue
        return (f"Wrong Item Position in table is {((multiplyresult.index(a))+1)} ")

    investigation = iscorrect(multiplyresult,n)
    print(investigation)

query = int(input("Enter the number whose table you want to know between 2 to Infinity??\n"))
rohandastable(query)



