class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Logic: Simple string manipulation

        '''
            Don't do it in a loop, replace creates a loop for itself
            address = address.replace(".","[.]")
            * Why not only address.replace(".","[.]")?
                s.replace does not modify the string in-place,
                Instead modifies and creates a version of string with changes which
                you can store somewhere
            
            Done :coinflipper: ;)
        '''
        address = address.replace(".","[.]")
        return address