"""
Assign 02 - <Zakhaddin Khalidov>

Directions:
    * Complete the sorting algorithm functions that are given below. Note that
      it okay (and probably helpful) to define auxiliary/helper functions that
      are called from the functions below.  Refer to the README.md file for
      additional info.

    * NOTE: Remember to add a docstring for each function, and that a reasonable
      coding style is followed (e.g. blank lines between functions).
      Your program will not pass the tests if this is not done!

    * Be sure that you implement your own sorting functions since.
      No credit will be given if Python's built-in sort function is used.
"""

import time
import random
from math import ceil, log10


def bubbleSort(list_of_items):
    """Bubble sort algorithm for list of integers."""
    start_time = time.time()

    for i in range(len(list_of_items)):
        for j in range(0, len(list_of_items) - i - 1):

            if list_of_items[j] > list_of_items[j + 1]:
                list_of_items[j], list_of_items[j + 1] = list_of_items[j + 1], list_of_items[j]

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def mergeSort2(list):
    """Recursive method for merge sort split by 2."""
    if len(list) > 1:
        mid = len(list) // 2

        left = list[:mid]
        right = list[mid:]

        mergeSort2(left)
        mergeSort2(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list


def merge3Way(list, start, point1, point2, end):
    """Merge method for 3 way merge sort."""
    left = list[start - 1:point1]
    mid = list[point1:point2 + 1]
    right = list[point2 + 1:end]

    left.append(float('inf'))
    mid.append(float('inf'))
    right.append(float('inf'))

    i = 0
    j = 0
    k = 0

    for g in range(start - 1, end):
        minimum = min([left[i], mid[j], right[k]])
        if minimum == left[i]:
            list[g] = left[i]
            i += 1
        elif minimum == mid[j]:
            list[g] = mid[j]
            j += 1
        else:
            list[g] = right[k]
            k += 1


def mergeSort3(list, start, end):
    """Recursive method for merge sort split by 3."""
    if len(list[start - 1:end]) < 2:
        return list
    else:
        point1 = start + ((end - start) // 3)
        point2 = start + 2 * ((end - start) // 3)

        mergeSort3(list, start, point1)
        mergeSort3(list, point1 + 1, point2 + 1)
        mergeSort3(list, point2 + 2, end)

        merge3Way(list, start, point1, point2, end)

        return list


def mergeSort(list_of_items, split_by_3=False):
    """Main function for merge sort."""
    start_time = time.time()

    if split_by_3:
        list_of_items = mergeSort2(list_of_items)
    else:
        start = 1
        end = len(list_of_items)
        list_of_items = mergeSort3(list_of_items, start, end)

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def quickFirst(list):
    """Quick sort method for pivot position first."""
    length = len(list)

    if length <= 1:
        return list
    else:
        pivot = list.pop(0)

    items_greater = []
    items_lower = []

    for item in list:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickFirst(items_lower) + [pivot] + quickFirst(items_greater)


def quickMiddle(list):
    """Quick sort method for pivot position middle."""
    length = len(list)
    pivot = length // 2

    if length <= 1:
        return list
    else:
        pivot = list.pop(pivot)

    items_greater = []
    items_lower = []

    for item in list:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickMiddle(items_lower) + [pivot] + quickMiddle(items_greater)


def quickSort(list_of_items, pivot_to_use='first'):
    """Quick Sort function using multiple pivot points."""
    start_time = time.time()

    if pivot_to_use == 'first':
        list = quickFirst(list_of_items)
    if pivot_to_use == 'middle':
        list = quickMiddle(list_of_items)

    elapsed_time = time.time() - start_time
    return (list, elapsed_time)


def countingSort(list_of_items, exp):
    """Radix sort helper function."""
    n = len(list_of_items)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = list_of_items[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = list_of_items[i] // exp
        output[count[index % 10] - 1] = list_of_items[i]
        count[index % 10] -= 1
        i = i - 1

    i = 0
    for i in range(0, len(list_of_items)):
        list_of_items[i] = output[i]


def radixSort(list_of_items, max_digits):
    """Radix sort function."""
    start_time = time.time()

    list = list_of_items

    max_num = max(list)

    exp = 1
    while max_num / exp > 1:
        countingSort(list, exp)
        exp *= 10

    elapsed_time = time.time() - start_time
    return (list, elapsed_time)


def assign02_main():
    """ A 'main' function to be run when our program is run standalone """
    list1 = list(range(5000))
    random.seed(1)
    random.shuffle(list1)

    # helpful for early testing
    # list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # run sorting functions
    bubbleRes = bubbleSort(list(list1))
    mergeRes2 = mergeSort(list(list1), split_by_3=False)
    mergeRes3 = mergeSort(list(list1), split_by_3=True)
    quickResA = quickSort(list(list1), pivot_to_use='first')
    quickResB = quickSort(list(list1), pivot_to_use='middle')
    radixRes = radixSort(list(list1), ceil(log10(max(list1))))

    # Print results
    print(f"\nlist1 results (randomly shuffled w/ size = {len(list1)})")
    print(list1[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  mergeSort3 time: {mergeRes3[1]:.4f} sec")
    print(mergeRes3[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  quickSortB time: {quickResB[1]:.4f} sec")
    print(quickResB[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])

    # Try with a list sorted in reverse order (worst case for quicksort)
    list2 = list(range(6000, 1000, -1))

    # list2 = [1, 4, 7, 3, 2, 10, 5]

    # run sorting functions
    bubbleRes = bubbleSort(list(list2))
    mergeRes2 = mergeSort(list(list2), split_by_3=False)
    mergeRes3 = mergeSort(list(list2), split_by_3=True)
    quickResA = quickSort(list(list2), pivot_to_use='first')
    quickResB = quickSort(list(list2), pivot_to_use='middle')
    radixRes = radixSort(list(list2), ceil(log10(max(list2))))

    # Print results
    print(f"\nlist2 results (sorted in reverse w/ size = {len(list2)})")
    print(list2[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  mergeSort3 time: {mergeRes3[1]:.4f} sec")
    print(mergeRes3[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  quickSortB time: {quickResB[1]:.4f} sec")
    print(quickResB[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()
