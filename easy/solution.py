f = open("text_after.txt").readlines()[0]
f = f.replace("...","0000")
f = f.replace(",",", ")
f = f.replace(".",". ")
print(len(f.split()))

