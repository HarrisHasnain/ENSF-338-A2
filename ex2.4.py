import json
import sys
from time import perf_counter
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)


with open("ex2.json", "r") as read_file:
    data = json.load(read_file)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[end]
    i = start - 1
    for j in range(start,end):
        if array[j] <= p:
            i += 1
            array[i], array[j] = array[j], array[i]
        array[i+1], array[end] = array[end], array[i+1]
        return i+1
        
def main():
    array_lengths = []
    time_to_complete = []
    for i in data:
        array_lengths.append(len(i))
        start = perf_counter()
        result = func1(i, 0, len(i)-1)
        end = perf_counter()
        time_to_complete.append(end-start)

    plt.plot(array_lengths, time_to_complete, label = "QuickSort")


    plt.title("Quicksort Runtime for varying arrays")
    plt.xlabel("array size")
    plt.ylabel("Time To Complete Func")

    plt.legend()
    plt.show()

    

main()
