# numeric datatype

# create variable with integer value

a = 100
print("the type of variable having value", a, "is", type(a))


# create variable with float datatype

b = 12.25
print("the type of variable having value", b, "is", type(b))

# create a variable with complex value

c = 100+3j
print("type of variable having value", c, "is", type(c))




# sring datatype
# string can be in single or double inverted comma

a = ("string in double inverted coma")
b = ('srting in single inverted coma')
print(a)
print(b)

# concatenate two or several strings use ','

print(a,"concatenated with",b)

#'+' to concate the two or several strings

print(a+ "concated" +b)

# python list datatype
# list is an orderd datatype sequence of some data written using square braces and commas

# list of having  only integers
a = [1, 2, 3, 4, 5]
print(a)

# list of having only strings
b = ["hello", "john", "reese"]
print(b)

# list having both integer and string
c= ["hey", "you",1, 2, 3, "go"]
print(c)

# index are 0 based
print(c[2])


# python tuple datatype
# data in tuple written in parenthesis and comma , patenthesis means round brackets
# difference between tuple and list is  tuple is immutable that is write protected
# tuple having only integers
a = (1, 2, 3, 4)
print(a)

# tuple having multiple datatype

b = ("hello", 1, 2, 3, "go")
print(b)
# tuple also having 0 base index

print(b[3])


# python dictionary datatype
# it is unordered sequence of data of key : value form
# dictionaries written in curly braces {key:value}

a = {1:"first name", 2:"last name", "age": 33}
print(a)
# print value having key = 1
print(a[1])

#print value having key =2
print(a[2])
#print value having key "age"
print(a["age"])

# different functions of string datatype

str = "suvarnaharshaldeore"
#if we want to print single character from string
print(str[4])
# if we want to print substring in string
print(str[0:7])

str1 = "pythondeveloper"
# concatenation
print(str + str1)
print(str,str1)
# validation of one string present in other
str3 = "harshal"
print(str3 in str)
str4 = "bhamare"
print(str4 in str)
#how to split string
#use str.split("write the character from where you want to split the string")
var = str.split("harshal")
print(var)
#trim or strip to remove white spaces in front or back
print(str.strip())
print(str.lstrip())
print(str.rstrip())






