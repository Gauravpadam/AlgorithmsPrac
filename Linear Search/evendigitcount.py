class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counteven = 0
        countdigit = 0

        #Logic: bs question
                #Iterate over all numbers
                #Set a number into temp and keep dividing it till it becomes 0
                #Meanwhile this happens, digitcount+1 on each division
                #Now modulo digitcount by 2, if 0, counteven + 1
                #Reset digitcount on each iteration to 0

                #(Another approach would be str conversion and taking length)

        for i in range(len(nums)):
            temp = nums[i] # Just so to not mess up the original array by dividing

            if nums[i] < 0:
                nums[i] = nums[i] * -1 # Edge case: negative

            while temp>0:
                temp = temp//10 # Dividing to reduce digits by one position at a time
                countdigit+=1 # Increasing digit count
            if countdigit % 2 == 0:
                counteven+=1
            countdigit = 0 # Resetting digitcount

        return counteven
