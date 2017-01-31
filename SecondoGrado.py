import math

print "programma che risolve un'equazione di secondo grado nella forma 'ax^2+bx+c=0'"

a=input("Inserisci a")
b=input("inserisci b")
c=input("inserisci c")

if b!=0 and c!=0:
	print "equazione completa"
	d=(b*b)-(4*a*c)
	x=(-b+math.sqrt(d))/(2*a)
	y=(-b-math.sqrt(d))/(2*a)

	
	print "x1=" , x
	print "x2=",y

elif b==0 and c!=0:
	print "equazione pura"
	x=+math.sqrt(-(c/a))
	y=-math.sqrt(-(c/a))

	print "x1=",x
        print "x2=",y


elif b!=0 and c==0:
	print "equazione spuria"
	x=0
	y=-(b/a)

	print "x1=",x
        print "x2=",y
