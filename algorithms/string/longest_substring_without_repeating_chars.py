def longest_substring(s: str):
    max_len = 0
    curr_len = 0
    curr_start = 0
    c_map = {}
    for i, c in enumerate(s):
        if c in c_map and curr_start <= c_map[c]:
            curr_start = c_map[c] + 1
            del c_map[c]
    
        c_map[c] = i
        curr_len = i - curr_start + 1

        if curr_len > max_len:
            max_len = curr_len

    return max_len

if __name__ == "__main__":
    print(longest_substring("pwwkew"))
    print(longest_substring("tmmzuxt"))
