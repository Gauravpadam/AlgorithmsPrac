'''
             Recursion tree:

                                  ^
                                  .
                                  .
                                  .
                                  | (sum = 15, Return control to main/function call)
                                  |
                     n    +  sum(n-1) # gets 24 (computes 5 + 10=15)
                          |       ^
                          v       | (Returns 4+6 = 10)
                    n-1   +   sum(n-2) # gets 6
                          |       ^
                          v       | (Returns 3+3=6)
                    n-2   +   sum(n-3) # gets 2
                          |       ^
                          v       | (Returns 2+1=3)
                    n-3   +   sum(n-4) # gets 1
                          |       ^   
                          v       |   (Return 1)
                    n-4   +     ...x
                          .
                          .
                (But wait, is n==1 now? Yes)

'''
def sum(n):

    if n == 1: # base case
        return 1

    return n+sum(n-1) # Recursive case


print (sum(5))