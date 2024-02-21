def substringsum(s,target):

    out = []
    n = len(s)

    i = 0
    j = 0
    curr = 0

    while j < n:
        curr = curr + ord(s[j])- ord('a')+1 
        
        if curr == target:
            out.append(s[i:j+1])
            curr = curr - (ord(s[i])- ord('a')+1 )
            i+=1
            j+=1
        else:

            while i < j and curr > target:
                curr = curr - (ord(s[i])- ord('a') +1 )
                i+=1
 
                if curr < target:

                    curr = curr + (ord(s[i])-ord('a')+1)
                    i-=1
                    break

            j+=1


    return out

out = substringsum("zohocorpopration",41)
out2 = substringsum("machinelearning",55)
print(out)
print(out2)