def isStep(numero):
    if len(numero)/float(2)!=len(numero)/2:
        return False

    for i in range(0,len(numero),2):
        if not (int(numero[i:i+2][0])+1==int(numero[i:i+2][1]) or int(numero[i:i+2][0])-1==int(numero[i:i+2][1])):
            return False
 
    return True

numero = input("Escriba un numero:")
isStep(numero)

if isStep(numero):
    print ("Es un número STEP")
else:
    print ("No es un número STEP")