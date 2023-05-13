class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        #Logic: Apply any sort in your knowledge, I used bbsort
        """


        for i in range(len(nums)):
            flag = 0
            for j in range(len(nums)-i-1):
                if nums[j]>>nums[j+1]:
                    (nums[j],nums[j+1]) = (nums[j+1],nums[j])
                    flag = 1
            if flag == 0:
                    break
        