class Solution:
    def heightChecker(self, nums: List[int]) -> int:

        temp = sorted(nums)

        #Logic: Dont even ask -_-

        count = 0

        for i in range(len(nums)):
            if temp[i]-nums[i] != 0:
                count+=1
        return count