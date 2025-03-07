def palindrome(a):
    a=a.lower().replace(" ", "")  
    return a==a[::-1] 

t=input()
if palindrome(t):
    print("Palindrome.")
else:
    print("Not a palindrome.")
