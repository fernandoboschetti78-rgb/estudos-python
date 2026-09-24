coresPrimarias ={
    "vermelho": "cor primaria, encontrada na natureza em plantas e no sangue",
    "azul": "cor primaria que é a cor do céu e do mar",
    "amarelo": "cor primaria que é encontrada principalmente na areia"
}

coresSecundarias = {
    "laranja": "cor secundaria, resultado da mistura de vermelho e amarelo",
    "verde": "cor secundaria, resultado da mistura de azul e amarelo",
    "roxo": "cor secundaria, resultado da mistura de azul e vermelho"
}

coresTerciarias = {
    "vermelho-alaranjado": "cor terciaria, resultado da mistura de vermelho e laranja",
    "amarelo-alaranjado": "cor terciaria, resultado da mistura de amarelo e laranja",
    "amarelo-esverdeado": "cor terciaria, resultado da mistura de amarelo e verde",
    "azul-esverdeado": "cor terciaria, resultado da mistura de azul e verde",
    "azul-arroxeado": "cor terciaria, resultado da mistura de azul e roxo",
    "vermelho-arroxeado": "cor terciaria, resultado da mistura de vermelho e roxo",
    "marrom": "cor terciaria, resultado da mistura de vermelho, amarelo e azul",
    "lilas": "cor terciaria, resultado da mistura de azul e vermelho com branco"
}

otrasCores = {
    "branco": "cor neutra, resultado da mistura de todas as cores",
    "preto": "cor neutra, ausência de luz",
    "cinza": "cor neutra, resultado da mistura de preto e branco",
    "rosa": "cor neutra, resultado da mistura de vermelho e branco"
}

cor =input("Digite o nome de uma cor: ").lower().strip()
while cor not in coresPrimarias and cor not in coresSecundarias and cor not in coresTerciarias and cor not in otrasCores:
        cor = input("cor invalida, digite novamente: ").lower().strip()

if cor in coresPrimarias:
    resultado = coresPrimarias[cor]
elif cor in coresSecundarias:
    resultado = coresSecundarias[cor]
elif cor in coresTerciarias:
    resultado = coresTerciarias[cor]
elif cor in otrasCores:
    resultado = otrasCores[cor]
    
print(f"a descrição da cor {cor} é: {resultado}")