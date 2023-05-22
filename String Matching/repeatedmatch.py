class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        # Logic: Basic string matching

        '''
            Pretty straightforward approach

            We are supposed to repeat 'a', 'n' number of times so that b is a substring of a
            The question asks what is the minimum number of repetitions required?

            What do we do?
            First thing's first

            IF b is already in a
            eg. a = "aa"
                b = "a"
            
            Finished, In 1 repetition of a i.e aa I get the substring b, So return 1

            Next, The main logic

            Now lets calc the repetitions reqd:
                We need to calc how many times we have to repeat a so as to "Fully" or "Partially" in some cases, Cover b

                For that, We divide lengths (No shit sherlock what next -_-)
                That being obvious, We take the ceil value
                * Why ceil?
                 First of all, Only consider float division '/' because we are tring to cover a length, cover 'something', cover 'distance', In this case 'Cover b'

                 Now If I'm trying to cover b, and my lengths divide to 2.5, I wont cover b in 2.5 or even 2, I NEED 3, and 3 is a CEIL value of division

                 Take this eg:
                 a = "abc"
                 b = "cabcabcab"

                 divide their lengths:
                    8/3 = 2.6
                    Firstly, No you can't split a string in 2.6 parts -_-
                    It's either 2 or 3,
                    Can 2 repetitions fully, or hell even close in to fully cover b?
                    No right?

                    Now consider 3,
                    abcabcabc, is CLOSE to cover the b string

                    3 is the Ceil value of division, that's why, we take ceil :)

                Next task at hand is simply constructed = a*repeats (forms the repeated string)
                Just start matching this string now
                  if b in constructed: (fully covered b as is)
                    return repeats # correct no. of repetitions already
                  if b in constructed+a: (partially covered b as in the above floor ceil eg.) # one more concat of a was needed
                    return repeats+1 # +1 for concat
                  else: (If even a concat wasn't enough to cover b, b is not in a i.e. a can never form b)
                    return -1

            Done


        '''
        if b in a:
            return 1
        
        repeats = math.ceil(len(b) / len(a))

        constructed = a*repeats

        if b in constructed:
            return repeats
        elif b in constructed+a:
            return repeats+1
        else:
            return -1
        
            
