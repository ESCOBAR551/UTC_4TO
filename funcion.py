def sumar(n1,n2):
    return n1+n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Error: Division por cero"
    
def restar(n1,n2):
    return n1-n2

n1 = int(input("ingresa el numero 1:"))
n2 = int(input("ingresa el numero 2:"))

print("La suma es:", sumar(n1,n2))
print("La multiplicacion es:", multiplicar(n1,n2))
print("La division es:", dividir(n1,n2))
print("la resta es:", restar(n1,n2))
