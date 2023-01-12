print("Examole of Set Operations 'Create' 'access' 'update' 'delete' ")
#crete set
thisset= {"Apple","Banana","Cherry"}

#acses set
for i in thisset:
    print(i)
    # print("Cherry" in thisset)

# add items in set
thisset.add("Mango")
print(thisset)

# update sets
thisset2 = {"Pineapple","Papaya"}
thisset.update(thisset2)
print(thisset)

# Delete items in set
thisset.remove("Banana")
print(thisset)

thisset3 = {"Potato","Pudina"}

#union use
thisset4 = thisset2.union(thisset3)
print(thisset4)