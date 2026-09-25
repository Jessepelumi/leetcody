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

result = group_anagrams_v(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
