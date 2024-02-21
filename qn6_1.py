def pairsum(arr,n,target):
    output = []

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                if arr[i] > arr[j]:
                    pair = [arr[j],arr[i]]
                else:
                    pair = [arr[i],arr[j]]
                output.append(pair)

    return output



n,s = map(int,input("Enter n,s :").split())
arr = list(map(int,input("Enter Array: ").split()))
output = pairsum(arr,n,s)
print(output)

k = len(output)

for i in range(k):
    for j in range(k ):

        if output[i][0]< output[j][0]:
            output[i],output[j] = output[j],output[i]
        elif output[i][0] == output[j][0]:
            if output[i][1] < output[j][1]:
                output[i],output[j] = output[j],output[i]

for i in output:
    print(i[0],i[1])