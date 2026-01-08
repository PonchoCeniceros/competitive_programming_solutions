from typing import Dict
from log import Log

log = Log()


#
# Exercise 509
#
class Solution:
    memo: Dict = {}

    def fib(self, n: int) -> int:
        #
        # caso(s) base
        #
        if n < 2:
            return n

        # veo si el resultado de este caso ya fué
        # calculado por otra llamada recusiva previa
        #
        if n in self.memo:
            return self.memo[n]

        # calculo el resultado y lo almaceno en memoria
        #
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


if __name__ == "__main__":
    solver = Solution()
    log.green(f"{solver.fib(n=2)}")
    log.green(f"{solver.fib(n=3)}")
    log.green(f"{solver.fib(n=4)}")
