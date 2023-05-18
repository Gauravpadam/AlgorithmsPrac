class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #Logic : bs qtn
        '''
            When sorted, max values are last two values
            as per req, ret max of (nums[i]-1)*(nums[j]-1)
            i.e. max of last two vals - 1 each
        '''
        nums = sorted(nums)
        return ((nums[-1]-1)*(nums[-2]-1))