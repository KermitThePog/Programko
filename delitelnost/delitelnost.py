#by Radovan Holčík (KermitThePog)
n = int(input("Zadej libovolné přirozené číslo: "))
for i in range(1, n+1): print((lambda j : str(i)+" " if(n%j==0) else "")(i), end="")

#print( (lambda n: str(n)) (int(input("Zadej libovolné přirozené číslo: "))) )

#print([x for x in range(n = int(input("Zadej libovolné přirozené číslo: "))) if n%x==0])
