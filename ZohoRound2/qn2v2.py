
def getscores(scores):
    
    for i in range(11):
        print(f"Player : {i+1} score: {scores[i]}")


def scores(s):

    n = len(s)
    i = 0

    players = [0,1,2,3,4,5,6,7,8,9,10]
    scores = ["DNB" for i in players]
    wickets = 0

    striker = players.pop(0)
    nonstriker = players.pop(0)
    p1 = 0
    p2 = 0
    extras = 0

    curr= True
    balls = 0
    while i < n:

        if s[i] in ['N','W']:
            extras += 1

        elif s[i] == ".":
            balls += 1

        elif s[i] == "X":
            balls += 1
            wickets += 1

            if wickets == 10:
                if curr:
                    scores[striker] = p1
                    scores[nonstriker]= str(p2)+"*"

                else:
                    scores[nonstriker] = p2
                    scores[striker] = str(p1)+"*"
                
                getscores(scores)
                return

            else:
                if curr:
                    scores[striker] = p1
                    p1 = 0
                    striker = players.pop(0)

                else:
                    scores[nonstriker] = p2
                    p2 = 0
                    nonstriker = players.pop(0)


        if s[i] in '123456':
            runs = int(s[i])
         
            if runs%2 == 1:
                balls +=1 
                if curr:
                    p1 += runs
                    curr = False
                else:
                    p2 += runs
                    curr = True
            elif runs% 2 == 0:
                balls += 1
                if curr:
                    p1+=runs
                else:
                    p2 += runs


        if balls == 6:
            balls = 0
            if curr:
                curr = False
            else:
                curr = True

        i+=1

    scores[striker] = str(p1)+"*"
    scores[nonstriker]= str(p2)+"*"

    getscores(scores)


s = "12345X612345X6123456WN...232.."
scores(s)