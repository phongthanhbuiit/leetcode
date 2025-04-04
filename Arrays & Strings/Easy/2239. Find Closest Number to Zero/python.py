# Easy
# Time: O(n)
# Space: O(1)

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for num in nums:
            if abs(x) > abs(num):
                x = num
            elif (x < num) and (abs(num) == abs(x)):
                x = num
        return x
