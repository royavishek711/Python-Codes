num=int(input('Enter the number: '))
res=1
for i in range(2,num+1):
    res*=i

print(f'The factorial of {num} is {res}')