import time

while True:
    conta=input("Digite a conta que deseja calcular: ").strip()
    if "x" in conta:
        conta = conta.replace("x", "*")
    if "÷" in conta:
        conta = conta.replace("÷", "/")
    if "^" in conta:
        conta = conta.replace("^", "**")

    try:
        resultado = eval(conta)
        print(f"O resultado da conta {conta} é: {resultado}")
        break
    except Exception:
        print("Conta inválida, digite novamente.")
        time.sleep(0.5)
