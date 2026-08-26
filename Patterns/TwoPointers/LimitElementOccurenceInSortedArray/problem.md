## Limit Element Occurrences in Sorted Array

You are given an integer array `nums` arranged in **non-decreasing order**. Your task is to modify the array **in-place** so that each unique value appears at most twice, while preserving the original relative ordering of elements.


Since certain programming languages do not allow resizing arrays, the valid result should occupy the **first k positions** of the original array. The function must return the value `k`, representing the count of elements in the final processed array.


**Important:** Only the first `k` elements of the modified array will be evaluated. Any values beyond position `k` are considered irrelevant and will not affect the correctness of your solution.


The solution must operate directly on the input array without allocating a separate array for output. Your algorithm should use only `O(1)` **auxiliary space** beyond the input array itself.

#### Examples

```
Input: nums = [1,1,1,2,2,3]
Output: k = 5, nums = [1,1,2,2,3,_]
```

Explanation:
The function returns k = 5. The first five positions contain [1,1,2,2,3]. The element '1' appeared three times originally but now appears only twice. The underscore represents a value that doesn't matter and won't be checked.

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: k = 7, nums = [0,0,1,1,2,3,3,_,_]
```

Explanation:
The function returns k = 7. The first seven positions contain [0,0,1,1,2,3,3]. The value '1' originally appeared four times but is now limited to two occurrences. The two underscores represent irrelevant values.

```
Input: nums = [1,1,2,2,3,3]
Output: k = 6, nums = [1,1,2,2,3,3]
```

Explanation:
The function returns k = 6. Since no element appears more than twice, the array remains unchanged. All six elements are valid in the output.

#### Constraints

```
1 ≤ nums.length ≤ 3 * 10⁴
-10⁴ ≤ nums[i] ≤ 10⁴
The array nums is sorted in non-decreasing order.
```
