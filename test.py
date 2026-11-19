from math import * 
# terme U_n = 1/0! + 1/1! + 1/2! + .... + 1/n!
def u(n): 
    return sum (1/factorial(k) for k in range (n+1))
def v(n):
    return u(n) + 1/(n * factorial (n))
n = int (input("entrer un entier n >= 1:"))
print (f" {'k':>4} | {'u_n':>20} | {'v_n':>20} | {'v_n - u_n':>14}")
print ("-"*70)
for k in range (1, n+1):
    uk = u(k)
    vk = v(k)
    print (f"{k:>4} | {uk:>20.10f} | {vk:>20.10f} | {vk - uk:>14.10f}")
    