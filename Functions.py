def str_test(s):
    d={"UPPER_CASE" : 0, "LOWER_CASE" : 0}
    for cha in s:
        if cha.isupper():
            d["UPPER_CASE"]+=1
        elif cha.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("The orignal String is ",s)
    print("No. of upper case latters: ",d["UPPER_CASE"])
    print("No. of lower case latters: ",d["LOWER_CASE"])

str_test("I am Aakash and I am Good Boy")




















# from math import factorial


# def myfun(value):

#     factorial = 1

#     if value < 0:
#         print("Sorry, factorial does not exist for negative numbers :(")
#     elif value == 0:
#         print("The factorial of 0 is 1 |:")
#     else:
#         for i in range(1,value+1):
#             factorial = factorial * i
#         print("The factorial of ",value,"is ",factorial)

# myfun(7)


































# def myfun(value):
#     if value > 1:
#         for i in range(2,int(value/2)+1):
#             if (value % 1) == 0:
#                 print(value," is not prime number :(")
#                 break
#         else:
#             print(value," is prime number :)")
#     else:
#         print(value," is not prime number :(")

# myfun(56)




# print("Example of Fuctions.")
# # without Paramiterized Funtion
# def myfunc():
#     print("Hellow world.")

# myfunc()

#  # Paramiterized Funtion
# def myfunc(a,b):
#     print("The sum of a and b is: ",a+b)

# myfunc(5,7)

# # Funtion with return value
# def myfunc(a,b,c):
#     return a+b+c

# print("The sum is: ",myfunc(5, 7, 9))

# # def myfunc1(a,b,c):
# #     print("The sum is: ",a+b+c)
# #     return a+b+c
# #
# # myfunc1(9,7,8)
