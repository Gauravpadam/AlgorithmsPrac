# As the name suggests, its cycle sort

'''
    gist: # When is it applied?
                When given a range from 1 to N, DEFINITELY apply cycle sort!

          # What's the big idea?
                Cycle sort compares and swaps, however it's different from others
                In cycle sort, We know the correct indices of elements as a RANGE of elements is provived

          #  What does that mean?
                Consider a range 1 to 5, And now consider the provided elements for eg. 4 , 2 , 3 , 1 , 5
                For each number we know the index to which it belongs
                4 belongs to index no 3
                2 belongs to index 1 i.e correct
                3 belongs to index 2 i.e. correct
                1 belongs to index 0
                5 belongs to index 4 i.e. correct
         
          # Set a while loop, till correct index is not matched keep swapping
          # That's it, Cycle sort ladies and gentleman

          # Complexity of 2N - 1 but O(n) 2N for swapping, -1 for the leftover correct position element

'''


def cyclesort (arr):
    print(arr) # Before
    i = 0
    while (i<len(arr)):
        if arr[i]!=arr[arr[i] - 1]: # Sorting begins here! arr[i] - 1 is the correct index, This is why python SUCKS negative indexing applies here, so in python use arr[i] instead of arr[i] - 1
            temp = arr[i]
            arr[i] = arr[arr[i]-1]
            arr[temp-1] = temp # Dont use arr[arr[i]-1], use temp instead, Why? see the line above it
        else:
            i+=1 # Increment only after sorting every element that comes our way, then pass through the array   

    return arr
print (cyclesort(list(range(11,0,-1))))
