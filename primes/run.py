import primes as prim

for i in range(len(prim.N)):
	new=prim.N[len(prim.N)-1]+1
	prim.N.append(new)
	if prim.isPrime(new):
		prim.P.append(new)

print (prim.N,prim.P)

save="data={'N':"+str(prim.N)+",'P':"+str(prim.P)+"}"
f = open('data.py', 'w')
f.write(save)
