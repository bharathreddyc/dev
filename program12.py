def computepay (h,r):
    ab40 = 0
    if (h > 40):
        ab40 = h - 40
    total = ab40 * (r + r / 2) + 40 * r
    return total
hrs = input ("Enter hours:")
h = float (hrs)
rps = input ("Enter rate per hour")
r = float (rps)
p = computepay (h,r)
print ("pay", p)
