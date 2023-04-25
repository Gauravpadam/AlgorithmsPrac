# bs question

nums = [1 , 2 , 11 , 7 , 64 , 31 , 17]
minval = 999999 # some unfathomable number

for i in range(len(nums)):
    minval = min(minval, nums[i]) # bruteforcing af

print (minval, " With lib func")

# without using a lib, still bs

minval = 999999

for i in range(len(nums)):
    if nums[i]<minval:
        minval = nums[i]
    else:
        continue

print (minval," Without lib func")