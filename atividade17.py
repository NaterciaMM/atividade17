# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.

ano = int(input("adcione um ano: "))

if ano% 100 !=0 ano%4 ==0 or ano% 400 ==0:
    print("ano bissexto")
else:
    print("ano não é bissexto")