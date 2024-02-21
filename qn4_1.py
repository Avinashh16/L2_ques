def shortestdistance(src,c):
    n = len(src)
    out = []
    for i in range(n):
        min = 10000
        for j in range(n):
            if src[j] == c:
                min = abs(i-j) if abs(i-j) < min else min
        
        out.append(min)

    return out




s = input("Enter Src: ")
c = input("Enter c: ")
src = []
for i in s:
    src.append(i)

print("src: ", src)
print("c: ", c)

output = shortestdistance(src,c)
print(output)