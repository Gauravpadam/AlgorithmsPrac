class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x

        #Logic: bs question
        #each time, calc val
        #checkif val == x: , for perf squares might be true
        #else if val > x: Too far, answer lies in e = mid - 1
        #else val < x: answer beyond this range, s = mid + 1
        #At last when nothing found, e ans s is the format
        #therefore, floorval is our answer

        while s <= e:
            mid = s + (e - s) // 2
            val = mid * mid

            if val == x: #A perfect square match
                return mid
            elif val > x: #Reduce search space by e = mid - 1
                e = mid - 1
            else: # Answer is beyond s = mid + 1
                s = mid + 1

        return s - 1 # Return floor value always, i.e. a match was not found, but return floor
