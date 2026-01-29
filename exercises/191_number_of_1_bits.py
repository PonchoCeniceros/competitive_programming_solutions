from log import Log


#
# Exercise 191
#
class Solution:
    def hammingWeight(self, n: int) -> int:
        x, s = n, 0
        while x > 0:
            s += x % 2
            x = x // 2
        return s


if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver.hammingWeight(n=11)}")
    Log.green(f"{solver.hammingWeight(n=128)}")
    Log.green(f"{solver.hammingWeight(n=2147483645)}")
