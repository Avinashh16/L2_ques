
def mindistance(arr,idx):
    min = 10000
    for i in arr:
        for j in idx:
            if abs(i-j) < min:
                min = abs(i-j)

    return min

def shortestdistance(src,c):

    h = {}
    n = len(src)

    for i in range(n):
        if src[i] in h:
            h[src[i]].append(i)

        else:
            h[src[i]] = [i]


    out = []

    for i in src:
        arr = h[i]
        idx = h[c]
        out.append(mindistance(arr,idx))

    return out







s = input("Enter Src: ")
c = input("Enter c: ")
src = []
for i in s:
    src.append(i)

print("src: ", src)
print("c: ", c)

output = shortestdistance(src,c)

print("output: " , output)