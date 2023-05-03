class Solution:
    def captureForts(self, forts: List[int]) -> int:

        # Logic: Bruteforced AF
        # Basically slice the array into subarrays and just see the below conditions, avoid any mishaps or you're dead

        subarrays = [] # Stores potential answers
        for i in range(len(forts)):
            if forts[i] == 1: # Starts from a 1
                for j in range(i+1,len(forts)):
                    if forts[j] == -1: # Looks for a closing -1
                        subarrays.append(forts[i+1:j])
                        break # Break as soon as appended
                    elif forts[j] == 1: # Annoying edge case is to be kicked immediately
                        break
            elif forts[i] == -1: # Starts from -1
                for j in range(i+1,len(forts)):
                    if forts[j] == 1: # Looks for an immediate closing 1
                        subarrays.append(forts[i+1:j])
                        break # Break as soon as appended
                    elif forts[j] == -1: # Cannot be travelled, boot immediately
                        break

    # Result generation 
        maxlen = 0

        if len(subarrays) == 1 and len(subarrays[0]) == 0: # Checks for 0 result
            return 0

        for arrays in subarrays:
            if len(arrays)>maxlen: 
                maxlen = len(arrays) # Select the maximum len subarray
        
        return maxlen # Return

        