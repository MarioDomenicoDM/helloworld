print "Equazione di primo grado nella forma 'ax+b=0 "

a = input("Inserisci a ")
b = input("Inserisci b ")

print a, "x+", b, "=0"

if a==0 and b==0:

	print "L'equazione e' indeterminata "


elif a==0:
        print "L'euqazione e' impossibile "

else:
	print "x=", -b, "/", a
        print "x=", -b/a

