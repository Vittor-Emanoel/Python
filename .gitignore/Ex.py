Ex01 Prova de Python

lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if li > (lado2 + lado3) or l2 > (lado1 + lado3) or l3 > (lado1 + lado2):
	print "Não pode ser um triangulo"
elif l1 == l2 == l3:
	print "Equilatero"
elif l1 == l2 or l1 == l3 or l2 == l3:
	print "Isósceles"
else:
	print "Escaleno"
