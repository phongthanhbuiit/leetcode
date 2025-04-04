# Answer[i] = nums[0] x nums[1] x ... x nums[i+1] x ... x nums[n-1]
# P[i] = 0 x ... x ... x i - 1
# S[i] = i+1 x ... x n - 1
# => A[i] = P[i] x S[i]
# P[i] = P[i-1] x num[i-1]
# S[i] = S[i+1] x num[i+1]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer