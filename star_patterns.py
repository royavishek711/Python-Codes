# *
# **
# ***

# user=int(input('Enter the number of rows: '))

# for i in range(1,user+1):
#     print('*'*i)

#  *
# ***
#*****

# user=int(input('Enter the number of rows: '))
# for i in range(1,user+1):
#     print(' '*(user-i)+'*'*(i*2-1))


#*****
#*   *
#*   *
#*   *
#*****

# rows=int(input('Enter the number of rows: '))
# for i in range(1,rows+1):
#     if i==1 or i==rows:
#         print('*'*rows)
#     else:
#         print('*'+' '*(rows-2)+'*')
num=int(input('Enter the number: '))
i=10
while i>0:
    print(f'{num} * {i}= {num*i}')
    i-=1

