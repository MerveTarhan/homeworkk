küme = []
for i in range(1,126):
    if 125%i==200%i==350%i:
        küme.append(i)

        
print(max(küme))
