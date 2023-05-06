'''
             Recursion tree:

                                  ^
                                  .
                                  .
                                  .
                                  | (fact = 120, Return control to main/function call)
                                  |
                     n    *   fact(n-1) # gets 24 (computes 5*24=120)
                          |       ^
                          v       | (Returns 6*4 = 24)
                    n-1   *   fact(n-2) # gets 6
                          |       ^
                          v       | (Returns 3*2=6)
                    n-2   *   fact(n-3) # gets 2
                          |       ^
                          v       | (Returns 2*1=2)
                    n-3   *   fact(n-4) # gets 1
                          |       ^   
                          v       |   (Return 1)
                    n-4   *     ...x
                          .
                          .
                (But wait, is n==1 now? Yes)

'''
def fact(n):

    if n <= 1: # base case
        return 1

    return n*fact(n-1) # Recursive case


print (fact(5))