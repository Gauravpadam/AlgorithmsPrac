class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        #Logic: bs prob
        '''
            Simple two pass and return merger in one line
            [x for x in nums if x%2==0] finds out all evens
            [x for x in nums if x%2>0] finds out all odds
            add both lists and return, That's it :/


        '''

        return ([x for x in nums if x%2==0]+[x for x in nums if x%2>0])