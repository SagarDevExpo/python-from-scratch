"""
WEEKS 4-5: Medium Challenges
These are closer to real interview problems.
You should be comfortable with the Easy Challenges first.

Each one maps to a DSA pattern you'll learn later.

Run: python3 medium_challenges.py
"""


# ============================================================
# 1. Two Sum (uses: dict as hash map)
# ============================================================

"""
Given a list of numbers and a target, return the INDICES of two
numbers that add up to the target.

[2, 7, 11, 15], target=9 → [0, 1] (2+7=9)
[3, 2, 4], target=6 → [1, 2] (2+4=6)

BRUTE FORCE: Two nested loops → O(n²)
OPTIMAL: Hash map → O(n) (you'll learn this in DSA!)

Try BOTH approaches.
"""

# Your code:




# ============================================================
# 2. Valid Parentheses (uses: stack pattern)
# ============================================================

"""
Given a string of brackets, determine if it's valid.
- Every open bracket has a matching close bracket
- Brackets close in the correct order

"()" → True
"()[]{}" → True
"(]" → False
"([)]" → False
"([{}])" → True

Hint: Use a list as a stack. Push opens, pop for closes.
"""

# Your code:




# ============================================================
# 3. Best Time to Buy and Sell Stock (uses: tracking minimum)
# ============================================================

"""
Given a list of stock prices (one per day), find the maximum profit
from buying on one day and selling on a later day.

[7, 1, 5, 3, 6, 4] → 5 (buy at 1, sell at 6)
[7, 6, 4, 3, 1] → 0 (prices only drop, don't buy)

Hint: Track the minimum price seen so far. At each day, check
if selling today would give the best profit.
"""

# Your code:




# ============================================================
# 4. Maximum Subarray (Kadane's Algorithm)
# ============================================================

"""
Find the contiguous subarray with the largest sum.

[-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])
[1] → 1
[-1, -2, -3] → -1

Hint: At each position, decide: start fresh or extend previous subarray?
current_sum = max(num, current_sum + num)
"""

# Your code:




# ============================================================
# 5. Climbing Stairs (uses: dynamic programming intro)
# ============================================================

"""
You're climbing a staircase with n steps. Each time you can
climb 1 or 2 steps. How many distinct ways to reach the top?

n=1 → 1 (just 1 step)
n=2 → 2 (1+1 or 2)
n=3 → 3 (1+1+1, 1+2, 2+1)
n=4 → 5

This is actually the Fibonacci sequence!
ways(n) = ways(n-1) + ways(n-2)

Start from the bottom: ways[0]=1, ways[1]=1, build up.
"""

# Your code:




# ============================================================
# 6. Product of Array Except Self
# ============================================================

"""
Given a list, return a list where each element is the product of
all OTHER elements (not itself). Do NOT use division.

[1, 2, 3, 4] → [24, 12, 8, 6]
Explanation: [2*3*4, 1*3*4, 1*2*4, 1*2*3]

Hint: Build prefix products (left to right) and suffix products
(right to left), then multiply them.
"""

# Your code:




# ============================================================
# 7. Missing Number
# ============================================================

"""
Given a list containing n distinct numbers from 0 to n,
find the one number that is missing.

[3, 0, 1] → 2
[0, 1] → 2
[9, 6, 4, 2, 3, 5, 7, 0, 1] → 8

Multiple approaches:
A) Math: sum(0..n) - sum(array)
B) Set: put in set, check which is missing
C) XOR: advanced bit manipulation (optional)
"""

# Your code:




# ============================================================
# 8. Rotate Array
# ============================================================

"""
Rotate a list to the right by k steps (in-place, don't create new list).

[1, 2, 3, 4, 5, 6, 7], k=3 → [5, 6, 7, 1, 2, 3, 4]

Elegant approach (three reverses):
1. Reverse entire array: [7, 6, 5, 4, 3, 2, 1]
2. Reverse first k: [5, 6, 7, 4, 3, 2, 1]
3. Reverse rest: [5, 6, 7, 1, 2, 3, 4]

Write a helper: reverse(nums, start, end)
"""

# Your code:




# ============================================================
# 9. Longest Common Prefix
# ============================================================

"""
Find the longest common prefix among a list of strings.

["flower", "flow", "flight"] → "fl"
["dog", "racecar", "car"] → ""

Hint: Compare characters at each position across all strings.
Stop when characters differ or a string is too short.
"""

# Your code:




# ============================================================
# 10. Number of Islands (simplified grid version)
# ============================================================

"""
Given a 2D grid of 1s (land) and 0s (water), count the number
of islands (groups of connected 1s, horizontally or vertically).

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
Answer: 3

Approach:
- Loop through every cell
- When you find a 1, that's a new island — count it
- "Flood fill" all connected 1s (change to 0 so you don't count again)

This IS the BFS/DFS problem from the DSA section!
Try to solve it with what you know (nested loops + recursion or
just a stack/queue).
"""

# Your code:

