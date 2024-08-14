name ="Avishek"
# to get the length of the string
print (len(name))
# string indexing normal start from 0
print(name[0])
#  we can also do negative indexing start from -1
print(name[-1])
#  we can also do slicing
print(name[0:4]) # it will print from 0 to 3rd index excluding 4th index
# slicing using negative indexing
print(name[-4:-1])
print(name[-1:-4]) # it will print nothing
print(name[:6]) # it will automatically print from 0 to 5rd index excluding 6th index
print(name[2:]) # it will automatically print from 2 to last index
# jump slicing
print(name[1:7:2]) # it will print from 1 to 6th index excluding 7th index with a jump of 2


# most used functions in string

sample="helLo,Wor ld: m"
print(len(sample))
print(sample.lower()) # it will convert the string to lower case
print(sample.upper()) # it will convert the string to upper case
print(sample.find("l")) # it will return the index of the string
print(sample.find("Wor"))
print(sample.find("n")) # it will return -1 if the string is not found
print(sample.replace("Wor","Universe")) # it will replace the string
print(sample.split()) # it will split the string
print(sample.split(":")) # it will also split the string based on a separator.
print(sample.split(",")) # it will also split the string based on a separator.
print(",".join(sample)) # it will join the string based on a separator
print(sample.count("l")) # it will count the number of times a string is present in the string
print(sample.count("World"))
print(sample.startswith("H")) # it will return true if the string starts with the given string
print(sample.startswith("h"))
print(sample.startswith("Hell"))
# same happens with endswith
print(sample.strip()) # it will remove the spaces from the beginning and end of the string
print(sample.capitalize()) #it will capitalize the first letter of the string and the rest will be in lower case
