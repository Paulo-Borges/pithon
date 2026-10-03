nome = str(input("Digite seu nome: "));
if nome == "Alice":
    print("Olá, Alice!")
else:
    print("Olá, " + nome + "!")


    from random import randint
    computador = randint(0, 5)
    print("Vou Pensar em um número, tente adivinhar!")
    jogador = int(input("Em que número eu pensei? "))
    if jogador == computador:
        print("Parabéns! Você acertou.")
    else:
        print("Errou! Eu pensei no número " + str(computador) + ".")