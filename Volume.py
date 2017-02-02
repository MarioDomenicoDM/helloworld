import math
print "Calcolo del volume di un cubo o di una sfera "
print "Effettua una scelta (1 - Cubo, 2- Sfera) "
s = input("? ")

if s==1:
	l=input("Lato del cubo: ")
	print "Il cubo di lato ", l," ha volume ", l*l*l
else:
	r=input("Raggio della sfera: ")
	print "Il cubo di raggio ", r," ha volume ", (4.*math.pi*(r*r*r))/3.
