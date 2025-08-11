def find_arr_area(arr, x, y):
    b = y - x
    y_val = arr[y]
    x_val = arr[x]
    l = y_val
    if y_val > x_val: l = x_val
    return l * b

def max_area_subarray(arr: list[int]):
    current_area = arr[0]
    current_area_start = 0
    potential_start = 0
    max_area = 0
    max_area_pos = [0, 0]
    for i in range(0, len(arr)):
        val = arr[i]
        print(val)
        new_area = find_arr_area(arr, current_area_start, i)
        potential_area = find_arr_area(arr, potential_start, i)
        if potential_area > new_area and potential_area > max_area:
            max_area = potential_area
            current_area_start = potential_start
            max_area_pos = [current_area_start, i]
        elif new_area > max_area:
            max_area = new_area
            current_area_start = i
            max_area_pos = [current_area_start, i]
        if val > arr[potential_start]:
            potential_start = i
        print("current_start =", current_area_start, " potential_start =", potential_start, " new_area =", new_area, " current_area =", current_area, "potential_area =", potential_area)

        
    return max_area, max_area_pos

if __name__ == "__main__":
    print(max_area_subarray([1,8,6,2,5,4,8,3,7]))
    print(max_area_subarray([1,2,1]))
    print(max_area_subarray([2,1]))