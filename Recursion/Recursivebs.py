nums = [1,2,3,4,7,11,21,33]
target = 0

def binarysearch(nums,target,s,e):
    if (s>e):
        return -1
    mid = s + (e-s)//2

    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return binarysearch(nums,target,s,mid-1)
    else:
        return binarysearch(nums,target,mid+1,e)

print (binarysearch(nums,33,0,len(nums)-1))