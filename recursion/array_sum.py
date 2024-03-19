def calc_sum(arr, index):
    if index == len(arr) - 1:
        n=5
        return arr[index]
    return arr[index] + calc_sum(arr, index + 1)

print(calc_sum([1, 2, 3, 4], 0))
