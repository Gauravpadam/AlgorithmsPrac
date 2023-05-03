class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        #Daily bs questions 

        #Logic: Not even worth explaining :/

        res = [[],[]] # Return sets for only single values

        for nums in nums1: # First loop for a not in b
            if nums not in nums2:
                res[0].append(nums)
        
        for nums in nums2: # Second loop for b not in a
            if nums not in nums1:
                res[1].append(nums)
        
        return res # Return list
        
        

        
        
