class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = 0
        e = len(nums) - 1
        res = [-1,-1]

        #Logic: To find the first and last occurences, Use binary search twice
                #In first passthrough , When a potential answer is hit, set res[0] = mid
                #and e = mid - 1
                #This starts binary search in the left part of the array and searches for
                #The first occurence
                #Similarly, Start another binary search, let it hit a potential match again
                #set res[1] = mid and s = mid + 1 this time for the last occurence in the
                #right part of the array

        while (s<=e):
            mid = s + (e-s)//2
            if target < nums[mid]:
                e = mid - 1
            elif target > nums[mid]:
                s = mid + 1
            else:
                #Searching for the first occurence here
                res[0] = mid # Set the val inside, but why?
                e = mid - 1

        s = 0
        e = len(nums) - 1

        while (s<=e):
            mid = s + (e-s)//2
            if target < nums[mid]:
                e = mid - 1
            elif target > nums[mid]:
                s = mid + 1
            else:
                #Searching for the last occurence here
                res[1] = mid # Set the val inside, not after while loop, but why?
                s = mid + 1


        return res