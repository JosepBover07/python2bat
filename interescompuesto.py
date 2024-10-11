# P --> capital inicial --> el dinero que les damos al banco
# t --> nuemro de años
# r --> interés anual en porcentajes
# n --> numero de periodos por año
# A --> capital final
def calcularinteres(P,r,t,n):
    A=P*(1+r/n)**(n*t)
    return A
P=float(input("capital inicial"))
r=float(input("interes anual en porcentaje"))
t=float(input("numero de años"))
n=float(input("numero de periodos por año"))

capitalfinal=calcularinteres(P,r,1,n)
print(f"la cantidad final despues de {1} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,2,n)
print(f"la cantidad final despues de {2} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,3,n)
print(f"la cantidad final despues de {3} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,4,n)
print(f"la cantidad final despues de {4} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,5,n)
print(f"la cantidad final despues de {5} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,6,n)
print(f"la cantidad final despues de {6} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,7,n)
print(f"la cantidad final despues de {7} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,8,n)
print(f"la cantidad final despues de {8} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,9,n)
print(f"la cantidad final despues de {9} años sera {capitalfinal}")
capitalfinal=calcularinteres(P,r,10,n)
print(f"la cantidad final despues de {10} años sera {capitalfinal}")