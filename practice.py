# name =(input("Enter your name: "))
# print("Good morning",name)
# # other ways to print
# print(f"Good morning {name}")
# print("Good morning {}".format(name))

# name =(input("Enter your name: "))
# date =(input("Enter your date: "))

# print(f'''Your name is {name} 
# Your date is {date}''')

# name='''
# My name is Avishek
# I am from India
# '''

# Name=input("Enter your name: ")
# Loc=input("Enter your location: ")

# print(name.replace("Avishek",f"{Name}").replace("India",f"{Loc}"))

#to find a double space in a string
# name ="I am  AVSIH     md"
# print(name.find("   "))
# print(name.replace("  "," "))

# print('Dear sir,\n\tI\'m Avishek Roy.\nBest Regards,\nAvishek Roy')

#list tuple practice
# list=[]
# i=0
# while i<7:
#     user=input('Enter fruit name: ')
#     list.append(user)
#     i+=1

# print(list)

# list=[]
# i=1
# while i<7:
#     user=int(input(f'Enter the marks of student {i}: '))
#     list.append(user)
#     i+=1
# list.sort()
# print(list)

# list=[]
# i=1
# while i<5:
#     user=int(input(f'Enter the number {i}: '))
#     list.append(user)
#     i+=1
# print(list)
# print(sum(list))

# tup=(1,2,3,4,5,1,2,3,4,51,2,3,4,5)
# user=int(input('Enter the number to count: '))
# cnt=tup.count(user)
# print(cnt)

#dictionary & sets practice
# user_dict={
#     'billy':'cat',
#     'kutta':'dog',
#     'sher':'lion',
#     'aam':'mango',
#     'gadi':'car'
# }

# user=input('Naam bataye jiska meaning jaan na h aapko: ')
# print(user_dict.get(user))

# user_set={}
# user_set=set()
# i=0
# while i<8:
#     user=input("enter the num: ")
#     user_set.add(user)
#     i+=1

# print(user_set)

# user_set={18, '18'}
# print(user_set)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)

# d={}
# i=0
# while i<5:
#     name=input('Enter your name: ')
#     sub=input('Enter your subject: ')
#     d.update({name:sub})
#     i+=1

# print(d)

# conditonal statements greatest number
# num1=int(input('Enter the first number: '))
# num2=int(input('Enter the 2nd number: '))
# num3=int(input('Enter the 3rd number: '))
# num4=int(input('Enter the 4th number: '))

 
# #1st approach
# if num1>num2 and num1>num3 and num1>num4:
#     print(num1,'is greater')

# elif num2>num1 and num2>num3 and num2>num4:
#     print(num2,'is greater')

# elif num3>num1 and num3>num2 and num3>num4:
#     print(num3,'is greater')

# else:
#     print(num4,'is greater')

# #2nd approach
# max_num = max(num1, num2, num3, num4)

# print(max_num, 'is greater')

# # 3rd approach
# greater=num1

# if num2>greater:
#     greater=num2
# elif num3>greater:
#     greater=num3
# elif num4>greater:
#     greater=num4

# print(greater,'is greater')

# marks1=int(input('Enter the marks of math: '))
# marks2=int(input('Enter the marks of chem: '))
# marks3=int(input('Enter the marks of phy: '))

# if (marks1+marks2+marks3)>=120 and marks1>=33 and marks2>=33 and marks3>=33:
#     print('pass')
# else:
#     print('fail')

# user=input('Enter the comment: ')
# if user.__contains__('buy now') or user.__contains__('make a lot of money') or user.__contains__('subscribe this') or user.__contains__('click this'):
#     print('spam')

# #other approach
# if 'buy now' in user or 'make a lot of money' in user or 'subscribe this' in user or 'click this' in user:
#     print('spam')


# #other approach

# # List of spam keywords or phrases
# spam_keywords = ['buy now', 'make a lot of money', 'subscribe this', 'click this']

# # Check if any spam keyword is in the user's comment
# if any(keyword in user for keyword in spam_keywords):
#     print('spam')

# user=input('enter the username: ')
# if len(user)<10:
#     print('username is not valid')
# else:
#     print('username is valid')

# user=input('enter the name: ')

# list=['avi', 'rimon', 'rup', 'priya', 'deb', 'deep']

# if list.__contains__(user):
#     print('present')
# else:
#     print('not present')


# marks=int(input('enter the marks: '))
# if marks<=0 or marks>100:
#     print('invalid marks')
# elif marks>=90 and marks<=100:
#     print('Grade: EX')
# elif marks>=80 and marks<90:
#     print('Grade: A')
# elif marks>=70 and marks<80:
#     print('Grade: B')
# elif marks>=60 and marks<70:
#     print('Grade: C')
# elif marks>=50 and marks<60:
#     print('Grade: D')
# elif marks<50:
#     print('Grade: F')

str=input('enter the post: ')
if 'harry' in str.lower():
    print('Yes')
else:
    print('no')