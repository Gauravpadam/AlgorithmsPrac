class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Logic: bs prob
        '''
            At s[indices[i]] you shall place s[i]
            That's it 
        '''

        result = [''] * len(s)  # Create a list to store the characters in the correct order
        for i in range(len(s)):
            result[indices[i]] = s[i]  # Place each character at its corresponding index

        return ''.join(result)  # Convert the list back to a string