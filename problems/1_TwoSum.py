from typing import List
from unittest import registerResult

from urllib3 import connection_from_url


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return []


def main():
    solution = Solution()

    nums = [3, 3]

    result = solution.twoSum(nums, 6)
    print(result)


if __name__ == "__main__":
    main()

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
