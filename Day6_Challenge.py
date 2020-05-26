f=int(input("Enter the number of free bytes: "))
u=int(input("Enter the number of used bytes: "))
o=int(input("Enter the number of bytes of old file: "))
n=int(input("Enter the number of bytes of new file: "))
Totalspace=f+u
UsedSpaceAfterDeleting=u-o
UsedSpaceAfterCreating=UsedSpaceAfterDeleting+n
FreeSpace=Totalspace-UsedSpaceAfterCreating
print("Free bytes available in the floppy disk are",FreeSpace)
