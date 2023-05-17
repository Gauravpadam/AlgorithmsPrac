class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)

        # Logic: Sorting + Memoization
        '''
            Pretty straightforward approach, Logic remains the same
            *But why sort the array first?
                Because we need the overlapping elements to be adjacent to each other
            
            Process starts with maintaining an empty array & keeping a prev variable to store the previous interval

            prev = intervals[0] initially

            Keep in mind, Prev will HOLD ON to any merged interval and keep trying to merge it with the next interval as long as it keeps getting overlapping intervals, This ensures no interval if being left unmerged

            Now, Since prev = intervals[0], We start the loop from 1 to len(intervals)
            In each iteration we check for the overlapping condition:
                If prev[1]>=intervals[i][0]:
                *How is this working?
                    We simply check if the last element of prev interval is greater than or equal to the first element of the current interval, If yes, Overlap is found, IF no, No overlap exists.
                
                So,coming back to If prev[1]>=intervals[i][0]:
                    do prev[1] = max(prev[1],intervals[i][1]) # consider an example [0,5][1,4] Are they overlapping? Definitely. But what if I dont take the max of prev[1] and intervals[i][1]? Won't I be blindly merging into [0,4], which is a smaller range than the desired one? i.e. [0,5] where 5 is the 'max of the two' get it?
                
                Now what if they dont overlap?
                Easy, Just append them as is
                set prev to the current interval i.e. interval[i] and repeat the process
                See , Here prev drops the previous interval, Appends it to the result and The story of its merger ends at current interval and prev picks up the latest interval and tries to merge it with the forthcoming intervals

                And the end of the for loop prev holds on to the last intervals it could / could not merge. just append it as is

                That's it
                    
                      '''

        res = [] # Stores the result
        prev = intervals[0] # Keeps a track of previous intervals and rapidly merges upcoming intervals

        for i in range(1,len(intervals)):
            if prev[1]>=intervals[i][0]:
                prev[1] = max(prev[1],intervals[i][1]) # Selecting max range for the opverlapping interval
            else:
                res.append(prev) # Overlap not found, Append here and pick up the next interval for merging
                prev = intervals[i] # Current interval picked up
        res.append(prev) # append the remaining interval in prev
        return res
            
