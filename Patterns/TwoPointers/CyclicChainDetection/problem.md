## Cyclic Chain Detection

#### Pattern: Slow Fast Pointers

You are given the starting node of a singly linked list. Your task is to determine whether the linked list contains a cycle — that is, whether any node in the chain eventually points back to a previously visited node, creating an infinite loop.


A cycle exists in the linked list if following the next pointers from the head leads you back to a node you have already traversed. If such a cyclic path exists, return `true`. If the chain terminates naturally (i.e., reaches a null pointer), return `false`.


**Important:** The `pos` parameter shown in the examples is used internally to construct the test case (indicating which node the tail connects to, forming a cycle). This parameter is not passed to your function — you must detect the cycle based solely on the structure of the linked list itself.

#### Examples

```
Input: head = [3,2,0,-4], pos = 1
Output: true
```

###### Explanation:

The linked list has 4 nodes with values [3, 2, 0, -4]. The tail node (-4) connects back to the node at index 1 (value 2), forming a cycle: 3 → 2 → 0 → -4 → 2 → 0 → -4 → ... (repeating infinitely). Since following the chain leads back to a previously visited node, a cycle exists.

```
Input: head = [1,2], pos = 0
Output: true
```

###### Explanation:

The linked list has 2 nodes with values [1, 2]. The tail node (2) connects back to the head node (value 1), forming a cycle: 1 → 2 → 1 → 2 → ... (repeating). A cyclic path is detected.

```
Input: head = [1], pos = -1
Output: false
```

###### Explanation:

The linked list contains only a single node with value 1, and it does not point to any other node (next is null). Since the chain terminates without revisiting any node, there is no cycle.

#### Constraints

```
The number of nodes in the list is in the range [0, 10⁴].
-10⁵ ≤ Node.val ≤ 10⁵
pos is -1 (indicating no cycle) or a valid index in the linked list (0-indexed) where the tail connects.
The pos parameter is for test case construction only and is not passed to your function.
```
