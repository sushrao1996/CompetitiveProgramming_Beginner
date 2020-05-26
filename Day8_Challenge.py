def avgWrk(a,b,c,d,e,f,totalnumberOfNurse):
    totalHours=float(a+b+c+d+e+f)
    averageNofOfHoursePerNurse=totalHours/numberOfNurse
    return averageNofOfHoursePerNurse

Howard=8
Pease=10
Campbell=9
Grace=8
McCarthy=7
Murphy=12
numberOfNurse=6
averageNofOfHoursePerNurse=avgWrk(Howard,Pease,Campbell,Grace,McCarthy,Murphy,numberOfNurse)
print("Average Hours:",averageNofOfHoursePerNurse)
