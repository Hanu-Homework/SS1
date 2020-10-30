def gcd(num1, num2):
    return num1 if num2 == 0 else gcd(num2, num2 % num1)


p = 7
q = 11
e = 17

n = p * q

z = (p - 1) * (q - 1)

public_key = (n, e)
