def dutch_national_flag(arr):
    # count the number of 0s, 1s and 2s
    count0 = count1 = count2 = 0
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    # based on the counts, 
    # add these numbers to the new arr
    new_arr_0 = []
    new_arr_1 = []
    new_arr_2 = []
    for i in range(len(arr)):
        if count0 != 0:
            new_arr_0.append(0)
            count0 -= 1
        if count1 != 0:
            new_arr_1.append(1)
            count1 -= 1
        if count2 != 0:
            new_arr_2.append(2)
            count2 -= 1

    final_arr = new_arr_0 + new_arr_1 + new_arr_2

    return final_arr



arr = [2, 0, 1, 2, 1, 0]
print(dutch_national_flag(arr))