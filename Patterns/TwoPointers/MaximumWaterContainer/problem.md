## Maximum Water Container

#### Pattern: Converging Pointers

You are given an integer array called height containing n positive integers. Imagine n vertical barriers placed along the x-axis, where the i-th barrier is positioned at coordinate i and extends from the ground (y = 0) up to height[i].


Your task is to select exactly two barriers that, together with the x-axis (the ground), form a rectangular container capable of holding water. The width of the container is determined by the horizontal distance between the two selected barriers, and the height of the container is limited by the shorter of the two barriers (since water would overflow over the shorter side).


Calculate and return the maximum volume of water that any such container can hold.


**Important:** The container must be upright—you cannot tilt or rotate it. The water capacity is computed as:

```
capacity = min(height[left], height[right]) * (right - left)
```

where left and right are the indices of the two chosen barriers (with left < right).

#### Examples

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

###### Explanation:

We select the barriers at indices 1 (height 8) and 8 (height 7). The container width is 8 - 1 = 7, and the effective height is min(8, 7) = 7. Therefore, the maximum water capacity is 7 * 7 = 49.

```
Input: height = [1,1]
Output: 1
```

###### Explanation:

With only two barriers of height 1 each, positioned one unit apart, the water capacity is min(1, 1) * (1 - 0) = 1.

```
Input: height = [1,2,3,4,5]
Output: 6
```

###### Explanation:

The optimal choice is barriers at indices 0 (height 1) and 4 (height 5), or indices 1 (height 2) and 4 (height 5). Using indices 1 and 4: capacity = min(2, 5) * (4 - 1) = 2 * 3 = 6.

#### Constraints

```
n == height.length
2 ≤ n ≤ 10⁵
0 ≤ height[i] ≤ 10⁴
```
