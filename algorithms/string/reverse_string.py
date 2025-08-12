def reverse_string(string: list[str]) -> str:
    p1 = 0
    p2 = len(string) - 1
    while p1 < p2:
        temp = string[p1]
        string[p1] = string[p2]
        string[p2] = temp
        p1 += 1
        p2 -= 1
    print(string)

if __name__ == "__main__":
    reverse_string(list("abcdefgh"))
    reverse_string(list("a"))