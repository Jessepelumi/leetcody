## Rearrange Linked List

#### Pattern: Slow Fast Pointers

You are given the head of a singly linked list containing n nodes. Your task is to rearrange the nodes by interleaving elements from the beginning and the end of the list, alternating between them.


The linked list can be visualized as:

```
N₀ → N₁ → N₂ → ... → Nₙ₋₂ → Nₙ₋₁
```

After rearrangement, the list should follow this pattern:

```
N₀ → Nₙ₋₁ → N₁ → Nₙ₋₂ → N₂ → Nₙ₋₃ → ...
```

The transformation pairs the first node with the last, the second node with the second-to-last, and so on, weaving them together into a single interleaved sequence.


**Important:** You must solve this problem by modifying the node connections themselves (in-place). You are not allowed to alter the values stored within the nodes—only the `next` pointers may be changed. The goal is to restructure the list without creating new nodes or using additional data structures proportional to the list size.

#### Examples

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

###### Explanation:

The original list is 1 → 2 → 3 → 4. After rearrangement:


First element (1) connects to last element (4) 4 connects to second element (2) 2 connects to second-to-last element (3)


Final list: 1 → 4 → 2 → 3

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

###### Explanation:

The original list is 1 → 2 → 3 → 4 → 5. After rearrangement:


First (1) → Last (5) → Second (2) → Second-to-last (4) → Middle (3)


Final list: 1 → 5 → 2 → 4 → 3


Notice the middle element (3) remains at the end for odd-length lists.

```
Input: head = [1,2,3]
Output: [1,3,2]
```

###### Explanation:

The original list is 1 → 2 → 3. After rearrangement:


First (1) → Last (3) → Middle (2)


Final list: 1 → 3 → 2

#### Constraints

```
The number of nodes in the list is in the range [1, 5 * 10⁴].
1 ≤ Node.val ≤ 1000
You must perform the rearrangement in-place without allocating extra space proportional to the list size.
Only node connections may be modified—node values must remain unchanged.
```
