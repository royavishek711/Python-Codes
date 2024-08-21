# import random 

#find a word present in another text file

# user=input('Enter the word to find: ')
# with open("poem.txt","r") as file:
#     content=file.read()
#     if (user in content.lower()):
#         print('word is present')
#     else:
#         print('not present')

#-----------------------------------------------------------------------------------------------------

#updating game high score

# def game():
#     score=random.randint(1,100)
#     print(f'your score: {score}')
#     with open('hi_score.txt', 'r') as file:
#         content = file.read()
#         if content!='':
#             content=int(content)
#         else:
#             content=0
#     if score>content:
#         with open('hi_score.txt','w') as file:
        
#             file.write(str(score))
#             print('score updated')
#     else:
#         print('your score is not updated')
# game()

#------------------------------------------------------------------------------------------------

#generate multiplication tables from 2 to 19 in different text files within a single folder

# def mul_table(n):
#     tab=''
#     for i in range(1,11):
#         tab+=f'{n} x {i} = {n*i}\n'
#     with open(f'tables/table_{n}.txt','w') as f:
#         f.write(tab)

# for i in range(2,20):
#     mul_table(i)

#------------------------------------------------------------------------------------------------

#replace word in a text file

# with open('poem.txt','r') as f:
#     content=f.read()

# with open('poem.txt','w') as f:
#     new_content=content.lower().replace('donkey','####') 
#     new_content=' '.join(new_content.split()) #remove extra spaces
#     f.write(new_content)

#-----------------------------------------------------------------------------------------------

#replace multiple words in a text file

# words=['donkey', 'cat', 'dog']

# with open('poem.txt','r') as f:
#     content=f.read()

# with open('poem.txt','w') as f:
#     for word in words: #traverse the list
#         content=content.lower().replace(word,'####')
    
#     content=' '.join(content.split()) #remove extra spaces
#     f.write(content)

#---------------------------------------------------------------------------------------------

#find a word and line no present in a text file

# with open('poem.txt','r') as f:
#     lines=f.readlines()

# lineno=1
# for line in lines:
#     if 'python' in line:
#         print('python is present in line no:', lineno)
#         break
#     lineno+=1
# else:
#     print('python is not present in any line')

#---------------------------------------------------------------------------------------------

#make a copy of txt file

# with open('poem.txt','r') as f:
#     content=f.read()

# with open('copy.txt','w') as f:
#     f.write(content)

#---------------------------------------------------------------------------------------------

# content of two files are same or not

# with open('poem.txt','r') as f:
#     content1=f.read()

# with open('copy.txt','r') as f:
#     content2=f.read()

# if (content1==content2):
#     print('files are identical')
# else:
#     print('files are not identical')

#-----------------------------------------------------------------------------------------------

#rename a file

# import os

# os.rename('copy1.txt', 'copy.txt')