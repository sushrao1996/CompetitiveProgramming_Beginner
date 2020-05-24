seconds=[66,57,54,53,64,52,59]
for j in range(len(seconds)):
    for i in range(len(seconds)-j-1):
        if seconds[i]>seconds[i+1]:
            seconds[i],seconds[i+1]=seconds[i+1],seconds[i]
print("Her best time is",seconds[0],"seconds")
