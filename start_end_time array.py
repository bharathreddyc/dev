tup1 = [(6,8),(1,9),(2,4)]
list2 =[]
for i in tup1:
    (x, y) = i
    print (x)
    print (y)
    list2.append(x)
    list2.append(y)
    #comment
#comment
list2.sort()
startbit = list2[0]
endbit = list2[-1]
print ("list", startbit, endbit)
