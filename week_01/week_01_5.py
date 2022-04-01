s = int(input())
tlqkf = [1,2]
for i in range (2,s):
    tlqkf.append(tlqkf[i-1]+tlqkf[i-2])
print(tlqkf[s-1]% 10007)