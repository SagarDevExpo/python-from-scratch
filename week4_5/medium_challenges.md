# Weeks 4-5: Medium Challenges

These are closer to real interview problems.
Be comfortable with the Easy Challenges first.
Each maps to a DSA pattern you'll learn later.

**Practice file:** Create `medium_practice.py`

---

## 1. Two Sum
Return **INDICES** of two numbers that add to target.
`[2, 7, 11, 15]`, target=9 → `[0, 1]`

Try **BOTH** approaches:
- Brute force: Two nested loops → O(n²)
- Optimal: Hash map → O(n)

---

## 2. Valid Parentheses
`"()[]{}"` → `True` | `"([)]"` → `False` | `"([{}])"` → `True`

Hint: Use a list as a stack. Push opens, pop for closes.

---

## 3. Best Time to Buy and Sell Stock
Find max profit from one buy + one sell (must buy before sell).
`[7, 1, 5, 3, 6, 4]` → `5` (buy at 1, sell at 6)
`[7, 6, 4, 3, 1]` → `0` (prices only drop)

Hint: Track minimum price seen so far.

---

## 4. Maximum Subarray (Kadane's Algorithm)
Find contiguous subarray with largest sum.
`[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → `6` (subarray `[4, -1, 2, 1]`)

Hint: `current_sum = max(num, current_sum + num)`

---

## 5. Climbing Stairs
n steps, can climb 1 or 2 at a time. How many distinct ways?
n=1→1, n=2→2, n=3→3, n=4→5

This is the **Fibonacci sequence!** `ways(n) = ways(n-1) + ways(n-2)`

---

## 6. Product of Array Except Self
Each element = product of all OTHER elements. **No division.**
`[1, 2, 3, 4]` → `[24, 12, 8, 6]`

Hint: Build prefix products (left→right) and suffix products (right→left).

---

## 7. Missing Number
n distinct numbers from 0 to n. Find the missing one.
`[3, 0, 1]` → `2`

Approaches: Math (`sum(0..n) - sum(array)`) or Set.

---

## 8. Rotate Array
Rotate right by k steps, **in-place**.
`[1,2,3,4,5,6,7]`, k=3 → `[5,6,7,1,2,3,4]`

Elegant approach (three reverses):
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining elements

---

## 9. Longest Common Prefix
`["flower", "flow", "flight"]` → `"fl"`
`["dog", "racecar", "car"]` → `""`

Hint: Compare characters at each position across all strings.

---

## 10. Number of Islands
2D grid of 1s (land) and 0s (water). Count connected groups of 1s.

```
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
→ **3 islands**

This IS the BFS/DFS problem from the DSA section! Try solving it now with what you know.
