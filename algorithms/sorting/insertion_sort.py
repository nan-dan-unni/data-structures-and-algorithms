def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        ins_ele = arr[i]
        j = i-1
        while j >= 0 and ins_ele < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ins_ele
        print(arr)

    return arr

if __name__ == "__main__":
    print(insertion_sort([2,9,1,3,4]))
