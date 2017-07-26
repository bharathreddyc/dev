#fibonacci series

fibn = input ("please enter the number you want:")
fibn = float (fibn)

val1 = 0
val2 = 1
temp1 = val1 + val2

while temp1 < fibn:
    temp1 = val1 + val2
    print (temp1)
    val1 = val2
    val2 = temp1
print ("completed")
