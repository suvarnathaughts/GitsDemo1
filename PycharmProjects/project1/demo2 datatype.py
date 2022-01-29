values = [1, 2, "suvarna", 4, 5]
#List is data type that allows multiple values and can be of different datatypes

print(values[0])  #1

print(values[3])  #4

print(values[-1]) #to print last value

print(values[1:3]) # 2 suvarna

values.insert(3, "bhamare") #[1, 2, 'suvarna', 'bhamare', 4, 5]
print(values)
values.append("end")   #[1, 2, 'suvarna', 'bhamare', 4, 5, 'end']
print(values)
values[2] ="janhvi" # to update the value
print(values)
values[3] = "deore"
print(values)
del values[0]# to delet value
print(values)