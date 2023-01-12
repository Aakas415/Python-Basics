a=int(input("enter a: "))

for i in range(a):
    for j in range(i+1):
        print("* ",end=" ")
    print("\n")    
    
for i in range(a):
    for j in range(i+1):
        print(j+1 ,end=" ")
    print("\n")    
    
ascii_value=65

for i in range(a):
    for j in range(i+1):
        alpha=chr(ascii_value)
        print(alpha ,end=" ")
    ascii_value += 1
    print("\n")    

