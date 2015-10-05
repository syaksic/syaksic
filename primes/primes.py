from data import data

N=data['N']
P=data['P']

def isPrime(val):
	if val in P:
		return True
	for p in P:
		if val % p==0:
			return False
	return True

def GoldbachPrimes(val):
	result=[]
	for Pb in P:
		aux=val-Pb
		if isPrime(aux):
			result.append(str(Pb)+'+'+str(aux))
				
	if result==[]:
		print str(val)+'''
		
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		
		'''+str(val)
	return result

def YaksicPrimes(val):
	result=[]
	for Pc in P:
		aux=val-Pc
		if aux < 2:
			break
		for Pb in P:
			if aux % Pb ==0:
				aux=aux/Pb
				if aux < 2:
					break
				if isPrime(aux):
					result.append(str(Pb)+'*'+str(aux)+'+'+str(Pc))
	if result==[]:
		print str(val)+'''
		
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		ERROR
		
		'''+str(val)
	return result


def generate(count):
	for i in range(count):
		new=N[len(N)-1]+1
		N.append(new)
		if isPrime(new):
			P.append(new)
	save="data={'N':"+str(N)+",'P':"+str(P)+"}"
	f = open('data.py', 'w')
	f.write(save)
	return P




