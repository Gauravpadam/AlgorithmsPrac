class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        e = math.ceil(num/2) # Basic logic, perfect sq. exists in half a range than num

        #Logic: bs question
        #set range 1 - num
        # if mis*mid = num then true
        #elif > num then mid is too big, lower the range
        #else mid is too small, higher the range

        while s<=e:
            mid = s + (e-s)//2

            if mid * mid == num: #found it
                return True
            elif mid * mid > num: #greater than num, lower the range
                e = mid - 1
            else: # make range higher
                s = mid + 1
        return False # not found


