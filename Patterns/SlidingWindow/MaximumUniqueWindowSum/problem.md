## Maximum Unique Window Sum

#### Pattern: Fixed Window

You are given an integer array `nums` and a positive integer `k`. Your task is to find the maximum possible sum among all contiguous segments (windows) of the array that satisfy the following conditions:


The window has exactly `k` consecutive elements. All `k` elements within the window are distinct (no duplicates).


Return the maximum sum of any window that meets both conditions. If no such window exists in the array (i.e., every contiguous segment of length `k` contains at least one duplicate), return `0`.

#### Understanding the Problem:

A window is a contiguous subsequence of consecutive elements in the array. For a window of size `k` starting at index `i`, it includes elements `nums[i], nums[i+1], ..., nums[i+k-1]`. The window is considered valid only when all `k` elements are unique — meaning no value appears more than once within that specific window.


Your goal is to identify the valid window with the highest sum of elements.

#### Examples

```
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
```

###### Explanation:

All windows of length 3 are:


- [1,5,4]: All elements are distinct. Sum = 1 + 5 + 4 = 10 ✓
- [5,4,2]: All elements are distinct. Sum = 5 + 4 + 2 = 11 ✓
- [4,2,9]: All elements are distinct. Sum = 4 + 2 + 9 = 15 ✓
- [2,9,9]: Contains duplicate 9. Invalid ✗
- [9,9,9]: Contains duplicate 9s. Invalid ✗


Among the valid windows, [4,2,9] has the maximum sum of 15.

```
Input: nums = [4,4,4], k = 3
Output: 0
```

###### Explanation:

The only window of length 3 is [4,4,4], which contains duplicate elements (the value 4 appears three times). Since there is no valid window with all distinct elements, we return 0.

```
Input: nums = [1,2,3,4,5], k = 2
Output: 0
```

###### Explanation:

All windows of length 2 are:


- [1,2]: Distinct. Sum = 3 ✓
- [2,3]: Distinct. Sum = 5 ✓
- [3,4]: Distinct. Sum = 7 ✓
- [4,5]: Distinct. Sum = 9 ✓


The maximum sum among all valid windows is 9.

#### Constraints:

```
1 ≤ k ≤ nums.length ≤ 10⁵
1 ≤ nums[i] ≤ 10⁵
```
