"""
  How to perform dictionary comprehension
    {key: value for key, value in iterable}
"""
nums_dict = {x:x*x for x in range(1,10)}
print(nums_dict)