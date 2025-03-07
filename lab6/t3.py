def count_(a):
    u=0
    l=0
    for char in a:
        if char.isupper():
            u+=1
        elif char.islower():
            l+=1

    print("Uppercase:", u)
    print("Lowercase:", l)

text = input()
count_(text)
