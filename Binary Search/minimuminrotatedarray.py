class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        pivot = -1 # Why not pivot = 0?
                    # Interesting, what happens when an array contains two elements and     it  is rotated once eg. [2,1]
                    #e > mid and nums[mid]>nums[mid+1]: is executed
                    #it marks pivot = mid, which in this case is ZERO
                    #what happens next? code sees pivot == 0? return nums[0]
                    #Code returns 2 which is not the minimum element
                    #Thus, The actual purpose of setting pivot = 0 , i.e. to indicate a normal unrotated array is destroyed
                    #To fix this problem, set the pivot to such a value which can never occur, any is fine, not necessarily pivot = -1

        #Logic: bs question, just find pivot, immediate next element is the minimum
        #if no pivot, array is norammly sorted, return nums[0]

        while s<=e:
            mid = s + (e-s)//2

            print (mid)
            if e > mid and nums[mid]>nums[mid+1]:
                print ("Im in boss")
                pivot = mid
                break
            elif mid > s and nums[mid-1]>nums[mid]:
                pivot = mid - 1
                break
            elif nums[s] >= nums[mid]: # Pivot happened somewhere in this range, look in this range
                e = mid - 1
            elif nums[s] < nums[mid]: # Pivot never happened in this range, look ahead
                s = mid + 1
        
        print (pivot)

        if pivot == -1:
            return nums[0]

        return nums[pivot + 1]
