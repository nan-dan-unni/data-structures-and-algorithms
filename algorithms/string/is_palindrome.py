import re

def is_palindrome(s: str):
    left = 0
    right = len(s) - 1
    s = s.replace(" ", "")
    s = re.sub(r'[^0-9a-zA-Z]', "", s)
    slist = list(s)
    while left < right:
        if not slist[left].isalnum() and not slist[right].isalnum():
            left += 1
            right -= 1
            continue
        elif not slist[left].isalnum():
            left += 1
            continue
        elif not slist[right].isalnum():
            right -= 1
            continue
        elif slist[left].lower() == slist[right].lower():
            left += 1
            right -= 1
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    print(is_palindrome("A man, A Plan, A Canal: Panama"))
    print(is_palindrome(" "))
    print(is_palindrome("Race a car"))
