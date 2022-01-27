from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0]*(len(nums)+1)

        memo[0] = 0
        memo[1] = nums[0]

        for i in range(2, len(memo)):
            memo[i] = max(memo[i-1], memo[i-2]+nums[i-1])

        return memo[-1]
