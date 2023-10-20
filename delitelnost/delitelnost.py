#by Radovan Holčík (KermitThePog)
n = int(input("Zadej libovolné přirozené číslo: "))
for i in range(1, n+1): print((lambda j : str(i)+" " if(n%j==0) else "")(i), end="")
