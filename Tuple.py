print("Examole of tuple Operations 'Create' 'access' 'update' 'delete' ")

t =(2,3,4,5,6)
print(t)
print(type(t))

print(t[2])
print(t[:3])

t_add = t+(7,8,9)
print(t_add)
print(t)

"""
For update or insert items in tuple 
we need to cunvert this tuple into list and again cunvert as tuple
This is example
"""
l=list(t)   #Converting tuple to list
l.insert(11,12)
print(l)

#remove element
l.remove(2)
print(l)
# Update value 3 as 8
l[1] = 8
print(l)

c_t= tuple(l)   #Converting list to tuple
print(c_t)

