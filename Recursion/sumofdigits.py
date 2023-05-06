'''
             Recursion tree:

                                  ^
                                  .
                                  .
                                  .
                                  | (sumofdigits=12, Return control to main/function call)
                                  |
                    50106%10  +  sumofdigits(n//10) #sends 5010 (6+6=12)
                          |       ^
                          v       | (Returns 0+6 = 6)
                    5010%10  +   sumofdigits(n//10) # sends 501
                          |       ^
                          v       | (Returns 1+5=6)
                    501%10  +   sumofdigits(n//10) # sends 50
                          |       ^
                          v       | (Returns 0+5=5)
                    50%10  +   sumofdigits(n//10)
                          |       ^   
                          v       |   (Return 5+0=5)
                    5%10  +   sumofdigits(n//10) #sends 0 ,receives 0
                          .       ^
                          .       | (Returns 0)
                (But wait, is n==0 now? Yes)

'''



def sumofdigits(n):
    if n == 0: # base case
        return 0
    else:
        return n%10+sumofdigits((n//10)) # Recursive case


print (sumofdigits(50106))