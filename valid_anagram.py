s = "racecar"
t = "carrace"

class Solution:
    def isAnagran(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            for i in s:
                t=t.replace(i,"",1)
            
            return len(t) == 0
        
solve = Solution()

print(solve.isAnagran(s, t))