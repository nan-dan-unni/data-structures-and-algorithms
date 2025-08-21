def longest_palindrome_substring(s: str) -> str:
    def find_longest_palindrome_from_center(subs: str, left: int, right: int):
        while(left >= 0 and right <= len(subs) - 1 and subs[left] == subs[right]):
            left -= 1
            right += 1
        return left+1, right-1
    max_len = 0
    max_left = 0
    max_right = 0
    for i in range(len(s)):
        odd_l, odd_r = find_longest_palindrome_from_center(s, i, i)
        even_l, even_r = find_longest_palindrome_from_center(s, i, i+1)
        odd_len = odd_r + 1 - odd_l
        even_len = even_r + 1 - even_l
        if odd_len > max_len:
            max_len = odd_len
            max_left = odd_l
            max_right = odd_r
        if even_len > max_len:
            max_len = even_len
            max_left = even_l
            max_right = even_r

    return s[max_left:max_right+1]


if __name__ == "__main__":
    print(longest_palindrome_substring("bb"))
    print(longest_palindrome_substring("abcdedcfghhgfcdeij"))
    print(longest_palindrome_substring("cbbd"))
    print(longest_palindrome_substring("c"))
