
def pairsum(arr,n,s):
    
    arr = sorted(arr)

    i = 0
    j = n-1

    out = []

    while i < j :
        curr = arr[i]+arr[j]

        if curr == s:
            pair = [arr[i],arr[j]]
            out.append(pair)
            if arr[i+1]== arr[i]:
                i+=1
            elif arr[j-1]==arr[j]:
                j -=1
            else:
                i+=1
                j-=1

        elif curr > s:
            j -=1

        else:
            i+=1


        

        
    return out



n,s = map(int,input("Enter n,s :").split())
arr = list(map(int,input("Enter Array: ").split()))
output = pairsum(arr,n,s)
for i in output:
    print(i[0],i[1])
