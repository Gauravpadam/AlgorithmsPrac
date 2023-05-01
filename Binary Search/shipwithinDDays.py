class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check (max,arr,days): # Code to check if mid capacity can be used to deliver within given days
            currentCapacity = 0 # current load
            no_of_days = 1 # starting from day 1

            for i in arr:
                currentCapacity+=i # Start loading
                if currentCapacity > max: # capacity limit hit
                    no_of_days+=1 # Load the next day
                    currentCapacity = i # This much is already sent the previous day
                if no_of_days > days: #At the end, If it took more days to send, the load we found through binary search was too big, Let's reduce the load and try again
                    return False
            return True # The load we found was able to be shipped, lets try to make it minimum in our bs section


        s = max(weights)
        e = sum(weights)

        '''
            Logic: bs question, Interesting approach
                This problem can be solved using binary search. We know that the weight capacity of the ship must be between the maximum weight of any single package and the sum of all package weights. We can perform a binary search on this range of possible capacities, and for each capacity, check whether it is possible to ship all the packages within the given number of days.
                To check whether a given capacity is feasible, we can simulate the loading of the ship day by day. Starting from the first package, we add packages to the current day's load until we reach the capacity limit. Once we reach the limit, we move on to the next day and repeat the process. If we are able to load all packages within the given number of days, then the capacity is feasible.

        ** By initializing s as max(weights), we are setting the lower bound of the search space as the weight of the heaviest package. This is because if the weight capacity of the ship is less than the weight of the heaviest package, then it is impossible to deliver that package in a single day, and we need to increase the weight capacity of the ship.

          In summary, by setting s as max(weights), we are ensuring that we do not waste any time searching for weight capacities that are less than the weight of the heaviest package, which is a requirement for the packages to be delivered in the given number of days.

          Setting e =sum(weights) was easy, It means that max capacity can deliver the shipment in one day itself, althought we dont want that, It helps in setting an upper bound.
          Our goal is to minimize this upper bound
        '''

        #total_weight distributed in days
        #Min weight capacity = s = max(weights)
        #Max weight capacity = e = sum(weights)
        #Minimize weight capacity and deliver everything
        #send packages in order ONLY

        while s<e:
            mid = s + (e-s)//2

            if check(mid,weights,days) == True: # check if curr weight can be shipped feasibly
                e = mid
            else: # If not, make the search go s = mid + 1
                s = mid + 1
        return s # s is the minimum



