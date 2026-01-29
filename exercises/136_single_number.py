from typing import List, Set
from log import Log


#
# Exercise 136
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        S: Set = set()

        for n in nums:
            if n not in S:
                S.add(n)
            else:
                S.remove(n)

        return list(S)[0]


if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver.singleNumber(nums=[2, 2, 1])}")
    Log.green(f"{solver.singleNumber(nums=[4, 1, 2, 1, 2])}")
    Log.green(f"{solver.singleNumber(nums=[1])}")
