# tuples are immutable like strings 
my_tuple=(2, 1, 5, 'avishek', 2,  'cse', 'python', 'iem', True)
new_tup=('bhim', 3, 'aru', False, 6)
# tup=my_tuple.count(1) 
#However, in Python, True is considered equivalent to 1 when counting or comparing because True has an integer value of 1.
# tup=my_tuple.index('avishek')
# tup=my_tuple[2:5]
#You can concatenate tuples using the + operator.
# tup=my_tuple+new_tup 
#You can repeat a tuple multiple times using the * operator.
# tup= new_tup*2
# Tuple Unpacking
# You can assign the elements of a tuple to multiple variables in a single statement.
# a,b,c,d,e=new_tup
# print(a,b,c,d,e)
#You can check if an item exists in a tuple using the in keyword.
# print('karn' in new_tup)
# print(len(new_tup))
num_tup=(-2,2,34,12,56,3,78,69)
# print(max(num_tup))
# print(min(num_tup))
#You can convert a tuple to a list using the list() function, which allows you to modify the elements.
# list=list(new_tup)
# print(list)
# You can use the sum() function to find the sum of all elements in a tuple containing numeric values.
print(sum(num_tup))