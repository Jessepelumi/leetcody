"""
input = ["eat", "tea", "tan", "ate", "nat", "bat"] 
output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

- pick a string
- compare it with every other string
- add them to a bucket
- when complete, add the bucket to the container
- create a new empty bucket
"""
def group_anagrams_bruteforce(words: list[str]) -> list[list[str]]:
    processed = set()
    current_group = []
    group = []

    for i in range(len(words)):
        if i in processed:
            continue
        current_group.append(words[i])
        processed.add(i)

        target_word = sorted(words[i])

        for j in range(i+1, len(words)):
            if j in processed:
                continue
            if target_word == sorted(words[j]):
                current_group.append(words[j])
                processed.add(j)
        group.append(current_group)
        current_group = []

    return group

"""
group = {sorted_string:[anagrams]}
"""
def group_anagrams_v(words: list[str]) -> list[list[str]]:
    # processed = set()
    # current_group = []
    group = {}

    for i in range(len(words)):
        key = sorted(words[i])
        key = "".join(key)

        if key not in group:
            group[key] = [words[i]]
        else:
            group[key].append(words[i])

    result = []
    for key in group:
        result.append(group[key])
        

        # for j in range(i+1, len(words)):
        #     if j in processed:
        #         continue
        #     if target_word == sorted(words[j]):
        #         current_group.append(words[j])
        #         processed.add(j)
        # group.append(current_group)
        # current_group = []

    return result

# result = group_anagrams_v(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(result)


"""Changes to make anagrams"""
"""
s1 = "bond"
s2 = "down"

ds = b o n d
final = bon, bn, b
"""
def how_many_changes(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("The words must be of same length")

    result = []

    for char in s1:
        result.append(char)

    for char in s2:
        if char in result:
            result.remove(char)

    return len(result)

"""
s1 = bond
s2 = down

result = {char:count}
"""
def how_many_changes_v(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("The words must be of same length")

    counts = {}

    for char in s1:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    for char in s2:
        if char in counts and counts[char] > 0:
            counts[char] -= 1

    sum = 0

    for key in counts:
        sum += counts[key]

    return sum
          

    # for char in s1:
    #     result.append(char)

    # for char in s2:
    #     if char in result:
    #         result.remove(char)


res = how_many_changes_v("aab", "abb")
print(res)
