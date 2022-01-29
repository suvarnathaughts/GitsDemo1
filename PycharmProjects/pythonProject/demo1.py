a = 4
b = 6
print(a)
print(b)
str = "my name is suvarna"
print(str)
values = [1, 2, "suvarna"] # list datatype
print(values[0]) # 0th index value 1 will be printed
values.append("deore") #append means to add value in last index
print(values)#[1, 2, 'suvarna', 'deore']
del values[0] # to delet value of 0th index
print(values)#[2, 'suvarna', 'deore']
values.insert(3,"harshal")
print(values)
del values[3]
print(values)
values.insert(2, "harshal")
print(values)
