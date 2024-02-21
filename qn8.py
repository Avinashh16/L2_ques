def circularrotation(arr):
    m = len(arr)
    n = len(arr[0])

    first = arr[0]

    for i in range(1,n):
        curr = []

        j = i%m
        
        k = 0

        while k < m :

            curr.append(arr[i][j])
            j = (j +1 ) % n
            k += 1
        #print(curr)
        if not curr == first:
            return False
        
    return True


arr = []

n = int(input("n = "))
print("Enter Array:")

while n :

    s = input().split()
    arr.append(s)
    n -= 1

print(circularrotation(arr))

            