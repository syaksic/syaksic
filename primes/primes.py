from data import data

N=data['N']
P=data['P']

def isPrime(val):
	for p in P:
		if val % p==0:
			return False
	return True

