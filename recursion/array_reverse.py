# 1
def array_reverse(idx, elements):
    if idx == len(elements) // 2:
        return
    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    array_reverse(idx + 1, elements)


elements = [1, 2, 3, 4, 5]
array_reverse(0, elements)
print (elements)

# 2
print(elements[::-1])

# 3
reversed_arr = []
while elements:
    reversed_arr.append(elements.pop())
print(reversed_arr)



