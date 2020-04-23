from random import shuffle
from typing import List


def InsertionSort(arr: List):
    for i in range(0, len(arr)):
        for j in reversed(range(0, i)):
            if i > 0 and arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
                i -= 1
            else:
                # Stop processing
                break


if __name__ == "__main__":
    raise NotImplementedError("There is no main programme")
