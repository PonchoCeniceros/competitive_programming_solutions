from typing import List


#
# Exercise 1
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibleNums = [{"val": target - n, "idx": i} for i, n in enumerate(nums)]
        possibleNums.sort(key=lambda x: x["val"], reverse=True)

        x, y, z = 0, 0, 0
        flag = True

        for n in possibleNums:
            val = n.get("val", 0)
            idx = n.get("idx", 0)
            if flag:
                z = val
                x = idx
                flag = False
                continue

            if val + z == target:
                y = idx

        return [x, y]


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.twoSum(nums=[2, 7, 11, 15], target=9))
    print("✅", solver.twoSum(nums=[3, 2, 4], target=6))
    print("✅", solver.twoSum(nums=[3, 3], target=6))
