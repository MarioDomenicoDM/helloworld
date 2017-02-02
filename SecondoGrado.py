import math

print "Programma che risolve un'equazione di secondo grado nella forma 'ax^2+bx+c=0'"

a = input("Inserisci a ")
b = input("inserisci b ")
c = input("inserisci c ")

if a==0 and b==0 and c==0:
    	print "L'equazione e' indeterminata"



elif a==0 and b==0:
    	print "L'equazione e' impossibile"



elif a==0:
    	x = -c/b
    	print "La x vale", x


else:	
	d = (b*b)-(4.*a*c)
	if d>=0:
		x1 = (-b+math.sqrt(d))/(2.*a)
		x2 = (-b-math.sqrt(d))/(2.*a)
		print "Delta = ", d 
		print "x1 = ", x1
		print "x2 = ", x2
	else:
		print "L'equazione non ammette soluzioni reali "
	
