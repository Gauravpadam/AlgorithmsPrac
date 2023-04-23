class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        e = len(arr) - 1

        '''Logic:Thiis is a bitonic array / mountain array. In this binary search 
           variation we try to find the peak element in the array. 
           To do this, Initially start end and mid are computed as usual.  
           if arr[mid+1]<arr[mid]: denotes that we have reached the descending part of the array, 
           and this hit might potentially be the answer, but who knows whether the previous element might be greater? 
           so we set e = mid (not mid - 1 as mid -1 is not to be skipped from search! it might be the greatest). 
           elif arr[mid]<arr[mid+1]: denotes that we have reached ascending part of array, and the further elements will contain the answer for sure.
           so s = mid + 1 ( not s = mid because e already know mid+1 is greater) finally both the pointers will coincide at one element,
           which will be the peak element '''

        while s<e:
            mid = s + (e-s)//2
            if arr[mid+1]<arr[mid]: #Descending part of array #Potential answer found
                e = mid
            elif arr[mid]<arr[mid+1]: #Ascending part of array #potential answer found
                s = mid + 1
        return s # or e, as both are equal
            
            