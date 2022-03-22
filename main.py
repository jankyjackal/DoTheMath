from questions import *

def main():
    qs = [
            Question(random_add, amount=3, min=10, max=100),
            ]
    for q in qs:
        q.prompt()

if __name__ == '__main__':
    main()
