from typing import List, Dict
from log import Log

log = Log()


#
# Exercise 746
#
class Solution:
    memo: Dict = {}

    def C(self, s, cost):
        return s >= len(cost)

    def foo(self, s: int, c: int, cost: List[int]) -> int:
        if self.C(s, cost):
            return 0

        if s in self.memo:
            return self.memo[s]

        x = 0 if self.C(s + 1, cost) else cost[s + 1]
        y = 0 if self.C(s + 2, cost) else cost[s + 2]

        self.memo[s] = c + min(
            self.foo(s + 1, x, cost),
            self.foo(s + 2, y, cost),
        )
        return self.memo[s]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = self.foo(-1, 0, cost)
        self.memo.clear()
        return ans


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.minCostClimbingStairs(cost=[10, 15, 20]))
    print("✅", solver.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
