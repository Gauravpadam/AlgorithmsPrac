class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        
        nums = sorted(nums)
        if nums[0] == 0: # If first element is 0, return 0 straightaway (SPECIAL CASE OF ALL ZERO ARRAY!)
            return 0

        # Handling single number cases explicitly
        if len(nums) == 1:
            if abs(nums[0]) == nums[0]: # positive integer
                return 1
            else: # negative number
                return -1 

        #Logic: bs question, Interesting approach
        # Just look for the last occuring negative element
        # Take len of aray from 0 to s, i.e. last negative element
        # modulo it by 2, i.e checking if even no. of negatives are present
        # If yes, Return 1, since product will be positive
        # if any 0 is spotted, return 0, before bs only
        # else, return -1 if odd negatives present

        def check(nums): # checks for last occurence of negative number
            s = 0
            e = len(nums) - 1
            result = -1
            while s <= e:
                mid = s + (e - s) // 2
                if nums[mid] < 0:
                    result = mid # set result & look further
                    s = mid + 1
                else:
                    e = mid - 1 # Look back
            return result

        val = check(nums) # Calling helper function

        if val == -1:  # Result stays -1, no -ve found, product will be positive
            return 1
        else: # Something has changed
            if nums[val+1]==0: # Check for an immediate zero, If yes ,ret 0, as product will be 0
                return 0
            else:
                if len(nums[0:val+1])%2 > 0: # Modulo of length of array from 0 to last occurence , if odd, product is -ve, return -1
                    return -1
                else: # Found even? Product will be positive
                    return 1



        