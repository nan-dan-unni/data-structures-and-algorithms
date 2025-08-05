def find_max_subarray(arr: list[int]) -> list[int]:
    current_sum = arr[0]
    max_sum = arr[0]
    max_sum_pos = [0,0]
    current_sum_start = 0
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_sum_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_pos = [current_sum_start, i]
    
    if max_sum < current_sum:
        max_sum = current_sum
        max_sum_pos = [current_sum_start, len(arr)-1]

    return max_sum, max_sum_pos

if __name__ == "__main__":
    print(find_max_subarray([-1, -2, 1, 4, 2, -3, 78]))
    print(find_max_subarray([-2, 5, 6]))
    print(find_max_subarray([-1,2,3,10,-2,5,3]))
