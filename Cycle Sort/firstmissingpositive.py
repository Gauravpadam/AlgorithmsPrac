class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Logic: The only reason this is flagged "Hard" is there is no range provided, Making it upto your intuition to see the cyclesort hidden in it, Once you see it, It's the most bs question in mankind's history xD

        #This is literally the copy pasted code of missing numbers

        i = 0
        while i < len(nums):
            if nums[i]>0 and nums[i]<=len(nums) and nums[i] != nums[nums[i]-1]: # Checking if nums[i]<=len(nums) and avoiding any negatives
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i+=1
        print (nums)
        for i in range(len(nums)):
            # case 1
            if nums[i]!=i+1: # eg . [1,2,0], 3 is missing, check for 1+1 till 0 found, 0 is misplaced and occupies 3's position
                return i+1
        #case 2
        return len(nums)+1 # If everything is sorted, N+1 is missing
