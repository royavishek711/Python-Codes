#factorial using recursion

# def fact(num):
#     if num==1 or num==0:
#         return 1
#     return num*fact(num-1)

# user = int(input('enter a num: '))
# print(fact(user))

#-----------------------------------------------------------------------------------------------------

#fibonacci series using recursion

# def fibo(num,prev,curr):
#     if num<=2:
#         return 1
#     res=prev+curr
#     print(res,end=' ')
#     return res+fibo(num-1,curr,res)

# num=int(input('Enter the number: '))
# prev=0
# curr=1
# if num<=0:
#     print('Enter a valid number')
# elif num==1:
#     print(prev)
# else:
#     print(prev,curr,end=' ')
#     fibo(num,prev,curr)

# using loop logic
# for i in range(num-2):
#     res=prev+curr
#     print(res)
#     prev=curr
#     curr=res

#----------------------------------------------------------------------------------------------

# find greatest number
# def greatest(n1,n2, n3):
#     if n1>n2 and n1>n3:
#         return n1
#     elif n2>n1 and n2>n3:
#         return n2
#     else:
#         return n3

# n1,n2,n3=map(int,input('Enter three numbers: ').split())
# print(greatest(n1,n2,n3))

#----------------------------------------------------------------------------------------------

# fahrenheit to celcius

# def f_to_c(fahr):
#     return ((fahr-32)*5/9)

# def c_to_f(cel):
#     return (cel*(9/5)+32)

# user=input('Enter the temp unit in f or c: ')
# if user=='f':
#     print(f_to_c(float(input('Enter the temp in f: '))))
# elif user=='c':
#     print(c_to_f(float(input('Enter the temp in c: '))))
# else:
#     print('Invalid option')

# -----------------------------------------------------------------------------------------------

# sum of n natural numbers

# def sum_of_n(n):
#     if n==0:
#         return 0
#     return n+sum_of_n(n-1)

# n=int(input('Enter the n natural number: '))
# print(f'sum of first {n} natural numbers are: {sum_of_n(n)}')

# -----------------------------------------------------------------------------------------------

# pattern using recursion
# ***
# **
# *

# def pattern(n):
#     if n==1:
#         return '*'
#     print('*'*n)
#     return pattern(n-1)

# n=int(input('Enter the num of rows: '))
# print(pattern(n))

# -----------------------------------------------------------------------------------------------

#remove a word from a list

# def rm_word(lst,word):
#     newlst = []
#     for i in lst:
#         if i!=word:
#             newlst.append(i.strip(word))
#     return newlst

# lst=['hello','world','my','name','is','Avishek','world','Avishek','rimon','hello']
# word=input("Enter the word to remove: ")
# print(rm_word(lst,word))

# -----------------------------------------------------------------------------------------------

#multiplication table using recursion

# def table(num,n):
#     if n<=10:
#         print(f'{num} * {n} = {num*n}')
#         return table(num,n+1)
#     else:
#         return
# num=int(input('enter the num for table: '))
# table(num,1)
