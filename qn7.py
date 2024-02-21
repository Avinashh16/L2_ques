#TO FIND WHETHER THE GIVEN STRING IS BALANCED OR NOT


def isBalanced(s):
    left = ['{','(','[']
    right = ['}',')',']']

    stack = []

    for i in s:
        if i in left:
            stack.append(i)
        elif i in right:
            if len(stack) == 0:
                return False
            else:
                topElement = stack.pop()
                if i == "}":
                    if not topElement == "{":
                        return False
                elif i == ")":
                    if not topElement == "(":
                        return False
                elif i == "]":
                    if not topElement == "[":
                        return False
                        
    if len(stack) == 0:
        return True
    else:
        return False    


s = "[()]{}{[()()]()}"
if isBalanced(s):
    print("Your String is balanced")
else:
    print("Your String is not balanced")