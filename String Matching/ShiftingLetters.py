class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ""

        # logic: terrible, anti-positional, incredible
        '''
            Instead of going with the approach of modifying multiple characters at once by bruteforcing, we first compute the number of shifts of each character

            The question states "Suppose We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc"."

            To optimize our approach, we calculate shifts for all characters, Once that is done, Its just shifting each character by that much ascii value

            Firstly, Store first shift value in prevsum
            prevsum = shifts[0]
            We know intuitively that sum of all shifts will be applied on first element, So do that. i.e. shifts[0] = sum(shifts)

            We run a loop now from 1 to len(shifts)-1, because last and first element remains unchanged
            At the end of each loop we shall calculate the sum of previous elements
            *Why?
            Total sum of shifts - Shifts of previous elements's shifts = Current elements's shifts
            For this, before modifying current shift value, store it in temp
            Then do shifts[0] - prevsum
            and then, prevsum = prevsum + temp

            That's it, Now you have all shifts

            Just perform the shifts inside a loop for each string character
              for i in range(len(s)):
                res = res + chr((((ord(s[i])+shifts[i])-97)%26)+97) # For keeping the value between 97 to 122

            That's it, Done :coinflipper:
            


        '''

        prevsum = shifts[0] # Initially, prevsum = shifts[0]
        shifts[0] = sum(shifts) # summing up all shifts in 0th element

        for i in range(1,len(shifts)-1):
            temp = shifts[i]
            shifts[i] = shifts[0] - prevsum # Computing each shift by subtracting sum of all shifts by sum of prev shifts
            prevsum = prevsum + temp # storing sum of prev shifts

        

        for i in range(len(s)):
                res = res + chr((((ord(s[i])+shifts[i])-97)%26)+97)
                
        return res



        





