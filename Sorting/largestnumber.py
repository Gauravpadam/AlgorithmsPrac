class LargerNumKey(str):
    def __lt__(x,y):
        return x+y > y+x # Operator overloading for transitivity check


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums = list(map(str, nums)) Rather do it in a single line as shown below
        # nums = list(reversed(sorted(nums))) This wont work!

        # What's the logic here?
        '''
            Logic begins from mapping the int array into string
            * Why compare strings?
                Because we need to calculate if transitivty is valid, Or simply understand
                For example, if the input is [3, 30, 34, 5, 9], we need to compare the strings "3", "30", "34", "5", and "9" in order to determine that the largest number that can be formed is "9534330".

            Also, This is a problem where we overload the operator '>'
            Comparator normally returns x when x > y

            But this time we work in pairs, We check if transitivity is applicable and then only return if x + y > y + x

            The class LargestNumKey checks if x + y > y + x and returns the result to append accordingly

            If it begins from 0, straighaway scrap it since no greatest no. begins from 0 and this can only mean that a array of 0's is given in input
        '''

        largest_num = ''.join(sorted(map(str, nums), key = LargerNumKey)) # mapping & sorting, checking which is larger x+y or y+x, each time x and y moves forward till the end of nums
        return '0' if largest_num[0] == '0' else largest_num # largest num cannot start with a 0