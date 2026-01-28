from typing import Dict
from ..log import Log


#
# Exercise 70
#
class Solution:
    memo: Dict = {}

    def climbStairs(self, n: int) -> int:
        # cuantas formas hay de bajar:
        #
        # 0 escalones: 1 forma, no hacer nada
        # 1 escalón:   1 forma, subir el escalon
        # 2 escalones: 2 formas,
        #             (1) subir de a 2 escalones,
        #             (2) subir de 1 en 1
        if n < 3:
            return n

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver.climbStairs(n=2)}")
    Log.green(f"{solver.climbStairs(n=3)}")
