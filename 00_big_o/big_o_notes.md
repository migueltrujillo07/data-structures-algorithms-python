# Big-O Notation – Notes

## What is Big-O?
Big-O notation describes the **upper bound** of an algorithm’s growth rate.

It answers the question:
> How does performance change as input size (n) increases?

---

## Time vs Space Complexity
- **Time Complexity**: How long the algorithm takes to run
- **Space Complexity**: How much extra memory it uses

---

## Common Big-O Classes

| Big-O | Name | Example |
|----|----|----|
| O(1) | Constant | Access array element |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through list |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Naive recursion |

---

## Rules to Analyze Big-O

1. Drop constants  
   - O(2n) → O(n)

2. Drop lower-order terms  
   - O(n² + n) → O(n²)

3. Loops add complexity  
   - One loop → O(n)
   - Nested loops → O(n²)

4. Sequential blocks  
   - O(n) + O(n) → O(n)

---

## Python-Specific Notes
- List access: O(1)
- Dictionary lookup: O(1) average
- Sorting: O(n log n)

---

## Interview Tip
Always explain:
1. What the algorithm does
2. Time complexity
3. Space complexity
