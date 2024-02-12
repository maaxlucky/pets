# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fibonacci_recursive(a=0, b=1, summ=0):
    c = a + b
    a = b
    b = c

    # T
    if c > 4000 * 1000:
        print(summ)
        return summ
    # R
    if c % 2 == 0:
        summ += c
        fibonacci_recursive(a, b, summ)

    else:
        fibonacci_recursive(a, b, summ)


def fibonacci():
    a = 0
    b = 1
    c = a + b
    summ = 0

    for _ in range(1000):
        a = b
        b = c
        c = a + b
        # print(c)
        if c % 2 == 0:
            summ += c
        if c > 4000 * 1000:
            break

    print(summ)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fibonacci()
    fibonacci_recursive()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
