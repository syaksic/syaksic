# Numeros Primos

## Conjeturas 

### Conjetura fuerte de Goldbach

Todo Numero Par mayor a 2 puede ser expresado como la suma de 2 Numeros Primos.

<!---(2N_i=P_a + P_b)-->
![Regla1](./img/Screenshot from 2015-10-03 13:03:45.png)

### Conjetura debil de Goldbach

Todo Numero Impar mayor a 5 puede ser expresado como la suma de 3 Numeros Primos.

<!---(2N_i+1=P_a + P_b + P_c)-->
![Regla2](./img/Screenshot from 2015-10-03 13:06:40.png)

### Conjetura simple de Yaksic

Todo Numero Primo mayor a 5 puede ser expresado como la multiplicacion de 2 Numeros Primos y la adicion de un Tercer Numero Primo.

<!---(P_i=P_a \cdot P_b + P_c)-->
![Regla3](./img/Screenshot from 2015-10-03 13:07:01.png)

	7:
	['2*2+3']
	11:
	['3*3+2', '2*3+5', '2*2+7']
	13:
	['2*5+3', '2*3+7']
	17:
	['3*5+2', '2*7+3', '3*2+5', '2*5+7', '2*3+11', '2*2+13']
	19:
	['2*7+5', '3*2+7', '2*3+13']
	23:
	['3*7+2', '5*2+3', '3*3+5', '3*2+11', '2*5+13', '2*3+17', '2*2+19']
	29:
	['2*13+3', '2*11+7', '3*3+11', '3*2+17', '2*5+19', '2*3+23']
	31:
	['7*2+3', '2*13+5', '5*2+11', '3*3+13', '2*7+17', '3*2+19']
	37:
	['5*7+2', '2*17+3', '3*5+7', '2*13+11', '5*2+17', '3*3+19', '2*7+23', '2*3+31']
	41:
	['3*13+2', '2*19+3', '2*17+7', '3*5+11', '7*2+13', '2*11+19', '3*3+23', '3*2+29', '2*5+31', '2*2+37']
	43:
	['2*19+5', '3*5+13', '2*13+17', '5*2+23', '2*7+29', '3*2+31', '2*3+37']
	47:
	['5*3+2', '11*2+3', '3*7+5', '2*17+13', '3*5+17', '7*2+19', '3*3+29', '2*5+37', '2*3+41', '2*2+43']
	53:
	['3*17+2', '5*5+3', '2*23+7', '3*7+11', '2*17+19', '3*5+23', '2*11+31', '3*2+41', '2*5+43', '2*3+47']
	59:
	['3*19+2', '13*2+7', '2*23+13', '3*7+17', '3*5+29', '7*2+31', '2*11+37', '3*3+41', '3*2+47', '2*3+53']
	61:
	['2*29+3', '5*5+11', '11*2+17', '3*7+19', '2*19+23', '3*5+31', '5*2+41', '3*3+43', '2*7+47']
	67:
	['5*13+2', '2*31+5', '5*2+7', '5*5+17', '11*2+23', '2*19+29', '3*5+37', '2*13+41', '5*2+47', '2*7+53', '2*3+61']
	


## Primos Optimos

Determine el conjunto de menor tamaño tal que usando las tres conjeturas anteriores se pueda generar todos los numeros naturales mayores a .

Ejemplo:

N=[1,2,3,4,5,6,7,8,9,10,11]
P=[2]

<!--
### Basics

- P_i: Numero Primo perteneciente al conjunto \math{P} 
- P_a: Numero Primo perteneciente al conjunto \math{P} 
- P_b: Numero Primo perteneciente al conjunto \math{P} 
- P_c: Numero Primo perteneciente al conjunto \math{P} 
- N_i: Numero Entero perteneciente al conjunto \math{N} 
-->



