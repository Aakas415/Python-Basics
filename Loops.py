print("Example of Loops.\n")

a=5
for i in range(0,a):
    print(i,end="\n")

#list elements
list = ["aakash","Jessy","Luffy"]

for i in list:
    print(i)

#tupal elements
t = ("Ram", "Sham")

for i in t:
    print(i)

#dictionary elements
d=dict()

d['steav- '] = 'FirstName'
d['harington- '] = 'LastName'

for i in d:
    print("%s  %s" %(i, d[i]))


# While Loop
count = 0
while(count<5):
    print("Guten Morgan")
    count= count+1

# Nesten Loops
# a=int(input("enter a: "))

for i in range(1,5):
    for j in range(i):
        print("* ",end=" ")
    print(" ")