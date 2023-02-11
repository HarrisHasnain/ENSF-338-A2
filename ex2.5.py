import json
import sys
from time import perf_counter
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)


with open("ex2.json", "r") as read_file:
    data = json.load(read_file)
    new_data = sorted(data)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    array_lengths = []
    time_to_complete = []
    for i in new_data:
        array_lengths.append(len(i))
        start = perf_counter()
        result = func1(i, 0, len(i)-1)
        end = perf_counter()
        time_to_complete.append(end-start)

    plt.scatter(array_lengths, time_to_complete, label = "QuickSort")

    plt.title("Quicksort Runtime for varying arrays")
    plt.xlabel("array size")
    plt.ylabel("Time To Complete Func")

    plt.legend()
    plt.show()

main()
