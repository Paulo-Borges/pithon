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


        print("Qual a velocidade do seu carro?")
        velocidade = int(input("Digite a velocidade: "))
       
        if velocidade > 80:
            print("Você está acima da velocidade permitida! Multado.")
            multa = (velocidade - 80) * 7.00
            print("O valor da multa é R$" + str(multa))
        else:
            print("Você está dentro da velocidade permitida.")


            numero = int(input("Digite um número: "))
            if numero % 2 == 0:
                print("O número é par.")
            else:
                print("O número é ímpar.")