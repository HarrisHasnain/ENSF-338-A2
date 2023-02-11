def fibonacci(num):
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

if __name__ == "__main__":
   num = 6
   value = fibonacci(num)
   print(f'\nThe value of fibonacci {num} is {value}\n')