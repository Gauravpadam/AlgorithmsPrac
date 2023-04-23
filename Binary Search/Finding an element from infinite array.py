'''Logic: This is an infinite array, No length methods can define the length of an infinite array.
        So, The main issue is finding the start and end indices of the array, rest question is bs.
        For this, We set a window initially of 2 elements, And we keep expanding this window exponentially.
        Thus, We are actually going from 1 -> N in logN time covering the whole infinite array, i.e. The converse
        of binary search algorithm.
        Element is bound to be caught somewhere if it exists in this infinite array
        Also, List index out of range is none of my concern, Array is supposed to be infinite, Cant simulate one here'''

def binarySearch (arr,s,e,target):
    while s <= e:
        mid = s + (e-s)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return -1

def ans(arr, target):
    #Setting the window of 2 initially
    s = 0
    e = 1

    #We search for the next window where our element exists
    while target > arr[e]:
        temp = e + 1 # This is my new start
        #end = previous end + (sizeOfBox)*2 (Still have a lil doubt here)
        e = e + (e - s + 1)*2 #Doubling the size of window each time exponentially
        s = temp

    return binarySearch(arr, s, e, target)


arr = [2 , 3 , 4, 7 , 11 , 17 , 21 , 27 , 41 , 69 , 74 , 81 , 105]
target = 7
print (ans(arr, target))
