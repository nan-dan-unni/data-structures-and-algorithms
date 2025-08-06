# best time to buy and sell stock

def best_time_to_buy_and_sell_stock(arr: list[int]) -> list[int]:
    current_diff = 0
    current_diff_start = 0
    max_diff = current_diff
    max_diff_pos = [0, 0]
    for i in range(1, len(arr)):
        new_diff = arr[i] - arr[current_diff_start]
        if new_diff < current_diff:
            current_diff = 0
            current_diff_start = i
        else:
            current_diff = new_diff

        if current_diff > max_diff:
            max_diff = current_diff
            max_diff_pos = [current_diff_start, i]
    return max_diff, max_diff_pos

if __name__ == "__main__":
    print(best_time_to_buy_and_sell_stock([5,3,2,6,8,5]))