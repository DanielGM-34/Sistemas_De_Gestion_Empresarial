def saludar():
    print("Buenos dias")
saludar()

def esMayorQ0(num):
    if(num > 0):
        print(num,"Es mayor a 0")
    else:
        print(num,"No es mayor")

esMayorQ0(0)

def sumar(num,num2):
    return num+num2

resulSum = sumar(69,69)

print(resulSum)

def SumaYresta(n1,n2):
    return n1+n2,n1-n2

resultadoSum, resultadoRest = SumaYresta(8,90)

print("Resultado suma:", resulSum)
print("Resultado resta:", resultadoRest)

def Sumar2(*valores):
    resultado = 0
    for itema in valores:
        resultado+=itema
    return resultado

print(Sumar2(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,900,500,900,100000000000))
