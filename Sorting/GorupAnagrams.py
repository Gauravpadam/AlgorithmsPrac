class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagram_dict = {}

      # Logic: Sorting + Hashmap
      '''
        In this problem, We have to sort the word and mantain a hashmap for it
        For this, We initialize a Hashmap "anagram_dict{}"

        Now, next step is the looping logic
        for each word in strs, We tend to create a sorted key entry in the hashmap
        Then, We will add all the values corresponding to these sorted entries in the value pair of that key entry

        So, step 1:
        sorted_word = ''.join(sorted(word)) # This sorts the string

        Step 2:
        if sorted_word not in anagram_dict: # Checks if there's already a key entry for the sorted word in the hashmap
        If yes, Skip below line, If no, execute it
          anagram_dict[sorted_word] = [] # This creates a new key entry for the sorted word alongwith an empty value array

        Step 3:
          Now, anagram_dict[sorted_word].append(word)
          Keep in mind that if there's already a sorted_word entry for the current word, This word CORRESPONDS to that sorted entry, i.e. This word is an ANAGRAM to the sorted word

          That's' it, Append it to the value array of corresponding sorted_word

          At last, We needed a list of anagrams. The list of anagrams is the list of all value pairs of the dictionary, So in short we are returing a "list of , list of anagrams"
      '''

      for word in strs: 
        sorted_word = ''.join(sorted(word)) # sorting the word
        if sorted_word not in anagram_dict: # checks if curr word exists as key in dict
          anagram_dict[sorted_word] = [] # appending as key if does not exist
        anagram_dict[sorted_word].append(word) # The word alreay had its corresponding sorted entry, This means it is an anagram, So, Append it to the corresponding sorted word entry
      
      return list(anagram_dict.values())