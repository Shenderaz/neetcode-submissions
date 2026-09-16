class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            storeS, storeT = {}, {}
            for i in range(len(s)):
                storeS[s[i]] = 1 + storeS.get(s[i],0)
                storeT[t [i]] = 1 + storeT.get(t[i],0)
                

            return storeS == storeT

