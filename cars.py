my_showroom = set()

my_showroom.add("Viper")
my_showroom.add("Model A")
my_showroom.add("Mazda 3")
my_showroom.add("Model T")


# print(len(my_showroom))

my_showroom.add("Model A")

# print(my_showroom)

second_garage = {"Mini", "Civic"}
my_showroom.update(second_garage)

# print(my_showroom)

my_showroom.discard("Model T")
# print(my_showroom)

my_junkyard = set()

my_junkyard.add("Model A")
my_junkyard.add("Mustang")
my_junkyard.add("Corvette")
my_junkyard.add("Mazda 3")
my_junkyard.add("Diablo")

same = my_showroom.intersection(my_junkyard)

# print(same)

new_showroom = my_showroom.union(my_junkyard)

# print(new_showroom)

new_showroom.discard("Mustang")
print(new_showroom)