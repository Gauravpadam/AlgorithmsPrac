class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Logic: bs question, Cycle sort & Linear search will finish this
        '''
            Same as finding a single missing number
            I shouldn't be explaining this :/
            Okay,
            #1: Cyclesort over all given things
            #2: nums[i]-1 is the correct index this time
                * Why? Because this is a range of 1 to n, The correct place is at -1 the index, ponder over it
            #3: Search linearly, wherever nums[i]!=i+1 (again, 1 to n based range thats why i+1, not i)
            #4: Append all those numbers in array & return it

            If you think about this, print the array once, You'll find that cyclesort is not sorting the array completely ;)
            We're just filtering out indices which cannot be sorted and likewise predicting the missing elements
        '''
        
        res = []
        i = 0
        while i<len(nums): # Cyclesort
            if nums[i] != nums[nums[i]-1]: # Basic cyclesort condition
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i+=1
        # Searching
        for i in range (0,len(nums)):
            if nums[i]!=i+1: # i+1 is due to 1 to n range, the correct element at ith position will always be i+1, for eg. at 0 there should be 1, at 1 there should be 2 and likewise
                res.append(i+1) # append if found guilty

        return res
