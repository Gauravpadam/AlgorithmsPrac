class Solution:
    def findKRotation(self,nums,  n):
        s = 0
        e = n - 1
        pivot = -1
        
        
        while s<=e:
            mid = s + (e-s)//2
            if (mid < e and nums[mid]>nums[mid+1]): # mid < end as we check mid + 1, which can cause out of bounds error
                pivot = mid
                break
            elif (mid > s and nums[mid-1]>nums[mid]): # Here we are returning mid - 1, thus we need to check start > mid else out of bounds error
                pivot = mid - 1
                break
            if nums[mid] <= nums[s]: # This means pivot occured somewhere in this range, set e = mid - 1 to search this range further
                e = mid - 1
            elif nums[s] < nums[mid]: # This means pivot lies outside this range as the ascending order still follows, set s = mid + 1 to look outside this range
                s = mid + 1
                
        if pivot == -1:
            return 0
            
    
        
        return pivot + 1