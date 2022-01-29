# it always use along with try except method
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except:
    print('i came here because try block not run')

finally:
    print('clear all record')
# even though code will not run at except block due to some reason control will reach to finally and run the code which we give under it