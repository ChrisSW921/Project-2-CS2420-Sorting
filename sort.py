"""This is my sort project"""


def quicksort(lyst):
    if isinstance(lyst, list):
        print("Hi")


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


def mergesort(lyst):
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
    if isinstance(lyst, list):
        for x in range(len(lyst)):
            min_idx = x
            for y in range(x + 1, len(lyst)):
                if lyst[min_idx] > lyst[y]:
                    min_idx = y
            lyst[x], lyst[min_idx] = lyst[min_idx], lyst[x]
        return lyst


def insertion_sort(lyst):
    if isinstance(lyst, list):
        print("Hi")


def is_sorted(lyst):
    if isinstance(lyst, list):
        print("Hi")


def main():
    print("Hi")

print(selection_sort([5, 6, 4, 3, 22, 2345, 1256, 3]))
