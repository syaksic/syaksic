import primes as prim

#print prim.generate(10)

limit=100
count=0
yaks=''
for p in prim.P:
	yaks=yaks+ '''
#######################################
	'''
	yaks=yaks+ str(p)
	yaks=yaks+ '''
#######################################
	'''
	yaks=yaks+ str(prim.YaksicPrimes(p))
	count+=1
	if count>limit:
		f = open('YaksicPrimes.txt', 'w')
		f.write(yaks)
		break

