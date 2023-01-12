# Basics
# The file is connected is aakash.txt


"""
r- read mode -[default]
w- write Mode
x- create file if not exist
t- text file -[default]
b- binary mode
+- read and write mode

"""


# f= open("aakash.txt","w")

# ONLY READING

# con = f.read()
# print(f.readlines())
# print(con)

# for con in f:
#     print(con)


# ONLY WRITING

# a= f.write("Aakash file is updated..!\n")
# print("Updated..!")

# print(a)

#WRITING AND READING BOTHE
f = open("aakash.txt", "r+")
print(f.read())
f.write("Here we go")

f.close()

