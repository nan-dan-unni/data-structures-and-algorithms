import math

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) > 1:
        mid = math.floor(len(arr) / 2)
        left = arr[:mid]
        right = arr[mid:]
        if len(left) > 1:
            left = merge_sort(left)
        if len(right) > 1:
            right = merge_sort(right)
        li = 0
        ri = 0
        i = 0
        while li < len(left) or ri < len(right):
            if li < len(left) and not ri < len(right):
                arr[i] = left[li]
                li += 1
            elif not li < len(left) and ri < len(right):
                arr[i] = right[ri]
                ri += 1
            elif left[li] > right[ri]:
                arr[i] = right[ri]
                ri += 1
            else:
                arr[i] = left[li]
                li += 1
            i += 1
    return arr

if __name__ == "__main__":
    print(merge_sort([64,2,9,-1,32,1,8,0,4,12]))
