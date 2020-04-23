from src.sorting.quicksort import quickSort
from random import shuffle
import pytest


class TestQuicksort:
    def test_quick_sort(self):
        testList = [1, 2, 5, 4, 3, 7, 5, 6, 10]
        expectedResults = [1, 2, 3, 4, 5, 5, 6, 7, 10]

        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults

    def test_quick_sort_small_list(self):
        testList = [1, 3, 2]
        expectedResults = [1, 2, 3]

        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults

    def test_quick_sort_large_list(self):
        testRange = range(0, 1000)
        testList = list(testRange)
        shuffle(testList)  # Shuffle the deck
        expectedResults = list(testRange)

        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults

    @pytest.mark.slow
    def test_quick_sort_very_large_list(self):
        testRange = range(0, 1000000)
        testList = list(testRange)
        shuffle(testList)  # Shuffle the deck
        expectedResults = list(testRange)

        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults

    @pytest.mark.slow
    def test_quick_sort_large_killer_list(self):
        testRange = range(0, 1000000)
        testList, expectedResults = list(reversed(testRange)), list(testRange)
        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults

    def test_quick_sort_already_sorted_small(self):
        testRange = range(0, 1000)
        testList, expectedResults = list(testRange), list(testRange)
        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults

    @pytest.mark.slow
    def test_quick_sort_already_sorted_large(self):
        testRange = range(0, 1000000)
        testList, expectedResults = list(testRange), list(testRange)
        # Invoke method under test
        quickSort(testList)

        assert testList == expectedResults
