from time import perf_counter
import matplotlib.pyplot as plt

def fib_new(num):
   if num < 0:
       print("Invalid number.")
   elif num == 0:
       return 0
   elif num == 1:
       return 1
   else:
       fib = [0, 1]
       for x in range(2, num + 1):
           fib.append(fib[x - 1] + fib[x - 2])
       return fib[x]


def org(n):
    if n == 0 or n == 1:
        return n
    else:
        return org(n-1) + org(n-2)

def main():
    time_result_org = []
    value_n_org = []
    fib_num_org = []
    time_result_new = []
    value_n_new = []
    fib_num_new = []
    for i in range(36):
        start_time_org = perf_counter()
        result_org = org(i)
        end_time_org = perf_counter()
        time_result_org.append(end_time_org - start_time_org)
        value_n_org.append(i)
        fib_num_org.append(result_org)

    for f in range(36):
        start_time_new = perf_counter()
        result_new = fib_new(f)
        end_time_new = perf_counter()
        time_result_new.append(end_time_new - start_time_new)
        value_n_new.append(f)
        fib_num_new.append(result_new)
        
    plt.plot(value_n_org, time_result_org, label = "Original Func")
    plt.plot(value_n_new, time_result_new, label = "Improved Func")

    plt.title("Two types of Fibonnaci Series Code")
    plt.xlabel("Value of n")
    plt.ylabel("Time To Complete Func")

    plt.legend()
    plt.show()


main()