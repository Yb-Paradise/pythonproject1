courses =["MIT","Cyber security","Datascience"]
print(courses)
#accessing an element
print(courses[2])

#Looping through an array
for a in courses:
    print("course is",a)

#Adding a new element into an array
courses.append("laravel")
print(courses)

#deleting an element from an array
courses.remove("Cyber security")
print(courses)