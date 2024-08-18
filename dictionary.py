user={
    "name":'Avishek',
    'roll':220,
    'dept':'cse',
    'id':22020002002021,
    'year':'4th',
    'college':'IEM',
    "CGPA":9.1,
    'city':'kolkata',
    'Ph. no':9064599810,
    'mail':'royavishek711@gmail.com'
}

# print(user)
# print(user.get('roll'))
user.update({'name':'Rimon', 'company':'Accenture'})
# print(user.keys())
# POP Removes the key and returns its value. If the key is not found, it returns the default value (or raises a KeyError if no default is provided).
# print(user.pop('mail'))
# print(user.pop('password')) #error
# popitem(): Removes and returns the last key-value pair as a tuple. Raises a KeyError if the dictionary is empty.
# print(user.popitem())
# setdefault(key, default): Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
user.setdefault('Gender','male')
new_user=user.copy()
new_user.clear()
print(new_user)