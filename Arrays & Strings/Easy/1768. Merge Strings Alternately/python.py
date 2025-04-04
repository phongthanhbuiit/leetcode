# String Solution
# Time:  O(n+m)²
# Space:  O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        len1 = len(word1)
        len2 = len(word2)

        for i in range(min(len1, len2)):
            result + = word1[i]
            result += word2[i]
               
        if (len1 > len2):
            result += word1[len2:]
        elif len2 > len1:
            result += word2[len1:])

        return result


# Optimal Solution
# Time:  O(n+m)
# Space:  O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        len1 = len(word1)
        len2 = len(word2)

        for i in range(min(len1, len2)):
            result.append(word1[i])
            result.append(word2[i])
            
        if len1 > len2:
            result.append(word1[len2:])
        elif len2 > len1:
            result.append(word2[len1:])

        return ''.join(result)