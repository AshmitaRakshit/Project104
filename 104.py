
from collections import Counter
new_data="WhitehatJr"
data=Counter(new_data)
print(data)
#output
#Counter({'h': 2, 't': 2, 'W': 1, 'i': 1, 'e': 1, 'a': 1, 'J': 1, 'r': 1})

new_list=data.items()
print(new_list)
#output
#dict_items([('W', 1), ('h', 2), ('i', 1), ('t', 2), ('e', 1), ('a', 1), ('J', 1), ('r', 1)])
#.items method() is used to return the list with dictionary keys and values

value=data.values()
print (value)
#output
#dict_values([1, 2, 1, 2, 1, 1, 1, 1])
#.values() returns all the values in the dictionary