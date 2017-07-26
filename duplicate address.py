list1 = [1,2,2,3,4,5,5]
myval = input ("pass the input number: ")
val = float (myval)
pos = 0
occurence = 0
for i in list1:
    pos = pos + 1
    if (val == list[i]):
        temp = pos
        occurence = occurence + 1
    # break
print ("occurence of val, times, position in list", val , occurence , temp)
