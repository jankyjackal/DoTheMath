#!/usr/bin/python3
from random import randint
from qs.questions import *

def main():

    questions = [
            Question(trys=0, question=square_to_ten)
            ]

    # Addition Qustions
    for i in range(4):
        questions.append(
                Question(
                    trys=0, 
                    question=qadd,
                    addends=[randint(1, 100) for i in range(2)]
            )
        )

    # Subracting Qustions
    for i in range(4):
        questions.append(
            Question(
                trys=0,
                question=qsub,
                minued = randint(1, 100),
                subtrahend = randint(1, 100),
            )
        )

    # Multipliy Qustions
    for i in range(4):
        questions.append(
                Question(
                    trys=0,
                    question=qmul,
                    factors=[randint(1, 12) for i in range(2)]
            )
        )


    # Deviding Qustions
    for i in range(4):
        end = 12
        dividend = randint(1, end)
        devisor = randint(1, end)
        while dividend % devisor != 0:
            dividend = randint(1, end)
            devisor = randint(1, end)

        questions.append(
            Question(
                trys=0,
                question=qdiv,
                dividend = dividend,
                devisor = devisor,
            )
        )

    for q in questions:
        q()

if __name__ == '__main__':
    main()
