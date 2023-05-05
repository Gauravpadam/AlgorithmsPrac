class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'} # Hashmap

        #Logic: BS question, Sliding window
        # Since python strings are immutable, use list() or dynamic arrays, or dont if you're a badass x)
        # First step is to set a window for checking, Here s[:k] is the window size
        #loop through the first window, get count, set answer
        #start from k now, add one count if s[i] in vowels, delete one if i-k ( The removed element from window was a vowel)
        count = 0 # Initializing count
        for i in range(k): # s[:k] window
            count+=int(s[i] in vowels) # Typecasting T and F into 1 and 0
            answer = count # The initial window contains 'count' number of vowels

        for i in range(k,len(s)):
            count+=int(s[i] in vowels) # You just got a vowel
            count-=int(s[i-k] in vowels) # You kicked a vowel out of window, i-k is the removed element from the window (duh)
            answer = max(count, answer) # comparing with the first window, technically the max window everytime its set

        return answer

        