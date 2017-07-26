#program to prompt for user for hours
hrs = input ("Enter Hours:")
rate = input ("Enter hourly rate:")
try:
    h = float (hrs)
    r = float (rate)
except:
    print ("Error, please enter numberic input")
    quit ()

z = 40
y = 0
if (h > 40) :
    y = float (h - 40)
total  =  z * r + y * (1.5 * r)
print (total)
