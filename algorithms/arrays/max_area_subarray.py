def max_area_subarray(arr: list[int]):
    max_area = 0
    left_start = 0
    right_start = len(arr) - 1
    max_area_pos = [0, 0]
    while left_start < right_start:
        height = arr[right_start]
        if arr[left_start] < arr[right_start]: height = arr[left_start]
        current_area = (right_start - left_start) * (height)
        if current_area > max_area:
            max_area = current_area
            max_area_pos = [left_start, right_start]
        if arr[left_start] < arr[right_start]:
            left_start += 1
        else:
            right_start -= 1
    
    return max_area, max_area_pos

if __name__ == "__main__":
    print(max_area_subarray([1,8,6,2,5,4,8,3,7]))
    print(max_area_subarray([1,2,1]))
    print(max_area_subarray([2,1]))
