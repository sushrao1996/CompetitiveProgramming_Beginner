def busSys(noOfPeople,noOfDays):
    if noOfDays==0:
        return 0
    else:
        return noOfPeople+busSys(noOfPeople,noOfDays-1)

noOfPeople=1200000
noOfDays=365
print(busSys(noOfPeople,noOfDays))

