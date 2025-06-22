# str = "shivam"
# str2 = "gusain"
# print(str +  str2)
# str3 = "my name is shivam gusain"
# print(str3[-6 : -2])

# str = input("enter user name :")
# print("length of user name is :", len(str))
# str = "my $ name is ship$ gusai$n my$ $ s$"
# print(str.count("$"))

# num = int(input("enter a number :"))
# if(num%2==0):
#     print("num is even")
# else:
#     print("num is odd")

num1 = int((input("enter first no :")))
num2 = int((input("enter second no :")))
num3 = int((input("enter third no :")))
if(num1 > num2 and num1 > num3): 
    print("num 1 is greater")
elif(num2 > num1 and num2 > num3):
    print("num 2 is greater")
elif(num3 > num1 and  num3 > num2):
    print("num 3 is greater")
    