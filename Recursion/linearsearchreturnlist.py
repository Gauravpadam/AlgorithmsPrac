arr = [5,7,11,21,3,2,5,3,5]

# Recursion tree

'''
                                 findallindex(arr, 5, 0, [])
                                     /         \
                                    /           \
                                   /             \
             findallindex(arr, 5, 1, [])      findallindex(arr, 5, 1, [0])
                     /         \                          /        \
                    /           \                        /          \
                   /             \                      /            \
findallindex(arr, 5, 2, [])  findallindex(arr, 5, 2, [0])  findallindex(arr, 5, 2, [0])
        /         \                /           \                    |
       /           \              /             \                   |
      /             \            /               \                  |
...                    ...     ...               ...       findallindex(arr, 5, 8, [0, 6, 8])
                                                   |              /         \
                                                   |             /           \
                                                   |            /             \
                                                ...             ...           ...

'''


def findallindex(arr, target,index, nums):
    if index == len(arr):
        return nums
    elif arr[index] == target:
        nums.append(index)
    return findallindex (arr,target,index+1,nums)

res = findallindex(arr,5,0,[])

print (res)

    


