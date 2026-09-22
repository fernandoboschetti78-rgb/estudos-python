numero1=float(input("numero 1 "))
operador=input("operador: ")
numero2=float(input("numero 2 "))

if operador == "+":
    resultado=numero1+numero2
elif operador == "-":
    resultado=numero1-numero2
elif operador== "x":
    resultado=numero1*numero2
elif operador== "/":
    resultado=numero1/numero2 
else: resultado="operador invalido por favor use outro"



print("resultado igual:",resultado)