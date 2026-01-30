from typing import List, Optional, Dict
from log import Log
import unittest


# Exercise 28
class Solution:
    def strStr(self, haystack: str, needle: str) -> int: ...


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.target = (
            self.sol.strStr  # [metodo a evaluar]
        )

    def test_cases(self):
        Log.teal("Running tests...")
        cases = [
            # Estructura: (input, expected_output)
            (("sadbutsad", "sad"), 0),
            (("leetcode", "leeto"), -1),
        ]

        for i, (input_data, expected) in enumerate(cases):
            with self.subTest(f"Case {i + 1}"):
                # Si el método tiene múltiples argumentos,
                # usa: self.target(*input_data)
                self.assertEqual(self.target(*input_data), expected)


if __name__ == "__main__":
    unittest.main()
