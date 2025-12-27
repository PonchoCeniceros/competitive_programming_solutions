from typing import Dict


#
# Exercise 1137
#
class Solution:
    memo: Dict = {}

    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        if n == 2:
            return 1

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = (
            self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        )
        return self.memo[n]


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.tribonacci(n=25))
