print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print( f"Chat {mensa}")
    print(mensa)
def ellacontesta(mensa):
    print(f"chat ella:{mensa}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es :{n} {ap}")
def suma(a,b):
    s=a+b
    return s
def resta(a,b):
    s=a-b
    return s
def division(a,b):
    s=a/b
    return s
def multiplicacion(a,b):
    s=a*b
    return s
# llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Uribe", "Daniel")
print("Operacion suma")
c1=int( input("Ingresa un numero:  "))
c2=int(input("Ingresa un numero:  "))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion resta")
c3=int( input("Ingresa un numero:  "))
c4=int(input("Ingresa un numero:  "))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacion division")
c5=float( input("Ingresa un numero:  "))
c6=float(input("Ingresa un numero:  "))
damedivision=division(c5,c6)
print(f"La resta de {c5} / {c6} = {damedivision}")

print("Operacion multiplicacion")
c7=int( input("Ingresa un numero:  "))
c8=int(input("Ingresa un numero:  "))
damemultiplicacion=multiplicacion(c3,c4)
print(f"La resta de {c7} x {c8} = {damemultiplicacion}")


