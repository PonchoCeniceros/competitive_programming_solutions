#!/bin/bash

# 1. Check if a name was provided
if [ -z "$1" ]; then
  echo "Usage: ./create_exercise.sh <exercise_name>"
  echo "Example: ./create_exercise.sh 3074_apple_distribution"
  exit 1
fi

# 2. Setup directory and filenames
DIRECTORY="exercises"
BASE_NAME=$1
FILE_PATH="${DIRECTORY}/${BASE_NAME}.py"

# Create the directory if it doesn't exist
mkdir -p "$DIRECTORY"

# 3. Extract the starting number (finds digits before the first underscore)
NUMBER=$(echo "$BASE_NAME" | grep -oE '^[0-9]+')

# 4. Create the file and add the template code
cat <<EOF >"$FILE_PATH"
from typing import List, Optional, Dict


#
# Exercise ${NUMBER:-"N/A"}
#


if __name__ == "__main__":
    solver = Solution()
    # print("✅", solver.)
EOF

echo "✅ File successfully created at: $FILE_PATH"
