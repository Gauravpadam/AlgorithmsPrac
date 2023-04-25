class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        maxsum = -1

        #Logic: bs question
                #Set maxsum for each loop
                #Return maxsum
                
        for customer in accounts:
            for bank in customer: 
                sum = sum + bank
            maxsum = sum if sum > maxsum else maxsum
            sum = 0 # Resetting sum for next customer
        return maxsum
