class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #Logic: The main work here is finding the pivot, rest is bs
        #To find pivot, Check four conditions:
        #1. if (mid < e and nums[mid]>nums[mid+1]): This means mid is the pivot
        #2. elif (s > mid and nums[mid-1]>nums[mid]): This means mid - 1 is the pivot
        #3. elif s > mid: This means pivot occured somewhere in this range, set e = mid - 1 and try to catch it in next iteration
        #4. elif s <= mid: This means pivot never occured here, It's outside this range, set s = mid + 1 and try to catch it in next iteration

        #After  pivot is found, Perform normal binary search on both the halfs of the array

        s = 0
        e = len(nums) - 1
        pivot = -1 # Hard setting pivot so that it denotes pivot not found later

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

         #If pivot is still = -1, i.e. If no pivot exists, i.e. Array not rotated

        if target == nums[pivot] and pivot!=-1 :# pivot!=-1 specifically for python users, as python reads nums[-1] as array element
            return pivot
        
        elif pivot == -1: # Normal binary search

            s = 0
            e = len(nums) - 1
            while s<=e:
                mid = s + (e-s)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1

            return -1

        
        elif target >= nums[0]:  # Searching in the first part of array, Coz we know target > s, and after pivot all elements < start, Thus pivot - 1
            s = 0
            e = pivot - 1
            while s<=e:
                mid = s + (e-s)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1

            return -1
        
        elif target < nums[0]:  # Searching in the second part of array, If < nums[0]
            s = pivot + 1
            e = len(nums) - 1
            while s<=e:
                mid = s + (e-s)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1

            return -1