## Code Challenge: Left Rotation
a *left rotation* operation on an array shofts each of the array's elements `1` unit to the left. 
For example, if `2` left rotations are performed on array `[1, 2, 3, 4, 5]`, then the array would become `[3, 4, 5, 1, 2]`. Given an array `a` of `n` integers, and a number `d`, to perform `d` left rotations on the array. Return the updated array.

#### Example:
```
Input: [1, 2, 3, 4, 5], 4
Output: [5, 1, 2, 3, 4]
Explanation: Perform d = 4 left rotations, the array undergoes the followin sequence of changes:
[1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1] -> [3, 4, 5, 1, 2] -> [4, 5, 1, 2, 3] -> [5, 1, 2, 3, 4]
```

Source: HackerRank