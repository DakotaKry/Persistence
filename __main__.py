import NumberSearch
import numpy
import Persistence


def mainFuncation():
    task = input("Type 1 for Persistence, 2 for Factors, or 3 to quit")
    if task == "1":
        num = int(input("Enter a number: "))
        print(Persistence.Persistence(num).persistence())
        mainFuncation()

    elif task == "2":
        num = int(input("Enter a number: "))
        print(NumberSearch.NumberSearch.factors(num))
        mainFuncation()

    elif task == "3":
        print("Quit")
        exit()

    else:
        print("Invalid input, please enter 1, 2, or 3!")
        mainFuncation()


mainFuncation()