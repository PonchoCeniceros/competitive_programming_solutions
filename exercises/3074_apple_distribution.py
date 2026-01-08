from typing import List
from log import Log

log = Log()


#
# Exercise 3074
#
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        remains = 0
        reassigments = 0
        capacity.sort(reverse=True)

        for a in apple:
            remains += a

        i = 0
        while remains > 0:
            remains -= capacity[i]
            reassigments += 1
            i += 1

        return reassigments


if __name__ == "__main__":
    solver = Solution()
    log.green(f"{solver.minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2])}")
    log.green(f"{solver.minimumBoxes(apple=[5, 5, 5], capacity=[2, 4, 2, 7])}")
    log.green(f"{solver.minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2])}")
    log.green(
        f"{solver.minimumBoxes(apple=[9, 8, 8, 2, 3, 1, 6], capacity=[10, 1, 4, 10, 8, 5])}"
    )
