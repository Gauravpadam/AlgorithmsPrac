class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1

        '''
        Logic: bs question, but good approach
        Approach for this problem:
Initialize two pointers, left and right, to the first and last indices of the input array, respectively.
While the left pointer is less than the right pointer:
a. Compute the index of the middle element by adding left and right and dividing by 2.
b. If the index of the middle element is odd, subtract 1 to make it even.
c. Compare the middle element with its adjacent element on the right:
i. If the middle element is not equal to its right neighbor, the single element must be on the left side of the array, so update the right pointer to be the current middle index.
ii. Otherwise, the single element must be on the right side of the array, so update the left pointer to be the middle index plus 2.
When the left and right pointers converge to a single element, return that element.
        '''

        while s<e:
            mid = s + (e-s)//2

            if mid%2>0:
                mid-=1
            if nums[mid] == nums[mid+1]: # No problem so far ,set s = mid + 1
                s = mid + 2 # why not mid + 1? No need of checking a pair twice, also it would cause a brutal catastrophic failure where the pair element we checked rn would be marked single as the right array will start from it and contain only a single occurence of that element
            elif nums[mid]!= nums[mid+1]: # some earlier element was single and caused a mishap on even pairs
                e = mid # why not mid - 1? what if mid was the element, you would've skipped it with mid - 1
        return nums[s] # e ans s
            

