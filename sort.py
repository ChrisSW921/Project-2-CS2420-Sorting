"""This is my sort project"""
import random
import time
from recursioncounter import RecursionCounter

def quicksort(lyst):
    """Quicksort function"""
    RecursionCounter()
    if isinstance(lyst, list):
        if len(lyst) <= 1:
            return lyst
        pivot = lyst[len(lyst) // 2]
        left = [x for x in lyst if x < pivot]
        middle = [x for x in lyst if x == pivot]
        right = [x for x in lyst if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    raise ValueError


def merge(left, right):
    """Merge helper function"""
    RecursionCounter()
    sorted_list = []

    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left[0])
            left.pop(0)
        else:
            sorted_list.append(right[0])
            right.pop(0)

    if left:
        sorted_list += left
    if right:
        sorted_list += right

    return sorted_list


def mergesort(lyst):
    """Merge sort"""
    if isinstance(lyst, list):
        if len(lyst) <= 1:
            return lyst

        middle_index = len(lyst) // 2
        left_split = lyst[:middle_index]
        right_split = lyst[middle_index:]

        left_sorted = mergesort(left_split)
        right_sorted = mergesort(right_split)

        return merge(left_sorted, right_sorted)
    raise ValueError


def selection_sort(lyst):
    """Selection sort"""
    if isinstance(lyst, list):
        for num in range(len(lyst)):
            min_idx = num
            for item in range(num + 1, len(lyst)):
                if lyst[min_idx] > lyst[item]:
                    min_idx = item
            lyst[num], lyst[min_idx] = lyst[min_idx], lyst[num]
        return lyst
    raise ValueError


def insertion_sort(lyst):
    """Insertion sort"""
    if isinstance(lyst, list):
        for index in range(1, len(lyst)):
            currentvalue = lyst[index]
            currentposition = index
            while currentposition > 0 and lyst[currentposition - 1] > currentvalue:
                lyst[currentposition] = lyst[currentposition - 1]
                currentposition = currentposition - 1
            lyst[currentposition] = currentvalue
        return lyst
    raise ValueError

def timesort(lyst):
    """Time sort"""
    if isinstance(lyst, list):
        new_list = sorted(lyst)
        return new_list
    raise ValueError


def is_sorted(lyst):
    """Is sorted"""
    if all(isinstance(x, int) for x in lyst) and isinstance(lyst, list):
        sorted_list = False
        if all(lyst[i] <= lyst[i + 1] for i in range(len(lyst) - 1)):
            sorted_list = True
        return sorted_list
    raise ValueError



def main():
    """main function"""
    data_size = 10000
    random.seed(0)
    data = random.sample(range(data_size * 3), k=data_size)

    test = data.copy()
    print("starting selection_sort")
    start = time.perf_counter()
    selection_sort(test)
    end = time.perf_counter()
    print(f"selection_sort duration: {end-start} seconds\n")

    test = data.copy()
    print("starting insertion_sort")
    start = time.perf_counter()
    insertion_sort(test)
    end = time.perf_counter()
    print(f"insertion_sort duration: {end - start} seconds\n")

    test = data.copy()
    print("starting mergesort")
    start = time.perf_counter()
    mergesort(test)
    end = time.perf_counter()
    print(f"mergesort duration: {end - start} seconds\n")

    test = data.copy()
    print("starting quicksort")
    start = time.perf_counter()
    quicksort(test)
    end = time.perf_counter()
    print(f"quicksort duration: {end - start} seconds\n")

    test = data.copy()
    print("starting timesort")
    start = time.perf_counter()
    is_sorted(timesort(test))
    end = time.perf_counter()
    print(f"timesort duration: {end - start} seconds\n")


if __name__ == '__main__':
    main()
