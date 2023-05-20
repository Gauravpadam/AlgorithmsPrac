class Solution:
    def tripsetsummationclosest(self, nums: List[int], target: int) -> int:
        # Logic: Good prob, Sorting + Two pointer approach

        '''
            This is a close variation of tripletsummation, But with a target
            Our aim is to get the sum as close as possible to the target
            How can we do it? Minimum absolute differences between target and sums
            * Why abs(differences)? 
                Because we are concerned with the magnitude of difference, Not the sign
                Take for eg. 10 - 8 and 10 - 12, 10 being the target
                2 and -2? But both 8 and 12 have a difference of 2 from 10 right? +_?
                RIGHT, RIGHT in terms of 'magnitude'. So, Take absolute differences

            Now how do we start?
            Simple, sort the array, You'll understand why later

            Initiate ans to some big value, because we are going to minimize it later

            Start looping, set two pointers s = i+1, e = len(nums) - 1

            set a while loop till s < e
            start summing elements nums[i] + nums[s] + nums[e]

            3 Conditions are:
                if sum == target: # Ideal scenario, Golden answer
                    return sum
                elif sum<target: # THIS is why we sort, (go check tripletsummation, It'll clear you concepts out further)
                    s+=1
                else: # Value was larger
                    e-=1
            
            Now in each iteration, Calculate the answer

            ans = min(ans, sum, key=lambda x:abs(target-x))
                * Why the lambda function and key?
                    Key tells the min() to evalute abs differences, For what?
                        For all the parameters inside the min function, In this case ans &sum
                        Let's make this easy for you:
                         Its the same as doing this:
                            sum_diff = abs(target - sum)
                            ans_diff = abs(target - ans)
                         if sum_diff < ans_diff:
                             ans = sum_diff
            
            That's it, Done :cointosser: ;)

        '''
        nums = sorted(nums) # Sorting
        ans = 9999999 # Some unfathomable number

        for i in range(len(nums)):
            s = i+1 # Start pointer
            e = len(nums) - 1 # end pointer

            while (s < e): # Start rolling the dice!
                sum = nums[i] + nums[s] + nums[e]

                if sum == target: # Golden hit, Return immediately
                    return sum
                elif sum<target: # Less val, increment start
                    s+=1
                else: # Higher than targer, decr end
                    e-=1
                ans = min(ans, sum, key=lambda x:abs(target-x)) # Lambda function to evaluate abs diff
        return ans
            

                