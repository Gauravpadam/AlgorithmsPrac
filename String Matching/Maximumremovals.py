class Solution:
    def is_subsequence(self,s, p, removed, k):
    
        #EGO PROBLEM
        
        # Create a set of removed indices for efficient lookup
        removed_set = set(removed[:k])

        pIndex = 0
        for sIndex in range(len(s)):
            if sIndex in removed_set:
                continue

            if s[sIndex] == p[pIndex]:
                pIndex += 1

            if pIndex == len(p):
                break

        return pIndex == len(p)

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable)

        while left <= right:
            mid = (left + right) // 2

            if self.is_subsequence(s, p, removable, mid):
                left = mid + 1
            else:
                right = mid - 1

        return right

