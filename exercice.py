#!/usr/bin/env python


#def dissipated_power(voltage, resistance):
#	# TODO: Calculer la puissance dissipée par la résistance.
#	return 0

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y

	# Calculer le produit scalaire
	dot_product = v1[0] * v2[0] + v1[1] * v2[1]
	# Vérifier si =0
	# Retourner Vrai si =0, faux sinon
	return dot_product == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	sum = 0
	num_values = 0
	# Pour chaque élément
	for v in values:
		if v >= 0:
			sum += v
			num_values += 1
	return sum/num_values

def bills(value, bill_values):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	#bill_values = [20, 10, 5, 1]
	result = []

	for bill in bill_values:
		if value >= bill:
			result += [value // bill]
			value = value % bill
	return result

if __name__ == "__main__":
	#print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137, [20, 10, 5, 1]))
