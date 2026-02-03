"""
Basic array (list) operations in Python
"""

# Access - O(1)
def access_element(arr, index):
    return arr[index]


# Update - O(1)
def update_element(arr, index, value):
    arr[index] = value


# Search - O(n)
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# Insert at end - O(1) amortized
def insert_end(arr, value):
    arr.append(value)


# Insert at index - O(n)
def insert_at_index(arr, index, value):
    arr.insert(index, value)


# Delete by index - O(n)
def delete_at_index(arr, index):
    arr.pop(index)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(access_element(nums, 2))
    update_element(nums, 1, 10)
    print(nums)

    print(linear_search(nums, 4))
    insert_end(nums, 5)
    insert_at_index(nums, 1, 99)
    delete_at_index(nums, 0)

    print(nums)
