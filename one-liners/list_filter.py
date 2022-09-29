"""
  Filter values from a list

   filter(function,iterable)
"""
random_nums = [10,11,12,13,14,15]
print(list(filter(lambda x: x%2 == 0 ,random_nums)))
