from typing import List, Optional, Dict


#
# Exercise 2917
#
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        n = nums[0]
        while n > 0:
            bit = n & 1
            print(bit)
            n >>= 1
        return 0


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.findKOr(nums=[7, 12, 9, 8, 9, 15], k=4))
    print("✅", solver.findKOr(nums=[2, 12, 1, 11, 4, 5], k=6))

    # ans = 0
    #
    # for i, y in enumerate(nums):
    #     x = 0
    #     n = y
    #     while n > 0:
    #         bit = n & 1
    #         n >>= 1
    #         x = x + 1 if bit == 1 else x
    #
    #     print(format(y, "08b"), x)
    #     if x >= k:
    #         ans = ans | (1 << i)
    #
    # return ans
