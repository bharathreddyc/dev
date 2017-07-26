largest = -1
smallest = None
iterator = 0
sum1 = 0
Temp = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    sval = float(num)
    #print (sval)
    try:
        if sval == float(num):
            print ("good")
    except:
        print("Invalid input")
        continue
    if (sval > largest):
        largest = sval
    elif (smallest is None):
        smallest = sval
    elif (sval < smallest):
        smallest = sval
    iterator = iterator + 1
    sum1 = sum1 + sval
    average = sum1 / iterator

print ("Smallest", smallest)
print ("Maximum", largest)
print ("total elements", iterator)
print ("total sum", sum1)
print ("average of all",average)
