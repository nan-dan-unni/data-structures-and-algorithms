def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            print(i, j)
            if arr[j+1] < arr[j]:
                ele_i = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = ele_i

    return arr

if __name__ == "__main__":
    print(bubble_sort([2,9,1,3,4]))
