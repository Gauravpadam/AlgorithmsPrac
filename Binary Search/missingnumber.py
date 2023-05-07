class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1

        nums = sorted(nums)

        #logic:bs question
        #sort, check if range's mid == array's mid
        #if yes, everything fine uptil this point, move ahead
        #else, go left, something's missing over there
        #return s (e ans s)

        s = 0
        e = len(nums)-1

        while s<=e:
            mid = s + (e-s)//2
            if nums[mid] == mid: # good check, If range's middle equals nums middle, everything is okay upto this point, go further ahead
              s = mid + 1
            elif nums[mid] > mid: # If greater, something is missing on left, go check
              e = mid - 1
        return s # e ans s


        class Solution:
    def missingNumber(self, nums: List[int]) -> int:

      # O(N) approach
      sum1 = len(nums)*(len(nums)+1)//2

      return sum1 - sum(nums)


      # with O(N) complexity:

      '''using cyclic sort'''

    class Solution:
      def missingNumber(self, nums: List[int]) -> int:

          #Logic: bs question, cycle sort + linear search
          '''
              The first instinct that clicks after seeing a range is cycle sort
              So do that first
              In the first while loop, It's typical cyle sort with arr[arr[i]] instead of
              arr[arr[i]-1]
              *Why? Because the range is from 0 to n not from 1 to n
              Next up is the condition,
              if nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                  The latter one is cycle sort, But why the first half?
                  The first half is for handling the cases N is missing from the array.
                  This condition is checking whether the index i is a valid index for the     given array nums. If i is greater than or equal to the length of nums, then the index is out of bounds and there is no element at that index. This would cause an IndexError when trying to access the element at that index.

                  After cyclesort, perform good old search wheres we check nums[mid]==mid: again, good old condition to check if positions match and everything is clear upto that point
          binary searching wont work here, remember its leaving out nums[i] < len(nums) elements in sorting, array may or may not be sorted!
          '''
          i = 0 # setting i
          while (i<len(nums)): # cyclesort
              if nums[i] < len(nums) and nums[i] != nums[nums[i]]: # if nums[i] < len(nums), this means to check if the number at that position is less than the actual indices available for array, doesn't mean the number doesn't belong here, It's a part of the range, But the index of this number i.e. its placeholder is missing due to that one missing number in the array, So best thing, dont place this number place others and this will reach its destination
                  temp = nums[i]
                  nums[i] = nums[nums[i]]
                  nums[temp] = temp
              else:
                  i+=1

          #searching
          #Case 1: A middle element is missing
          for i in range(0, len(nums)):
              if nums[i]==i:
                  continue
              else:
                  return i
          #Case 2: The last element is missing
          return len(nums)

          
          
        


