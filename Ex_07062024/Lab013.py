# List data type
# it is similar to array

# It has Add item, remove item, update item, view item and exit item

Shopping_list = ["Milk", "Eggs", "Bread", "Butter"]
print(Shopping_list)
print(Shopping_list[0])
print(Shopping_list[-1])

# We can create list of different data types ie sting, int, boolen ect

#list = [1, 2, 3, 4.4, 5.6, True, "Siddhesh"]

Shopping_list.append("chocklate") #add item at the end of list
Shopping_list.remove("Eggs")#remove item from list
Shopping_list.insert(1, "Soup") #add item at specific index
Shopping_list.extend(["Maggi" "Pepsi"]) #add multiple item at the end of list

print(Shopping_list)
