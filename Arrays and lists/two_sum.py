def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums): # enummerate can give you access to both index and value

        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i] # returns the current index i and stored index in dictionary num_indices[complement]
        num_indices[num] = i
    return []

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))
