def colourfill(arr,colour,index,n):

    q = [index]
    h = {}
    target = arr[index[0]][index[1]]
    while (len(q)!= 0):
        curr = q.pop(0)
        i = curr[0]
        j = curr[1]
        h[(i,j)] = True
        arr[i][j] = colour

        print("--------------------")

        for row in arr:
            print(*row)

        print("------------------")
        

        if j-1 >= 0:
            if arr[i][j-1]== target:
                if not (i,j-1) in h:
                    q.append([i,j-1])
                    h[(i,j-1)] = True
        if j+1 < n :
            if arr[i][j-1]== target:
                if not (i,j+1) in h:
                    h[(i,j+1)] = True
                    q.append([i,j+1])
        if i-1 >= 0:
            if arr[i-1][j] == target:
                if  not (i-1,j) in h:
                    q.append([i-1,j])
                    h[(i-1,j)] = True
        if i+1 < n:
            if arr[i+1][j]== target:
                if not (i+1,j) in h:
                    q.append([i+1,j])
                    h[(i+1,j)] = True

    
    return arr




n = int(input("Enter n : "))

arr = []
t = n
print("Enter Your Array")
while t:
    row = input().split()
    arr.append(row)
    t-=1

colour = input("Enter Colour To Fill: ")
i,j  = map(int,input().split(","))
index = [i,j]
out = colourfill(arr,colour,index,n)

for i in out:
    print(*i)


"""
R G G G G G R          
Y R R R R R Y
Y Y R R R Y Y
B B B R B B B
Y Y R R R Y Y
Y R R R R R Y
R G G G G G R
"""
