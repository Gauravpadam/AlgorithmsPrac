'''
    Any problem which can be broken down into simpler problems, Can be solved by recursion.
    Fibo(N) = Fibo(N-1) + Fibo(N-2) is a 'recurrence relation'

    Two steps to recursion:
        1.Break it down into simple problems
        2.Base condition is the information we already have

    Recursion tree:

                    fib(4)
                   /      \
              fib(3)       fib(2)
             /      \      /     \
         fib(2)   fib(1)   fib(1) fib(0)
          /    \
     fib(1)   fib(0)

'''


def fibonacci(n):
    if n<2: # base case
        return n
    return fibonacci (n-1) + fibonacci (n-2) # recurrence relation


print(fibonacci (4))