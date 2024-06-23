# revision of list

list = [1,2,3,4]

#index
print("element at index 0 " ,list[0])

#change an elemet
list[1] = 10
print("lsit after changeing element", list)

#append
list.append(9)
print("list after appending", list)

#extend
list.extend([6,7])
print("list after extending", list)

#insert
list.insert(2, 8)
print("list after inserting", list)

#remove
list.remove(8)
print("list after removing", list)

#copy
list2 = list.copy()
print("list2 after copying", list2)

#clear list
list.clear()
print("list after clearing", list)

#sort
list2.sort()
print("list2 after sorting", list2)

#sorting is not prossbile for different kind of elements
# list3 = [1, 2, "a", "b", True]
# list3.sort()
# print("list3 before sorting", list3)
