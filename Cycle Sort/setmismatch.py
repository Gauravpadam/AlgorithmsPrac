class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # Logic: Cycle sort's property exploitation
        '''
            Think about this,
            If a number is in the wrong index, it will be occupied by a duplicate number
            Here, if nums[i] is at the wrong index, i+1 is missing from the array!
            Similarly, if nums[i] is at the wrong index, that means it is the duplicate element occupying the position of i+1

            For eg:
            Take an array [1,2,2,4]
            Here 3 is the missing element,
            And the duplicate occupies its position
            
            That's it, question over :|
        '''
        i = 0
        while i < len(nums): # Cyclesort
            if nums[i]!=nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i+=1
        
        for i in range(len(nums)): # Hit the wrong index
            if nums[i]!=i+1:
                return [nums[i],i+1]