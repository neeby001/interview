f = open("cond.txt").readlines()[0]
f = f.replace("="," ")
d = f.split()
ful = ""
for i in range(len(d)):
    cur = d[i]
    new = cur[0]
    for j in range(len(cur)):
        if cur[j]=="-":
            new += cur[j+1]
    new += " "
    ful += new
print(len(ful)-1)
            
