def rotate_array(arr: list[int], k: int):
    copy = arr[:]
    if k > len(arr):
        k %= len(arr)
    for i in range(0, len(arr)+k):
        rotate_index = i-k
        pos_index = i
        if rotate_index < 0:
            rotate_index = len(arr) + rotate_index
        print(pos_index, len(arr) - 1)
        if pos_index > len(arr) - 1:
            pos_index = pos_index - len(arr)
        print(pos_index)
        arr[pos_index] = copy[rotate_index]
    print(arr)


if __name__ == "__main__":
    # rotate_array([1,2,3,4,5], 3)
    rotate_array([-1], 2)