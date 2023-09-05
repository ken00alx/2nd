import collections

test_tup = ('gfg', 1, ['is', 'best'])
print("The original tuple is : " + str(test_tup))
# Get tuple element data types
# Using collections.Sequence + isinstance() + type()

res = [(type(ele), len(ele) if isinstance(ele, collections.Sequence) else None)
    for ele in test_tup]

#Printing the result
print(f"The data types of tuple in order are: " + str(res))