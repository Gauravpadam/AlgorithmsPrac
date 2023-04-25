class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        s = 0
        e = 0

        # Logic: Good question.
        #First try to find the minimum and maximum possible sum values out of the array given
        #This forms the ranges for binary search
        #Then in this range, mid is your potential ans
        #Try to make pieces as per mid allows
        '''     for num in nums:
                if (sum + num > mid):
                    pieces+=1
                else:
                    sum+=num '''
        # See above conditions, They make pieces according to the mid
        # If mid is too small, s = mid + 1
        # If too large, e = mid - 1
        # return s or e, both point at final answer of sum

        
        for i in range(len(nums)):
            s = max(s, nums[i]) # Basic linear search, gives maximum element of array
            e+= nums[i] # Gives max array sum
            
        #Binary search
        while s<e:
            #try for mid as the potential ans
            mid = s + (e-s)//2

            #calc how many pieces you can divide into with this max sum
            sum = 0
            pieces = 1 # initially
            
            for num in nums:
                if (sum + num > mid): # You cannot add this into this subarray, make new one
                    sum = num # New subarray, sum = num,pretty self explainatory
                    pieces+=1
                else:
                    sum+=num
            if pieces > k: # If count of pieces is greater than asked, It means mid we calculated is too small to accomodate true answer
                s = mid + 1 
            else:  # If smaller than asked, It means mid we calculated is too large to accomodate true answer
                e = mid
        return e # or start, start = end