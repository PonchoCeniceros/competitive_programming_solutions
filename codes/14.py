import pytest
from utils.log import Log
from typing import List


#
# Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        lens = [len(arr) for arr in strs]
        minLen = min(lens)

        Log.teal(f"{minLen}")

        return ""


# Unit tests


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([], ""),
    ],
)
def test_Longest_Common_Prefix(strs, expected):
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == expected
