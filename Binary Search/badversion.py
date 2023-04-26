# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

    #Logic: Okay, We need the first bad version, bs qustion btw
    #For this we can store the bad versions we encounter during binary search
    #once hit, e = mid - 1 and store this version in a variable
    #So, The first time you encounter a version, you store it
    #then immediately go mid - 1 to search for earlier versions
    
        s = 1
        e = n
        version = 0


        while s<=e:
            mid = s + (e-s)//2
            val = isBadVersion(mid) # To reduce function calls
            if val == True:
                version = mid
                e = mid - 1
            elif val == False:
                s = mid + 1
        return version