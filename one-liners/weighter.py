internet_usage_age = 13
valid = "Your are allowed to use Youtube"
invalid = "You are not allowed to use youtube"

"""
  normal implementation
if internet_usage_age >= 13:
      print(valid)
else:
   print(invalid)
"""

#one liner
print(valid) if internet_usage_age >= 13 else print(invalid)