# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

#Logic: Guesswork is same as getting a target, rest is bs

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n
        while s<=e:
            mid = s + (e-s)//2
            val = guess(mid) # For reducing function calls
            if val==0:
                return mid
            elif val == -1: # Number is higher, go lower
                e = mid - 1
            else: # Number is lower, go higher
                s = mid + 1
