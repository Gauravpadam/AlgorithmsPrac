class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Logic: bs question
        '''
            We've already observed, Cyclesort leaves out the indices it cannot sort
            Just exploit that property and get the answer
            You'll always find the duplicate at the end of the array, rest everything will be sorted, since there's only one element out of place, rest all belong
            That's it :/ ez
        '''
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i+=1
        
        return nums[-1] # The duplicate element will always end up at the end of the array, since the rest of the array will be sorted