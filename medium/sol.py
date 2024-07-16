s = open("text.txt").readlines()[0]
alp = open("alphabet.txt").readlines()[0]
cnt = 0
for i in range(1,len(s)-1):
    ind_before = alp.index(s[i-1])%2
    ind_after = alp.index(s[i+1])%2
    if ind_before+ind_after==2:
        cnt += 1
print(cnt)
