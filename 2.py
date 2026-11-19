

def is_palindrome(a):
    chiffres = []

    while a >= 10:
        b = a % 10
        chiffres.append(b)
        a = a // 10

    chiffres.append(a)

    for i in range(len(chiffres) // 2):
        if chiffres[i] != chiffres[len(chiffres) - i - 1]:
            return False

    return True
a=9009
for i in range(100, 1000):
    for j in range(100, 1000):
        b = i * j
        if is_palindrome(b) and b > a:
            a = b

print(a)

    


    