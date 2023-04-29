class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1 # What's the slowest she can eat? 1 banana
        e = max(piles) # what's the fastest she can eat? max bananas, why not more?
                        # She chooses on pace of piles! max pace = max(piles)
        
        # Logic: Interesting approach, bs question
        '''
            In this question, Dangling speed search, rather than array binary search occurs
            speed ranges from 1 banana per hour to max. value of piles banana per hour
            In this speed range lies our optimum & minimum eating speed
            #1 Initiate binary search
            #2 calc mid
            #3 calculate the total no. of hours required for eating at current speed (mid) to finish all bananas i.e. sum(Math.ceil(pile / mid) for pile in piles)
            *Why ceil?*
            - Because she will take the complete hour after finishing a pile, as mentioned she wont eat anything after a pile is over for that hour
            #4 If calc hours > h: eating too slow, hurry up, s = mid + 1
            #5 If calc hours < h: slow down, ate too fast, not the minimum value, e = mid
            #6 Return s, as s contains miniumum eating speed required

        '''
        while s<e:
            mid = s + (e-s)//2

            total_hours = sum(math.ceil(pile / mid) for pile in piles) # Calculating the total eat time for the current speed
            if total_hours > h: # If eating takes more time than the guards show up
                s = mid + 1
            else: # If eating is too fast, this is NOT the minimum value we are looking for
                e = mid
        return s # This is the minimum value koko can eat at
        
