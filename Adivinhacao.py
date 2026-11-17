import random

print("=== Jogo de adivinhação ===")


while True:

    qtdChute = 0
    numero = random.randint(1, 10)


    while True:
        try:
            chute = float(input("Digite um numero de 1 a 10: "))

            if 1 <= chute <= 10:
                qtdChute += 1
            else:
                print("Erro | O número precisa ser entre 1 e 10.")
                continue


            if chute > numero:
                print("Opa, passou! Tente um número menor.")
            elif chute < numero:
                print("Um pouco mais! Tente um número maior.")
            else:
                print(f"Parabéns, você acertou em {qtdChute} tentativa(s)!")
                break

        except ValueError:
            print("Erro | Digite apenas números válidos.")
            

    print("Tentativas: " ,qtdChute)
    print("Numero Sorteado: ", numero)

    
    while True:
        continuar = input("Deseja continuar jogando?(SIM/NÃO)").upper().strip()

        if continuar in ["SIM", "NÃO", "NAO"]:
            break
        else:
            print("Entrada inválida. Digite apenas SIM ou NÃO.")
            
        
    if continuar in ["NÃO", "NAO"]:
        print("Saindo...")
        break
            

    