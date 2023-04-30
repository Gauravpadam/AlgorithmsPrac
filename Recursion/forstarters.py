# Recursion is solving a problem by recalling the problem solution

# Lets take a function

def message(n,t):
    if n == t: # Base case of recursion
        print (n)
        return
    print (n)
    message (n+1,t) # Function calling itself

message(1,10) # print numbers from 1 to 10

#Points to be noted**:
'''
    1.When a function is called, It enters stack memory
    2.Till the function is being executed, It STAYS in the stack memory
    3.Same functions with different parameters are pushed into the stack alongwith their parameters**
'''