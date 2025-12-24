from typing import List


#
# Exercise 888
#
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        ans: List = []
        xSum, ySum = sum(a for a in aliceSizes), sum(b for b in bobSizes)

        total = xSum + ySum
        fair = total / 2

        x = fair - xSum
        y = fair - ySum

        print(f"total: {total}, distribucion: {fair}")
        print(f"x := {x} = {fair} - {xSum}")
        print(f"y := {y} = {fair} - {ySum}")

        return ans

        # xBoxes: List = []
        # yBoxes: List = []
        # ans: List = []
        #
        # priority = ""
        # aLen, bLen = len(aliceSizes), len(bobSizes)
        #
        # if aLen == bLen:
        #     priority = "alice"
        #     xSum = sum(a for a in aliceSizes)
        #     ySum = sum(b for b in bobSizes)
        #     xBoxes = aliceSizes
        #     yBoxes = bobSizes
        #
        # elif aLen < bLen:
        #     priority = "alice"
        #     xSum = sum(a for a in aliceSizes)
        #     ySum = sum(b for b in bobSizes)
        #     xBoxes = aliceSizes
        #     yBoxes = bobSizes
        # else:
        #     priority = "bob"
        #     xSum = sum(b for b in bobSizes)
        #     ySum = sum(a for a in aliceSizes)
        #     xBoxes = bobSizes
        #     yBoxes = aliceSizes
        #
        # for x in xBoxes:
        #     for y in yBoxes:
        #         if (xSum - x + y) == (ySum - y + x):
        #             ans = [x, y] if priority == "alice" else [y, x]
        # return ans


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.fairCandySwap(aliceSizes=[1, 1], bobSizes=[2, 2]))
    print("✅", solver.fairCandySwap(aliceSizes=[2], bobSizes=[1, 3]))
