import random
import math

vida_maxima_jogador = 5
vida_jogador = vida_maxima_jogador
nivel = 1
ataque_jogador = 3
defesa_jogador = 1
exp = 0
exp_necessaria = (nivel + 1) * 1.1
moeda_bronze_player = 0
moeda_prata_player = 0

nome = input("Digite o nome do jogador: ")

while vida_jogador > 0:
    print(f"\nNome: {nome}")
    print(f"Vida: {vida_jogador}/{vida_maxima_jogador}")
    print(f"Ataque: {ataque_jogador}")
    print(f"Defesa: {defesa_jogador}")
    print(f"Nível: {nivel}")
    print(f"Experiência: {exp}")
    print(f"Moedas de Bronze: {moeda_bronze_player}")
    print(f"Moedas de Prata: {moeda_prata_player}\n")

    pergunta = input(f"Deseja entrar na caverna {nome}? (sim ou nao): ").lower()

    if pergunta == "nao":
        print("Você decidiu não entrar na caverna. Resultados da aventura:")
        print(f"\nNome: {nome}")
        print(f"Vida: {vida_jogador}/{vida_maxima_jogador}")
        print(f"Ataque: {ataque_jogador}")
        print(f"Defesa: {defesa_jogador}")
        print(f"Nível: {nivel}")
        print(f"Experiência: {exp}/{exp_necessaria}")
        print(f"Moedas de Bronze: {moeda_bronze_player}")
        print(f"Moedas de Prata: {moeda_prata_player}\n")
        break

    if pergunta == "sim":
        chance = random.randint(0, 100)
        monstro = None

        if chance <= 39:
            print("Um monstro fraco apareceu!")
            monstro = {
                "vida_maxima": 5,
                "vida_atual": 5,
                "ataque": 2,
                "defesa": 0,
                "xp": 1,
                "moeda_bronze": 1,
                "moeda_prata": 0
            }

        elif 40 <= chance <= 69:
            print("Um monstro médio apareceu!")
            monstro = {
                "vida_maxima": 10,
                "vida_atual": 10,
                "ataque": 4,
                "defesa": 1,
                "xp": 3,
                "moeda_bronze": 3,
                "moeda_prata": 0
            }

        elif 70 <= chance <= 89:
            print("Um monstro difícil apareceu!")
            monstro = {
                "vida_maxima": 15,
                "vida_atual": 15,
                "ataque": 6,
                "defesa": 2,
                "xp": 10,
                "moeda_bronze": 10,
                "moeda_prata": 0
            }

        elif 90 <= chance <= 99:
            print("O Boss apareceu! (prepare-se!)")
            monstro = {
                "vida_maxima": 50,
                "vida_atual": 50,
                "ataque": 10,
                "defesa": 5,
                "xp": 100,
                "moeda_bronze": 0,
                "moeda_prata": 1
            }

        print("||||||| A batalha começou! |||||||")

        while vida_jogador > 0 and monstro["vida_atual"] > 0:
            print("1: Atacar")
            print("2: Abandonar caverna")
            acao = input("Escolha uma opção: ")

            if acao == "2":
                print("Você fugiu da batalha!")
                break

            elif acao == "1":
                dano_jogador = max(ataque_jogador - monstro["defesa"], 0)
                monstro["vida_atual"] -= dano_jogador
                print(f"Você causou {dano_jogador} de dano. Vida do monstro: {max(monstro['vida_atual'], 0)}")

                if monstro["vida_atual"] <= 0:
                    print("Você derrotou o monstro!")
                    exp += monstro["xp"]
                    moeda_bronze_player += monstro["moeda_bronze"]
                    moeda_prata_player += monstro["moeda_prata"]
                    print(f"Ganhou {monstro['xp']} de XP e {monstro['moeda_bronze']} moedas de bronze!")

                    while exp >= exp_necessaria:
                        nivel += 1
                        vida_maxima_jogador += 2
                        vida_jogador = vida_maxima_jogador

                        if nivel % 2 == 1:
                            ataque_jogador += 1
                            defesa_jogador += 1

                        exp_necessaria = (nivel + 1) * 1.1
                        print(f"Subiu para o nível {nivel}! Vida restaurada para {vida_jogador}!")

                    break

                dano_monstro = max(monstro["ataque"] - defesa_jogador, 0)
                vida_jogador -= dano_monstro
                print(f"O monstro causou {dano_monstro} de dano. Sua vida: {max(vida_jogador, 0)}")

                if vida_jogador <= 0:
                    print("Você morreu... Game Over!")
                    break

    if vida_jogador <= 0:
        print("Você foi derrotado! Resultados da aventura:")
        print(f"\nNome: {nome}")
        print(f"Vida: {vida_jogador}/{vida_maxima_jogador}")
        print(f"Ataque: {ataque_jogador}")
        print(f"Defesa: {defesa_jogador}")
        print(f"Nível: {nivel}")
        print(f"Experiência: {exp}/{exp_necessaria}")
        print(f"Moedas de Bronze: {moeda_bronze_player}")
        print(f"Moedas de Prata: {moeda_prata_player}\n")
        break
