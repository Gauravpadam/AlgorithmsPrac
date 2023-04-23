# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        s = 0
        e = mountain_arr.length() - 1

    # Proof that LEETCODE HARD IS BS
    #Logic: Find the peak element in a bitonic array using the first while loop shown below
            #After finding the peak element, Now its a simple binary search problem
            #Order agnostic binary search will work. First perform normal binary search on
            #First half of the array (s = 0 e = peak)
            #Then, Perform order agnostic binary search on second half of the array (s = peak , end = 0)
            #Additionally, There was a function call limit on mountain_arr.get() method, So we stored in a temp called val and used it instead
        while s<e:
            mid = s + (e-s)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1): #Ascending part of array
                s = mid + 1
            elif mountain_arr.get(mid) > mountain_arr.get(mid+1): # Descending part of array, Potential answer
                e = mid
                
        peak = s # setting peak value after first loop gets executed, peak = e works too

        # Performing binary search on first half of the array
        mid = 0 
        s = 0
        e = peak # denotes ending of ascending part
        while s<=e:
            mid = s + (e-s)//2
            val = mountain_arr.get(mid) # For reducing the number of calls to the function
            if target == val:
                return mid
            elif target < val:
                e = mid - 1
            else:
                s = mid + 1

        # Performing binary search on the second part of the array
        
        mid = 0
        s = peak # Denotes beginning of descending part
        e = mountain_arr.length() - 1

        while s<=e:
            mid = s + (e-s)//2
            val = mountain_arr.get(mid) # For reducing function calls
            if target == val:
                return mid
            elif target < val:
                s = mid + 1
            else:
                e = mid - 1
        
        return -1