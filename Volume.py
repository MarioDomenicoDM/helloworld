import math
s=input("-1 Cubo, -2 Sfera      ")

if s==1:
	print "Hai scelto di calcolare il volume del cubo "
	l=input("inserisci il lato ")
	print "il volume e' ",l*l*l 
else:
	print "Hai scelto di calcolare il volume della sfera "
	r=input("inserisci il valore del raggio ")
	print "il volume e' " ,(4*math.pi*(r*r*r))/3
