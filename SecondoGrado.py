import math

print "programma che risolve un'equazione di secondo grado nella forma 'ax^2+bx+c=0'"

a = input("Inserisci a")
b = input("inserisci b")
c = input("inserisci c")

if b!=0 and c!=0:
	print "equazione completa"
	d = (b*b)-(4*a*c)
	x1 = (-b+math.sqrt(d))/(2*a)
	x2 = (-b-math.sqrt(d))/(2*a)

	
	print "x1=", x1
	print "x2=", x2

elif b==0 and c!=0:
	print "equazione pura"
	x1 = +math.sqrt(-(c/a))
	x2 = -math.sqrt(-(c/a))

	print "x1=", x1
        print "x2=", x2


elif b!=0 and c==0:
	print "equazione spuria"
	x1 = 0
	x2 = -(b/a)

	print "x1=", x1
        print "x2=", x2
