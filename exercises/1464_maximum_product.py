from typing import List


#
# Exercise 1464
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        u, iu, v = -1, -1, -1

        for i, n in enumerate(nums):
            if n > u:
                u, iu = n, i

        for i, n in enumerate(nums):
            if iu != i:
                if n > v:
                    v = n

        return (u - 1) * (v - 1)


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.maxProduct(nums=[3, 4, 5, 2]))
    print("✅", solver.maxProduct(nums=[1, 5, 4, 5]))
