# The list containing the number of students who are enrolled in python class
data11 = ['bhargavi', 'sandhya', 'hyndavi', 'somu']
# The list containing the number of students who are enrolled in web development class
data12 = ['bhargavi', 'sandhya', 'hyndavi', 'sandhya', 'roy', 'john', 'somu']

# The below print statement is used for printing the students who are common in both the classes
print("Students who enrolled in both python and web developement classes are: \n")
for a in data11:
    if a in data12:
        print(a)

# The below print statement is used for the students who are enrolled in both of the classes
print("Students who have enrolled in both of web development or python are: \n")

# Checking out the odd one's out from the first available data
for b in data11:
    if b not in data12:
        print(b)

# Checking out the odd one's out from the second available data
for c in data12:
    if c not in data11:
        print(c)