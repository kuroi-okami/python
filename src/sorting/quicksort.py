from typing import List
from math import floor


def _medianOf3(arr: List, begin: int, end: int) -> (int, int):
    """
    Brief: Help method to provide median of three functionality to quick sort
           An initial pivot is selected - then adjusted be rotating the first index, center index
           and end index into the correct order. The pivot is then moved to the penultimate index
    Args:
        arr: List being sorted
        begin: The first index in scope
        end: The final index in scope

    Returns: Pivot Value - The value being used at the pivot
             Pivot Index - The index which contains the pivot value

    """
    center = floor((begin + end) / 2)

    if arr[center] < arr[begin]:
        arr[begin], arr[center] = arr[center], arr[begin]

    if arr[end] < arr[begin]:
        arr[end], arr[begin] = arr[begin], arr[end]

    if arr[end] < arr[center]:
        arr[center], arr[end] = arr[end], arr[center]

    arr[center], arr[end - 1] = arr[end - 1], arr[center]
    return arr[end - 1], end - 1  # Pivot is not at end - 1


def _partition(arr: List, begin: int, end: int) -> int:
    """
    Brief: Partition an array around a pivot point - with larger values moving to the RHS, and smaller values
           to the LHS

    Args:
        arr: List being sorted
        begin: The first index in scope
        end: The final index in scope

    Returns: The index held by the pivot

    """
    primary_pivot, pivot_index = _medianOf3(arr, begin, end)

    tortoise = begin
    for hare in range(begin, pivot_index):
        if arr[hare] < primary_pivot:
            arr[tortoise], arr[hare] = arr[hare], arr[tortoise]
            tortoise += 1

    arr[tortoise], arr[pivot_index] = arr[pivot_index], arr[tortoise]  # Restore the pivot
    return tortoise


def _recursiveQuickSort(arr: List, begin: int, end: int) -> None:
    """
    Brief: Recursive implementation of Quicksort following the median of three rule,
           to provide a more optimal pivot selection
    Args:
        arr: List being sorted
        begin: The first index in scope
        end: The final index in scope

    Returns: None

    """
    if begin < end:
        index = _partition(arr, begin, end)

        _recursiveQuickSort(arr, begin, index - 1)
        _recursiveQuickSort(arr, index + 1, end)


def quickSort(arr: List) -> None:
    _recursiveQuickSort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    raise NotImplemented("There is no main programme")
