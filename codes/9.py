import pytest
from utils.log import Log
from typing import List, Dict, Optional


#
# Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool: ...


# Unit tests


@pytest.mark.parametrize(
    "x, expected",
    [(121, True), (-121, False), (10, False)],
)
def test_Palindrome_Number(x, expected):
    sol = Solution()
    assert sol.isPalindrome(x) == expected
