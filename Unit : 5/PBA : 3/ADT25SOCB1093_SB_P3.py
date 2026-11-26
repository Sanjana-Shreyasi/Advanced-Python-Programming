#PBA 3
#Section B
#Q3

f=open("lines.txt","r")
long_ln=""
ln_no=0
count=0

for i in f:
    ln_no+=1

    if len(i)>len(long_ln):
        long_ln=i
        count=ln_no

print("LoOngest line is:",long_ln.strip())
print("Linee no:",count)

f.close()

#Output
'''LoOngest line is: File handling is an important topic.
Linee no: 2'''


