#program to prompt for user for hours
score = input ("Enter score:")
hr1 = float (score)
try:
    if (hr1 < 0) :
        print ("good")
    if (hr1 > 1.0) :
        print ("bad")
except:
    print ("Error, please enter score betwen 0.0 and 1.0 ")
    quit ()

def thing (hr):
    if (hr >= 0.9) :
        print ("A")
    elif (hr >= 0.8) :
        print ("B")
    elif (hr >= 0.7) :
        print ("C")
    elif (hr >= 0.6) :
        print ("D")
    elif (hr < 0.6) :
        print ("F")

thing (hr1)
print ("completed")
