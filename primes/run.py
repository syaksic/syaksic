import primes as prim

#print prim.generate(10)

limit=100
count=0

for p in prim.P:
	print p
	prim.YaksicPrimes(p)
	count+=1
	if count>limit:
		break

