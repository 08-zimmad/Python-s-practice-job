def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Initialize a pointer to keep track of the position to overwrite
    write_index = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous element,
        # overwrite the next position with the current element
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    
    return write_index

# Example usage:
nums = [1, 1, 2, 2, 3]
print(remove_duplicates(nums))  # Output: 5
print(nums[:remove_duplicates(nums)])  # Output: [1, 2, 3, 4, 5]
