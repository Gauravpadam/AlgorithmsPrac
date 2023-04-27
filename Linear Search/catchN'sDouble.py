class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        #Bruteforce

        for num in arr:
            print (num)
            for i in range(0,len(arr)-1):
                if num == 0 and arr.count(0)==1: #Skipping idle zeros
                    num+=1
                elif arr[i]==num*2:
                    return True
        return False