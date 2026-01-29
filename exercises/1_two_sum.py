from typing import List, Dict
from log import Log


#
# Exercise 1
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x, y = 0, 0
        # con los hashTable podemos hacer consultas en O(1),
        # si la respuesta que buscamoas esta contenida en el
        # mismo conjunto de información, podemos usar un hash
        # map para auxiliarnos en consultar si dicha respuesta
        # ya está en el conjunto previo que hemos revisado
        hashTable: Dict = {}

        for i, x in enumerate(nums):
            y = target - x

            # necesito encontrar una y en mi hash table de x acumuladas,
            # ya que alguna de esas x satisfarán x + y = target
            if hashTable.get(y, None) is not None:
                x, y = i, hashTable[y]
                break

            # guardo la x para la siguiente y propuesta
            hashTable[x] = i

        return [x, y]


if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver.twoSum(nums=[2, 7, 11, 15], target=9)}")
    Log.green(f"{solver.twoSum(nums=[3, 2, 4], target=6)}")
    Log.green(f"{solver.twoSum(nums=[3, 3], target=6)}")
    Log.green(f"{solver.twoSum(nums=[3, 2, 3], target=6)}")
