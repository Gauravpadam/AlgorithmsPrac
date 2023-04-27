class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1

        nums = sorted(nums)

        #logic:bs question
        #sort, check if range's mid == array's mid
        #if yes, everything fine uptil this point, move ahead
        #else, go left, something's missing over there
        #return s (e ans s)

        s = 0
        e = len(nums)-1

        while s<=e:
            mid = s + (e-s)//2
            if nums[mid] == mid: # good check, If range's middle equals nums middle, everything is okay upto this point, go further ahead
              s = mid + 1
            elif nums[mid] > mid: # If greater, something is missing on left, go check
              e = mid - 1
        return s # e ans s


