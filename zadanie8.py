lista=[]
x = 0
while x <=9:
     a = int(input("Podaj liczbe %d: " % (x+1)))
     x+=1
     if a % 2 == 0 :
         lista.append(a)
print(lista)