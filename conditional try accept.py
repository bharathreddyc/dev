# compare try accept block
rawstr = input ('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if (ival > 0) :
    print ('great')
else:
    print ('not a number')

astr = 'Bob'
try:
    print ('i am in the block')
    istr = int(astr)
    print ('There)'
except:
    istr = -1
