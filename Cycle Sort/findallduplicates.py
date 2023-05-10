class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        #Logic : cyclesort & linear, thats it :/
        '''
            1-n range, 1 ranged cyclesort, check nums[i] != nums[nums[i]-1]
            Cyclesort's property exploitation and question over :/
            Cyclesort will throw all elements which dont belong in the sequence of the array where their indexes wont match nums[i] = i+1 property
            Seek such numbers using linear and return result
            That's it
        '''

        i = 0
        while i < len(nums):
            if nums[i]!=nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i+=1
                
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
        
        return res
            