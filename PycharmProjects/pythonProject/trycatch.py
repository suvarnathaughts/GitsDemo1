
try:
   with open('filelog.txt', 'r') as reader:
        reader.read()
#except:
   # print("some how i reached to this block because there is failure in try block")
except Exception as e:
    print(e)      # this is the way to know error without test fail
# finally key is also used along with try except

