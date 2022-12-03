# Remove duplicates from list
# without using Sets.

test_list = [1, 2, 34, 34, 5, 6, 67, 67, 2]

no_dup_list = []

for element in test_list:
    if element not in no_dup_list:
        no_dup_list.append(element)

print(no_dup_list)
