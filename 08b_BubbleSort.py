from typing import Any


def bubble_sort(elements: list[Any]) -> None:
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements_1 = [5,9,2,1,67,34,88,34]
    elements_2 = [1,2,3,4,2]
    elements_3 = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements_1)
    bubble_sort(elements_2)
    bubble_sort(elements_3)
    print(elements_1)
    print(elements_2)
    print(elements_3)