def scores(s):
    overs = []

    n = len(s)
    i = 0

    p1 = 0
    p2 = 0
    extras = 0

    curr= True
    balls = 0
    while i < n:

        if s[i] in ['N','W']:
            extras += 1
        elif s[i] in ['1','3','5']:
            balls += 1
            if curr:
                p1 += int(s[i])
                curr = False
            else:
                p2 += int(s[i])
                curr = True
            

        elif s[i] in ['2','4','6']:
            balls += 1
            if curr:
                p1+=int(s[i])
            else:
                p2 += int(s[i])


        elif s[i] == ".":
            balls += 1

        if balls == 6:
            balls = 0
            if curr:
                curr = False
            else:
                curr = True


        i+=1

    
    print("P1 - ",p1)
    print("P2 - ",p2)
    print("Extras - ",extras)



s = "111111111111111"
scores(s)