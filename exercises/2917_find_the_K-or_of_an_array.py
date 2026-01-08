from typing import List
from log import Log

log = Log()


#
# Exercise 2917
#
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        answ = 0
        mask = 1

        for _ in range(32):
            cnt = 0
            for n in nums:
                bit = n & mask
                cnt = cnt + 1 if bit > 0 else cnt
            if cnt >= k:
                answ += mask

            mask <<= 1
        return answ


if __name__ == "__main__":
    solver = Solution()
    log.green(f"{solver.findKOr(nums=[7, 12, 9, 8, 9, 15], k=4)}")
    log.green(f"{solver.findKOr(nums=[2, 12, 1, 11, 4, 5], k=6)}")
    log.green(f"{solver.findKOr(nums=[10, 8, 5, 9, 11, 6, 8], k=1)}")
