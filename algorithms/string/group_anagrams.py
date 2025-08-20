def is_anagram(str1: str, str2: str):
    if not len(str1) == len(str2):
        return False
    c_map = {}
    for c in str1:
        if c in c_map:
            c_map[c] += 1
        else:
            c_map[c] = 1
    for c in str2:
        if c in c_map:
            c_map[c] -= 1
            if c_map[c] == 0:
                del c_map[c]
        else:
            return False
    if len(c_map) > 0:
        return False
    return True

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anag_map = {}

    for i, strn in enumerate(strs):
        if strn in anag_map:
            anag_map[strn].append(i)
            continue

        anagrams_found = False
        for key in anag_map:
            if is_anagram(str1=strn, str2=key):
                anag_map[key].append(i)
                anagrams_found = True
                break
        if anagrams_found:
            continue
        anag_map[strn] = [i]
    
    groups = []
    for val in anag_map:
        group = []
        for i in anag_map[val]:
            group.append(strs[i])
        groups.append(group)
    return groups

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan", "eat", "ate","nat","bat"]))
    print(group_anagrams([""]))
    print(group_anagrams(["a"]))
