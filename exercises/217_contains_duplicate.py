from typing import List, Dict
from ..log import Log


#
# Exercise 217
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # la verdad aqui pude haber implementado me jor un set,
        # ya que no requerimos un valor dummy para el set,
        # pero para el caso funciona
        hashTable: Dict = {}

        for n in nums:
            if n in hashTable:
                return True
            hashTable[n] = "x"  # la x es dummy
        return False


if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver.containsDuplicate(nums=[1, 2, 3, 1])}")
    Log.green(f"{solver.containsDuplicate(nums=[1, 2, 3, 4])}")
    Log.green(f"{solver.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])}")
