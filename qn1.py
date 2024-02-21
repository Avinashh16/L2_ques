#PROGRAM TO CHECK WHETHER THE GIVEN STRING IS A PALINDROME

def isPalindrome(s):
    i = 0
    j = len(s)-1

    while i <= j :
        if not s[i] == s[j]:
            return False
    
        else:
            i+=1
            j -=1

    return True

s = input("Enter your String: ")
if isPalindrome(s):
    print("Your String is a palindrome")
else:
    print("Your String is not a palindrome")