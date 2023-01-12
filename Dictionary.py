print("Examole of Dictionary Operations 'Create' 'access' 'update' 'delete' ")
# Creating dic
mydic = dict()

mydic = {
    "Brand":"Ford",
    "Model":"GT100",
    "Year": "1990"
}

# Acsses items
print(mydic)
print(len(mydic))
print(mydic['Model'])

a=mydic.get('Year')
print(a)

# add items
a = mydic.keys()
mydic["Color"] = "Blue"
print(a)
print("After addition:\n",mydic)

# Update items
mydic.update({"Year":2020})
print("After Update:\n",mydic)

# Delete items
del mydic["Color"]
print("After deletion:\n",mydic)

# copy dictionary to other dic
thisdict = dict()

thisdict={
    "Brand": "BMW",
    "Model": "XUV100",
    "Year": "2021"
}

# thisdict = dict(mydic)
# print("\n\n",thisdict)
mydic = thisdict.copy()
print("\n",mydic)