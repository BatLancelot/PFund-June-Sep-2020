text: str = input()
times: int = int(input())


def repeat(a, b):
    result = ''
    for _ in range(0, a):
        result += b
    return result


def repeat_2(a, b):
    return a * b


def repeat_3(string: str, repetitions: int):
    return string * repetitions


print(repeat(times, text))
print(repeat_2(times, text))
print(repeat_3(times, text))



