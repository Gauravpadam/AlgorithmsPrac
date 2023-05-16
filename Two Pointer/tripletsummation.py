class Solution:
    def tripletsummation(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        #Logic: Two pointer approach + Sorting
        '''
            This problem asks to find triplets which sum up to 0
            For this purpose, We follow a two pointer approach
            Firstly, loop from 0 to len(nums)
            set left=i+1 & right=len(nums)-1
            Now, while left < right : (This condition ensures all elements are checked)
                if nums[i] + nums[left] + nums[right] = 0:
                    add them to the set as a tuple
                    *Why set? To avoid duplicates / permutations
                    if sum < 0, This means the left val is too small (How do we know? The array is sorted,That's how) so, left+=1
                    elif sum > 0:
                        right val is too large(Don't ask how do we know again -_-)
                        do right-=1
                    AND keep repeating the summations till left < right
                    Once it exits the while loop, All possible cases were checked and set s contains our answers from this iteration

                    Now, let the for loop do its job for every array element

                    That's it, Done


        '''
        s = set()
        sum = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    s.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1

                elif sum < 0:
                    left+=1
                else:
                    right-=1
        return s
