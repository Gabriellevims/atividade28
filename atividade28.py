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
        n= len(idademaior)
      
        
    else:
        idademenor.append(idade2)
        m=len(idademenor)
        
print(m)
print(n)