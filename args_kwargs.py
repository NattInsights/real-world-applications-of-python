# this is positional arguments
"""def full_name(fname, surname):
    return fname + " " + surname
print(full_name("Darren", "Lath"))"""

"""def my_dog(breed = "unknown breed", name = "N/A"):
    return "My dog is a " + breed + " and their name is " + name
print(my_dog("Havanese", "Buster"))"""

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")