print("Examole of List Operations 'Create' 'acsess' 'update' 'delete' ")
# Creating list
list = ["Samsung","iPhone","Poco","Vivo","Oppo"]
# accsess list
print(list)

print("The length of List is: ",len(list))

# remove items
list.remove("Vivo")
print("After removing item in list: ",list)

list.pop(1)
print("After Pop opration: ",list)

# add items
list.append("Realme")
print("After adding element: ",list)

list.extend("Linovo")
print("After adding element: ",list)

list.insert(1,2)
print(list)

#delete list
list.clear()
print(list)