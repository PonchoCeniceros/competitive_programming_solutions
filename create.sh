#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./create.sh \"<number>. <problem_name>\""
  echo "Example: ./create.sh \"9. Palindrome Number\""
  exit 1
fi

DIRECTORY="codes"
INPUT=$1

# Extract number and problem name (supports both "9. Palindrome Number" and "9 Palindrome Number")
NUMBER=$(echo "$INPUT" | grep -oE '^[0-9]+')
PROBLEM_NAME=$(echo "$INPUT" | sed -E 's/^[0-9]+\.? *//')

# Generate function name from problem name (convert spaces to underscores)
FUNCTION_NAME=$(echo "$PROBLEM_NAME" | sed 's/[^a-zA-Z0-9 ]//g' | sed 's/  */_/g' | sed 's/ /_/g')

if [ -z "$NUMBER" ] || [ -z "$PROBLEM_NAME" ]; then
  echo "❌ Error: Invalid format. Use \"<number>. <problem_name>\" or \"<number> <problem_name>\""
  echo "Example: ./create.sh \"9. Palindrome Number\""
  echo "Example: ./create.sh \"9 Palindrome Number\""
  exit 1
fi

FILE_PATH="${DIRECTORY}/${NUMBER}.py"

mkdir -p "$DIRECTORY"

cat <<EOF >"$FILE_PATH"
import pytest
from utils.log import Log
from typing import List, Dict, Optional


#
# $PROBLEM_NAME
#
class Solution:
    ... # Implement your solution here


# Unit tests


@pytest.mark.parametrize(
    "", # "parameters, expected",
    [
        # Add your test cases here
    ],
)
def test_${FUNCTION_NAME}(parameters, expected):
    sol = Solution()
    # assert sol.method_name(parameters) == expected
EOF

echo "✅ Ready for TDD at: $FILE_PATH"
