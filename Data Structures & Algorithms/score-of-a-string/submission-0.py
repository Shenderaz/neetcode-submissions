class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s) -1): #go through the loop, no visiting the last position
            abs (ord (s[i]) - ord(s[i +1])) # get ASCII values from both side
            res += abs(ord (s[i]) - ord (s[i +1])) # get it in the result 
            
        return res

        