shopping_list_wife = ["eggs", "milk", "bread", "butter", "cheese"]
shopping_list_husband = ("eggs", "milk", "bread", "butter", "cheese")
print("Wife's shopping list (list):", shopping_list_wife)
print("Husband's shopping list (tuple):", shopping_list_husband)
# Modifying the wife's shopping list
shopping_list_wife.append("apples")
print("Wife's modified shopping list (list):", shopping_list_wife)
# Trying to modify the husband's shopping list (will raise an error)

#convert tuple to list to modify
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
my_list = list(my_tuple)
print(my_list)

my_list.append("orange")
print(my_list)

#convert back to tuple
my_tuple = tuple(my_list)
print("after converting back to tuple" , my_tuple)


#create empty tuple
empty_tuple = ()
print("empty_tuple :", empty_tuple)
print("type of empty_tuple :", type(empty_tuple))


hero1 = ("Superman", "Clark Kent", "Metropolis")
hero2 = ("Batman", "Bruce Wayne", "Gotham")
new_heroes = (hero1, hero2)
print("New Heroes Tuple:", new_heroes)

