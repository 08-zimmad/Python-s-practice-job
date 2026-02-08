#extract unique Elements from sorted Array

# Brute Force Method
# this method is o(N) and takes space

def get_unique_element(arr: list) -> list:
    unique_arr = []

    for i in arr:
        if i in unique_arr:
            continue
        unique_arr.append(i)

    return unique_arr

# Sorted Array
arr = [1,1,2,2,2,3,3,3,3,4,4,4,4,4]

print(get_unique_element(arr))

# what if I want to optimize it?

def get_unique_element_optmzd(arr: list) -> int:
    n = len(arr)
    if n <= 1:
        return n

    idx = 1

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx


# Sorted Array
arr = [1,1,2,2,2,3,3,3,3,4,4,4,4,4]

unique_indx = get_unique_element_optmzd(arr)

for i in range(0, unique_indx):

    print(arr[i])


