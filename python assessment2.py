def sort_key(tuple_item):
    return tuple_item[-1]

def sort_tuples_by_last_element(tuple_list):
    sorted_list = sorted(tuple_list, key=sort_key)
    return sorted_list

# Sample List
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sorting the list
result = sort_tuples_by_last_element(sample_list)

# Printing the sorted result
print("Expected Result:", result)
