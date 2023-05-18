class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        #Logic: bs qtn
        '''
            Not even worth explaining :/
        '''

        # Bruteforced approach
        res = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            res.append(count)
            count = 0
        return res

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # Optimized approach : Sorting + Hashmap
        '''
            In this approach, use a counts hashmap
            Create a copy of curr array and sort the copy
            Now we have one to keep the order of output ( The og one) and one to simply get the smaller nums than the current nums

            Initiate the first loop
            if numscopy[i] in counts.keys():
                *Why this?
                Take a case , nums = [1,2,2,3,8]
                How many elements smaller than 2? 1 right?
                I'm marking i elements as smaller always
                So hear me out genius, Won't the second occurence of 2 change the value of smaller elements to i=2 i.e 2?
                This makes it necessary to consider each occurence only one, and how do we do it? continue keyword (basic looping go learn bruh)

                Now we have all counts, Only thing is to put the counts somewhere in ORDER,
                Here's where we use the og nums
                for i in range(len(nums)):
                    numscopy[i] = counts.get(nums[i])
                    *why get nums[i]?
                        It'll fetch the counts in required order, If I make it numscopy[i], It'll give sorted output (sorted array, duh -_-)

                That's it, Done

        '''
        
        counts = {} # Hashmap

        numscopy = sorted(nums) # Sorting & cloning

        for i in range(len(numscopy)): # Inserting keys into hashmap
            if numscopy[i] in counts.keys(): # We only want the first occurences of duplicate elements to be targeted
                continue
            else:
                counts[numscopy[i]] = i # Current pos = No.s smaller than current val (Sorted arr, duh -_-)

        for i in range(len(nums)): # Just transferring counts to numscopy
            numscopy[i] = counts.get(nums[i]) # Counts of nums[i] getting transferred
        
        return(numscopy)



        

