# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Bro Code"
# I'm going to be indexing in this section
first_name = name[0:3]  # or [:3]
last_name = name[4:8]  # or [4:]
funky_name = name[0:8:2]  # or [::2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
# ----------------------------------------------------------------------------------------------------------------------
# In this section im going to be slicing

website1 = "https://google.com"
website2 = "https://wikipedia.com"


slice = slice(8, -4)

print(website1[slice])
print(website2[slice])
