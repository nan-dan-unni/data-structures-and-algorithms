def find_two_sum(arr: list[int], sum: int) -> list[int]:
    if len(arr) > 1:
        history = {}
        for i in range(len(arr)):
            diff = sum - arr[i]
            if diff in history:
                return [history[diff], i]
            history[arr[i]] = i

    return []


if __name__ == "__main__":
    print(find_two_sum([3, 2, 3, 2], 5))