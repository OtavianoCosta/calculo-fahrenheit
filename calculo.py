print("Ola, seja Bem vindo!!")

pergunta = input("Qual grau voce quer converter para fahrenheit?")

chute = float(pergunta)

calculo1 = chute - 32
calculo2 = 5 * calculo1
calculo3 = calculo2 / 9

print(chute, "Fahrenheit e o mesmo que", calculo3, "em C")

pergunta2 = input("Agora digite o Grau em Celsius que deseja converter para fahrenheit")

chute1 = float(pergunta2)

calculo1 = chute1 * 9/5
calculo2 = calculo1 + 32

print(chute1, " Celcius e o mesmo que", calculo2, "em Fahrenheit")

