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
