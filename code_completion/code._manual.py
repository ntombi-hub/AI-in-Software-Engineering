# manual_code.py
def sort_dict_list(data, key):
    return sorted(data, key=lambda x: x[key])

# Example usage
items = [{'name':'Alice','age':25}, {'name':'Bob','age':20}]
sorted_items = sort_dict_list(items, 'age')
print(sorted_items)
