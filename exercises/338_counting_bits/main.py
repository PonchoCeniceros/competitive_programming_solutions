from typing import List
from log import Log

log = Log()


#
# Exercise 338
#
class Solution:
    def count(self, n: int) -> int:
        x, s = n, 0
        while x > 0:
            s += x % 2
            x = x // 2
        return s

    def countBits(self, n: int) -> List[int]:
        ans: List = []
        for i in range(n + 1):
            s = self.count(i)
            ans.append(s)
        return ans


if __name__ == "__main__":
    solver = Solution()
    log.green(f"{solver.countBits(n=2)}")
    log.green(f"{solver.countBits(n=5)}")
