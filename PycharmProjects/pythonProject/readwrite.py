file = open('test.txt')
# print(file.read()) # to read contents from text file
# now we will see how to read single line
#print(file.readline())
#print(file.readline())
#print(file.readline())
# all this inmp for INTERVIEW

# print line by line using while loop
#line = file.readline()
#while line!="":
   # print(line)
 #   line = file.readline()

for line in file.readlines():
    print(line)



file.close()