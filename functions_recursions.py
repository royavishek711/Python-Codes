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

# prime number using recursion

