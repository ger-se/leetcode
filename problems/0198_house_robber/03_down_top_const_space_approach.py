from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        current = 0
        previous = 0

        n = len(nums)
        for i in range(0, n):
            temp = current
            current = max(current, previous+nums[i])
            previous = temp

        return current
