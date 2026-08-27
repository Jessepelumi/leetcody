## Relocate Zeroes to End

#### Pattern: Read and Write

You are given an integer array `nums`. Your task is to shift all occurrences of the value `0` to the end of the array while preserving the relative order of all non-zero elements.


**Critical Requirement:** The transformation must be performed **in-place** — meaning you cannot create a separate array or use additional storage proportional to the array size. The operation must modify the original array directly.


This is a fundamental problem in array manipulation that tests your ability to efficiently reorganize elements using constant extra memory while maintaining stability (preserving the original relative ordering of non-zero elements).

#### Examples

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

###### Explanation:

After processing, all non-zero elements (1, 3, 12) appear first in their original relative order, followed by all zeroes (two 0's) at the end.

```
Input: nums = [0]
Output: [0]
```

###### Explanation:

The array contains only a single zero. There are no non-zero elements to move, so the array remains unchanged.

```
Input: nums = [1,0,2,0,3,0,4]
Output: [1,2,3,4,0,0,0]
```

###### Explanation:

Non-zero elements 1, 2, 3, and 4 maintain their relative order and are shifted to the front. The three zeroes are pushed to the end.

#### Constraints

```
1 ≤ nums.length ≤ 10⁴
-2³¹ ≤ nums[i] ≤ 2³¹ - 1
The solution must be in-place with O(1) extra space
```
