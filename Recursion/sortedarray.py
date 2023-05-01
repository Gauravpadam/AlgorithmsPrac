
arr = [1,2,2,3,3]

#Logic: bs question
'''
    1. two pointers prev, curr
    2. prev = 0, curr = 1 initially
    3. In next recursion, prev = curr, curr = curr+1
    4. Base case is when curr == len(arr) i.e. 5 in this case, Program returns True
    5. This means sorted array is determined, Recursion tree is linear in this case

                    Recursion tree:

            isSorted(arr,prev=0,curr=1) # Returns True & Control to main
                        |
                        v
        isSorted(arr,prev=curr,curr=curr+1) # Gets true from leaf
                        |
                        v
        isSorted(arr,prev=curr,curr=curr+1) # Gets true
                        |
                        v
        isSorted(arr,prev=curr,curr=curr+1) # Gets true
                        |
                        v
        isSorted(arr,prev=curr,curr=curr+1) # Gets true
                        |
                        v
        isSorted(arr,prev=curr,curr=curr+1) # Curr = 5, Base case hit! Returns True


'''

def isSorted(arr,prev,curr):

    if curr == len(arr):
        return True

    if arr[prev]>arr[curr]:
        return False
    elif arr[prev] <= arr[curr]:
        return isSorted(arr,curr,curr+1)

print (isSorted(arr,0,1))