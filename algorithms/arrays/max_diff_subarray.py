def best_time_to_buy_and_sell_stock(arr: list[int]) -> list[int]:
    max_diff = 0
    current_diff_start = 0
    max_diff_pos = [0, 0]
    for i in range(1, len(arr)):
        new_diff = arr[i] - arr[current_diff_start]
        if arr[i] < arr[current_diff_start]:
            current_diff_start = i
        elif new_diff > max_diff:
            max_diff_pos = [current_diff_start, i]
            max_diff = new_diff
    return max_diff, max_diff_pos


if __name__ == "__main__":
    print(best_time_to_buy_and_sell_stock([7,1,5,3,6,4]))
