largest = -1
smallest = None
while True:
    num = input("Enter a number:")
    try:
        if sval = float (num):
            print "good"
    except:
        print ("Invalid input")
        continue
    if (sval > largest):
        largest = sval
    elif (smallest is None):
        smallest = sval
    elif (sval < smallest):
        smallest = sval
    if num == "done" :
        break

print ("Maximum is", largest)
print ("Minimum is", smallest)
