def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        min_ele = arr[min_pos]
        arr[min_pos] = arr[i]
        arr[i] = min_ele

    return arr

if __name__ == "__main__":
    print(selection_sort([2,9,1,3,4]))
