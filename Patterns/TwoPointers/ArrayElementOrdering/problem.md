## Array Element Ordering

#### Pattern: Partition

You are given an array of integers. Your task is to arrange all elements in ascending order and return the resulting array.


The challenge is to implement the ordering algorithm from scratch without relying on any built-in sorting utilities provided by the programming language. Your implementation must achieve a time complexity of O(n log n) and utilize as little additional space as possible.


This problem tests your understanding of efficient comparison-based sorting algorithms such as merge sort, quicksort, or heap sort, and your ability to implement them correctly and efficiently.

#### Examples

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

###### Explanation:

After arranging the elements in ascending order, the array becomes [1,2,3,5]. Notice that elements 2 and 3 remain in their relative positions since they were already in order, while 1 and 5 moved to their correct positions.

```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

###### Explanation:

The array contains duplicate values. After ordering, all identical elements are grouped together: both 0s come first, followed by both 1s, then 2, and finally 5.

```
Input: nums = [-3,2,-1,0,4,-2]
Output: [-3,-2,-1,0,2,4]
```

###### Explanation:

The array contains both positive and negative integers. After ordering, negative numbers appear first in ascending order (-3,-2,-1), followed by zero, and then positive numbers (2,4).

#### Constraints:

```
1 ≤ nums.length ≤ 5 * 10⁴
-5 * 10⁴ ≤ nums[i] ≤ 5 * 10⁴
You must not use any built-in sorting functions
Your solution must run in O(n log n) time complexity
Aim for the minimum space complexity possible
```
