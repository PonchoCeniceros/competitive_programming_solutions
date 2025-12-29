from typing import List, Optional, Dict


#
# Exercise 2917
#
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int: ...


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.findKOr(nums=[7, 12, 9, 8, 9, 15], k=4))
    print("✅", solver.findKOr(nums=[2, 12, 1, 11, 4, 5], k=6))
