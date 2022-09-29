#create a list based on existing lists
courses = ['chinese','french','science','hydraulics','gender']

"""
  How to use list comprehension
  [expression for item in list]
"""
convert_to_uppercase = [course.title() for course in courses]
print(convert_to_uppercase)