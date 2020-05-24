TotalNoOfHD=400
TotalNoOfHDPerContainer=8
packages=0
while TotalNoOfHD>0:
    TotalNoOfHD-=TotalNoOfHDPerContainer
    packages+=1
    
print(packages)    
