# print("namashkar")
#a = "12"
#a = int(a)
#print(type(a))
#print(bool(a))
# a = 134
# b = 23
# a = str(a)
# print(type(a))
# print(bool(b))
# a = tuple(a)
# print(type(a))
# a = input("enter your fucking name : ")
# b = input("enter your age : ")
# print("thank you fucking", (a) )
# print(f"thank you fucking {a} and you will be cracked for 69 times soon {b} ")
# a = "aman"
# b = 12
# c = "fuvked"
# d = "get"
# e = "tonight"

# print(a)
# print(b)
# print(c)
# print(a,b,c)
# print(a,d,c,e)
# a = 3
# b = 4
# print(a)
# print(b)
# print(a+b)
# print(a-b)
# print(a/b)
# print(a//b) #flow division
# print(a*b)
# print(a**b) #power of a to b
# print(48%4) #remainder
# #BODMAS
# print(13+67-6*24/8)
# a = 34
# #compound assignment operation
# a = a + 34
# or
# a += 34
# a = a + 29
# #or
# a += 29
# a-= 29
# a*= 29
# a/= 29
# a//= 29

# print(a)
# num1 = int(input("enter first number : "))
# num2 = int(input("enter second number : "))
# if num1 > num2 :
#     print(f"{num1} is greater than {num2}")
# elif num2 >num1 :
#     print(f"{num2} is greater than {num1}")
# else: print("both numbers are equal")
# gen = (input("Enter the gender (M or F) : "))
# if gen == 'M':
#     print("good morning sir")
# elif gen== 'F':
#     print("good morning mam")
# else :
#     print("undefined gender")
# a = int(input("enter a number"))
# if a%2 ==0:
#     print("number is even")
# else : print("numver is odd")
#check leap year
# year = int(input("enter the year"))
# if year%100==0 and year%400==0:
#     print("its a leap year")

# elif year%100!=0 and year%4 ==0:
#     print("its a leap year")
# else:
#     print("its a normal year")
# n = int(input("enter a number : "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
#     else: 
#         odd=odd+i
# print(f"your even and odd are {even},{odd}")
# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     print(i)
# n = int(input("enter the number :"))
# for i in range(n,0,-1):
#     print(i)
# n = int(input("Enter the number : "))
# for i in range(1,11):
#     print(f"{n}*{i} = {n*i}")
# n = int(input("enter the number : "))
# sum=0
# for i in range (0,n+1):
#     sum=sum +i
# print(f"the sum is {sum}")
# n= int(input("enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact= fact*i
# print(f"the factorial is {fact}")
# n = int(input("enter the number : "))
# for i in range (1,n+1):
#     if n%i==0:
#         print(i)
# n= int(input("enter the number: "))

# sum=0

# for i in range(1,n):
#     if n%i==0:
#      sum=sum+i

# if sum==n :
#     print("your number is a perfect square")

# else: 
#     print("number is not a perfect square")


# n= int(input("enter the number: "))
# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count==2:
#     print("number is a prime number")
# else :
#     print("number is not a prime number")
# a = "Anush is great"
# print(a[14::-1])

# a = "Anush IS Great"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])
# n = (input("enter the number"))
# if n== n[::-1]:
#     print("the number is palindrone")
# else :
#     print("its not palindrone")
# a = "jerheuf1233@!#@!#"

# char=0
# dig=0
# spchr=0
# for i in a:
#     if i.isdigit():
#         dig+= 1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+= 1
    
# print(f"your digits are {dig}\n your alphabet are {char}\n your spchar are {spchr}")
# l =[43,53,6,4,-5,-45,45,-65]
# print("positive elements are :")
# for i in l:
#     if i>=0:
#         print(i)
# print("these are negavite elements:")
# for i in l:
#     if i<0:
#         print(i)
# l =[23,344,53,23,53]
# sum=0
# for i in l:
#     sum += i
# print(sum/len(l))

# l = [23,34,34,233,565,34]
# largest =l[0]
# index=0
# for i in range(len(l)):
#    if l[i]> largest:
#       largest =l[i]
#       index =i
# print(f"largest number is {largest} at index {index}")
# for i in range(10):
#     if i==4:
#         pass
#     else :print(i)
# for i in range(20):
#     print(i)
# n = int(input("enter tne number"))
# num=n
# if n>0:
#  for i in n(len(n)-1,-1,-1):
#     print(num)
a ="Anush is God"
print(a[12::-1])
