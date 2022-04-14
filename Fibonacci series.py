def printFibonacciNumbers(n):
  #assign the value to local variable
    f1 = 0
    f2 = 1
  #check the n value condition for 0 value
    if (n < 1):
        print(n)
        return
  #print the f1 value
    print(f1, end=" ")
  #create list of 1 to n element for Fibonacci series
    for x in range(1, n):
        print(f2, end=" ")
  #swapping the value
        next = f1 + f2
        f1 = f2
        f2 = next
 
 
# Driven code
printFibonacciNumbers(0)