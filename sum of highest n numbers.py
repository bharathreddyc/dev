# largest(1, [1,2,3]) == [3]
# largest(3, [3,1,8,9,2]) == [3,8,9]

list1 = [3,344,56,335,243,33,43]
list1.sort(reverse=True)
val = input ("enter how many numbers:")
myval = int(val)
list2 = []
print ("length of the list is : ", len(list1))
for i in range(myval):
    print ("The numbers are: ", list1[i])
    list2.append(i)
