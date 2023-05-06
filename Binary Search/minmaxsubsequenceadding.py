class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        #binary search, find the range that has minimum and maximum <=9
        l = 0
        r = len(nums)-1
        mod = 10**9+7

        def binary_search(l, r, nums, target):
            #Need to find where target - nums[0] is in the array. 
            #Need to find the right boundary

            #Using the ultimate template
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] == target:
                    l = mid + 1
            #Do not need to do edge case check. Because it will be done in the for loop below
            return l-1
        
        res = 0
        for l in range(len(nums)):
            if nums[l]>target:
                break #if the smallest number being checked is already larger than target, there is no chance for getting a meaningful r2 to build subsequences that satisfy the requirement
            r2 = binary_search(l, r, nums, target-nums[l])
            if r2>=l:
                res += pow(2, r2-l, mod)# Note, if we find [2, '3', 4, 5, 6, 7, '8'] ('x' means left and r2, respectively), for the l==3, any subsequence including 4 to 8 (5 numbers) satisfy the requirement. Thus, it is r2-l, because there are this many numbers (5 numbers in this example)
        return res % mod