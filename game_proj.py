import random

computer=['r','p','s']
s=random.choice(computer)

user=input('Enter your choice: Rock for r, Paper for p, Scissors for s: ')
print('Computer chooses:',s,'\nYou choose:',user)
if user==s:
    print('Oops it is a tie!')
elif (s=='s' and user=='r') or (s=='r' and user=='p') or (s=='p' and user=='s'):
    print('You won!')
elif (user=='s' and s=='r') or (user=='r' and s=='p') or (user=='p' and s=='s'):
    print('You loose!')
else:
    print('Enter a valid choice!')
    