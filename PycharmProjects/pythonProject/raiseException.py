Itemsincart = 0
# assert (Itemsincart==2) # this is the one way to fail the test
# the other way is to raise exception
if Itemsincart !=2:
    raise Exception("items in cart dont match")