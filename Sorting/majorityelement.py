class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = set()
        maxc = -1
        target = -1

        # Logic: Bruteforce logic
        # Pretty self explainatory
        for i in range(len(nums)):
            if nums[i] not in seen and nums.count(nums[i])>maxc:
                maxc = nums.count(nums[i])
                target = nums[i]
                seen.add(nums[i])
        
        return target

        # Optimized logic: Sorting
        '''
            Hidden key to identify here:
            "The majority element is the element that appears more than ⌊n / 2⌋ times."
            So, Won't the central array element always be an occurence of the majority element?
            That's it, question gone :)
        '''
        
        nums = sorted(nums)

        return nums[len(nums)//2]
