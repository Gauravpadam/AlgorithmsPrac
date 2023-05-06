'''
             Recursion tree:
                Go check sum of digits and make logical changes
'''



def productofdigits(n):
    if n == 0: # base case
        return 1
    elif n%10 == 0: # base case 2, saves alot of overhead
        return 0
    else:
        return n%10*productofdigits((n//10)) # Recursive case


print (productofdigits(51116))