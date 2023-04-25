# bs question

nums = [[2,4,6],[71,1,2],[7,2,33,22,3,88,777,88]]
key = 7

def search(nums, key):
    for arr in nums: # Dig into 2D
        for num in arr: # Dig into 1D
            if num == key:
                return True
            else:
                continue
    return False

print(search(nums,key))