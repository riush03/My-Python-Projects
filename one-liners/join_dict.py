engineering_course = {'maths':'engineering mathematics','physics':'fluid mechanics'}
education_course = {'english':'literature','maths':'basic mathematics'}

"""
 use ** to join
"""
merged_dict = {**engineering_course,**education_course}

print(merged_dict)