# my first sorting algorithm
list1 = [1,32,55,3,232,999,23]
list2 = []
temp1 = len (list1)
print (temp1)
for i in range(temp1):
    for j in range(temp1):
        if (list1[i] < list1[j]):
            #swap then
            temp2 = list1[i]
            list1[i] = list1[j]
            list1[j] = temp2
        #print one round
for p in list1:
    print (p)
print ("the second lowest number is ", list1[1])
