from typing import List, Set
from log import Log


#
# Exercise 26
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # implementamos un set auxiliar para alamcenar los elementos unicos
        # y una lista auxiliar para procesar el algoritmo (muy programación funcional)
        aux: Set = set()
        arr: List = []

        for n in nums:
            if n not in aux:
                aux.add(n)
                arr.append(n)

        # este truco me gustó, cambiar el contenido
        # completo de la lista con un slice
        nums[:] = arr
        return len(nums)

    def test(self, nums: List[int], expectedNums: List[int]) -> None:
        k = self.removeDuplicates(nums)
        assert k == len(expectedNums)

        for i in range(k):
            assert nums[i] == expectedNums[i]


if __name__ == "__main__":
    solver = Solution()
    solver.test(nums=[1, 1, 2], expectedNums=[1, 2])
    solver.test(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], expectedNums=[0, 1, 2, 3, 4])
