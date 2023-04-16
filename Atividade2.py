altura = input("Digite sua altura: ")

peso = input ("Digite seu peso: ")

altura = float(altura)

peso = float(peso)

imc = peso/(altura**2)

imc = round(imc,2)

print("O IMC é: ", imc)

if imc < 18.5:
 print("Magreza")

elif imc>= 18.5 and imc <= 24.99:

  print("Normal")
elif imc>= 25 and imc <= 29.99:

 print("Sobrepeso")

elif imc>= 30 and imc <= 39.99:

 print("Obesidade")

else: 

 print("Obesidade grave")