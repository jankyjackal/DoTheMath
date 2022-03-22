#!/usr/bin/python3
from random import randint
from qs.questions import *

def main():
    questions = [
            Question(trys=0, question=square_to_ten)
            ]

    for i in range(4):
        questions.append(
                Question(
                    trys=0, 
                    question=qadd,
                    addends=[randint(1, 100) for i in range(2)]
            )
        )

    for i in range(4):
        questions.append(
                Question(
                    trys=0,
                    question=qmul,
                    factors=[randint(1, 12) for i in range(2)]
            )
        )


    for q in questions:
        q()

if __name__ == '__main__':
    main()
