import sys

__all__ = [ 'input_ints', 'input_int']


def _input_get(prompt):
    try:
        answer = input(prompt)
    except KeyboardInterrupt:
        print()
        sys.exit()
    except EOFError:
        print()
        sys.exit()
    if answer == 'q':
        sys.exit()
    elif answer == '':
        _input_get(prompt)
    return answer


def input_ints(prompt, delim=' ') -> int:
    answer = _input_get(prompt).split(delim)
    for i in answer:
        if i.isalpha == True:
            return None
    return [int(i) for i in answer]


def input_int(prompt) -> int:
    answer = _input_get(prompt).split(' ')[0]
    if answer.isalpha() == True:
        return None
    return int(answer)


