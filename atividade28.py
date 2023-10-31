# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import time

idademaior = []
idademenor = []

for i in range(3):
    idade = int(input("Digite o ano que você nasceu:"))
    x=time.localtime()
    idade2=  (x[0]) -idade 
    if idade2 >= 18:
        idademaior.append(idade2)
        nmaior= len(idademaior)
    else:
        idademenor.append(idade2)
        nmenor = len(idademaior)
print(f"O número de pessoas que são maior de idade é {nmaior}.\n O número de pessoas que são menor de idade é {nmenor}")