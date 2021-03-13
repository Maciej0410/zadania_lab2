a=input(u"Podaj liczbę całkowitą a: ")
b=input(u"Podaj liczbę całkowitą b: ")
c=input(u"Podaj liczbę całkowitą c: ")

a=int(a)
b=int(b)
c=int(c)

if a > b & a > c:
    print(u"Liczba a: %d jest największa" % (a))
elif b > a & b > c:
    print(u"Liczba b: %d jest największa" % (b))
elif c > a & c > b:
    print(u"Liczba c: %d jest największa" % (c))
elif a==b > c:
    print(u"Liczby a i b są równe: %d, %d i są największe" % (a, b))
elif a==c > b:
    print(u"Liczby a i c są równe: %d, %d i są największe" % (a, c))
elif c==b > a:
    print("Liczby c i b są równe: %d, %d i są największe" % (c, b))
elif a == b < c:
    print(u"Liczba c: %d jest największa" % (c))
elif a == c < b:
    print(u"Liczba b: %d jest największa" % (b))
elif c == b < a:
    print(u"Liczba a: %d jest największa" % (a))
else:
    print("Wszystkie liczby są równe: %d=%d=%d => a=b=c" % (a,b,c))

