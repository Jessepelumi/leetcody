## Tri-Value Partition

#### Pattern: Partitioning

You are given an array nums containing n elements where each element is exclusively one of three distinct values: 0, 1, or 2. Your task is to rearrange the array in-place such that all elements with value 0 appear first, followed by all elements with value 1, and finally all elements with value 2.


The result should group identical values together in ascending order of their category (0s, then 1s, then 2s).

#### Key Constraints:

You must modify the array in-place without allocating a separate array for the output.


You cannot use any built-in sorting function provided by your programming language.


This problem is a classic example of the Dutch National Flag Problem, originally proposed by Edsger W. Dijkstra. It challenges you to efficiently partition elements into three distinct groups using pointer manipulation techniques.

#### Examples

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

###### Explanation:

The array is partitioned so that all 0s come first (positions 0-1), followed by all 1s (positions 2-3), and finally all 2s (positions 4-5). The relative order within each group may vary, but the grouping must be maintained.

```
Input: nums = [2,0,1]
Output: [0,1,2]
```

###### Explanation:

Each distinct value appears exactly once. After partitioning, 0 is at position 0, 1 is at position 1, and 2 is at position 2.

```
Input: nums = [1,0,2,1,2,0,0,1,2]
Output: [0,0,0,1,1,1,2,2,2]
```

###### Explanation:

The array contains three 0s, three 1s, and three 2s. After in-place partitioning, all 0s occupy the first three positions, 1s occupy the middle three positions, and 2s occupy the last three positions.

#### Constraints:

```
n == nums.length
1 ≤ n ≤ 300
nums[i] is either 0, 1, or 2
```
