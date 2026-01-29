from typing import List
from log import Log
import re


#
# Exercise 1003
#
class Solution:
    #
    # Mi original solution, didnt implement stacks but regex works for me
    # also i prefer to keep this solition because I implemented a 2 lvl
    # exception handling
    #
    def op(self, s: str) -> str:
        try:
            (x, y) = re.split(r"abc", s, maxsplit=1)
            return x + y

        except Exception as e:
            raise e

    def _isValid(self, s: str) -> bool:
        try:
            # Log.teal(s)
            t = s
            while t != "":
                t = self.op(t)
                # Log.blue('""' if t == "" else t)

            return True

        except Exception:
            return False

    #
    # better solution with stack
    #
    def isValid(self, s: str) -> bool:
        S: List = []

        if len(s) < 3:
            return False

        for c in s:
            S.append(c)
            if len(S) >= 3:
                if S[-3] + S[-2] + S[-1] == "abc":
                    S.pop()
                    S.pop()
                    S.pop()
        return not S


if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver.isValid(s='aabcbc')}")
    Log.green(f"{solver.isValid(s='abcabcababcc')}")
    Log.green(f"{solver.isValid(s='abccba')}")
