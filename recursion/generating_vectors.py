def generating_vectors(arr, index):
    if index >= len(arr):
        print(', '.join([str(x) for x in arr]))
        return
    for num in range(0, 2):
        arr[index] = num
        generating_vectors(arr, index + 1)


generating_vectors([0,0,1], 0)


def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)

# gen01(0, [None, None, None])