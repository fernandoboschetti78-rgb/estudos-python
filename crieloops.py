import time 

loops=int(input("numero de loops: "))
intervalo=float(input("intervalo entre loops:"))
texto=input("texto dos loops: ")

for i in range(loops):
    print(texto)
    time.sleep(intervalo)