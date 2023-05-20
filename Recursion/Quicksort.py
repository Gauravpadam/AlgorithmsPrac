def quicksort(arr, low , high):
    if (low>=high): # Single element case, Return as is
        return

    s = low
    e = high
    mid = s + (e-s)//2
    p = arr[mid]

    while s <= e:
        
        # Wont swap if its already sorted
        while arr[s] < p: # Left half < pivot? Good, keep going and find the violation
            s+=1
        while arr[e] > p: # Right half > pivot? Good, keep going and find the violation
            e-=1
        
        # Violation found, Swap now
        if (s<=e): # Swap only after checking if its the breaking condition
            arr[s],arr[e] = arr[e],arr[s]
            s+=1 # Check the next lot
            e-=1 # Check the next lot

    # Now our pivot is at correct index, sort the other two halves now
    quicksort (arr, low , e)
    quicksort (arr, s , high)
        
arr = [5,4,3,2,1]
quicksort (arr, 0 , len(arr)-1) # Call to sort the arr
print (arr) # Sorted arr