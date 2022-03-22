from .inputs import *
from random import randint

__all__ = ['Question', 'qadd', 'qmul', 'square_to_ten']

class Question:

    def __init__(self, question, trys=0, *args, **kwargs):
        self.question = question
        self.trys = trys if trys != 0 else -1
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        while self.trys != 0:
            r = self.question(*self.args, **self.kwargs)
            if r == False:
                print("Wrong!")
                self.trys -= 1
            elif r == None:
                print("Huh?")
            elif r == True:
                print("Correct!")
                break

def qadd(addends: list):
    s = sum(addends)
    prompt = ' + '.join([str(i) for i in addends])
    answer = input_int(f"{prompt} = ")
    if answer == None:
        return None
    elif answer == s:
        return True
    return False


def qmul(factors: list):
    product = 1
    for i in factors:
        product *= i

    prompt = ' × '.join([str(i) for i in factors])
    answer = input_int(f"{prompt} = ")
    if answer == None:
        return None
    elif answer == product:
        return True
    return False


def qdiv(dividend, devisor):
    raise NotImplemented
    quotient = dividend / devisor


def square_to_ten():
    answers = input_ints("1² to 10²: ")
    if answers == None:
        return None

    if len(answers) != 10:
        print(f"Wrong amount of numbers: [{len(answers)}/10]")
        return None

    answers = [int(i) for i in answers]
    answers.extend([i**2 for i in range(1,11)])
    if len(set(answers)) != 10:
        return False
    return True
