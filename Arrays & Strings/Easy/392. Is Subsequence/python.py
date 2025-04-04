# Time:  O(n)
# Space:  O(n)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = len(s)
        if count == 0:
            return True

        index = 0

        for c in t:
            if index >= len(s):
                return False

            if c == s[index]:
                index += 1
                count -= 1

            if count == 0:
                return True

        return False


# clean code
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        for c in t:
            if index < len(s) and c == s[index]:
                index += 1
        
            if index == len(s):
                return True
        
        return index == len(s) 