kandidat = ""
for t in input("Zadej větu: ").split():
    if len(t) > len(kandidat): kandidat = t
print(kandidat)