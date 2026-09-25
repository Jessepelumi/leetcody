"""In-Place Unique Elements"""
"""
values = 112; seen = 12
read:      ^
write:     ^
values = 12
"""
def extract_unique_elements(values: list[int]) -> int:
    seen = set()
    write = 0

    for read in range(len(values)):
        values[write] = values[read]

        if values[write] not in seen:
            seen.add(values[write])
            write += 1

    return write

"""Limit Element Occurences"""
"""
nums = 111223; counts = {num:count}
read:     ^
write:   ^
nums = 
"""
def limit_element_occurence(nums: list[int]) -> int:
    counts = {}
    write = 0

    for read in range(len(nums)):
        nums[write] = nums[read]
        counts[nums[write]] = counts.get(nums[write], 0) + 1

        if counts[nums[write]] <= 2:
            write += 1

    return write
