import random


while True:

    QtdChute = 0
    numero = random.randint(1, 10)


    print("Jogo de adivinhação")
    while True:
        try:
            chute = float(input("Digite um numero: "))

            if 1 <= chute <= 10:
                break
            else:
                print("Erro | O número precisa ser entre 1 e 10.")

        except ValueError:
            print("Erro | Digite apenas números válidos.")
            continue

    if chute > numero:
        print("Opa passou")
        QtdChute += 1
        continue
    elif chute < numero:                 
        print("Um pouco mais")
        QtdChute += 1
        continue 
    elif chute == numero:
        print("Parabéns você acertou!")
        QtdChute += 1


    while True:
        continuar = input("Deseja continuar?(SIM/NÃO)").upper().strip()

        if continuar in ["SIM", "NÃO", "NAO"]:
            break
        else:
            print("Entrada inválida. Digite apenas SIM ou NÃO.")
            
        
    if continuar in ["NÃO", "NAO"]:
        print("Saindo...")
        break
            

    print("Tentativas: " ,QtdChute)
    print("Numero Sorteado: ", numero)
