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
#** **
#*   *
#** **
#*****

n = 5  # Number of rows

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()  # Move to the next line

# i == 0 or i == n-1: This condition prints * in the first and last rows.
# j == 0 or j == n-1: This condition prints * in the first and last columns.
# i == j: This prints * on the main diagonal.
# i + j == n-1: This prints * on the anti-diagonal.