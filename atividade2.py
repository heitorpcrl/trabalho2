#Nomes: Heitor Santos Cortes, Marcelo, Guilherme Vieira, Jair
from os import system
import random


vida = 5
vida_pos_batalha = vida
nivel = 1
ataque = 3
defesa = 1
exp = 0
exp_necessaria = exp
moeda_bronze_player = 0
moeda_prata_player = 0
moeda_bronze = 0
moeda_prata = 0
vida_monstro = 0
ataque_monstro = 0
defesa_monstro = 0

personagem = {
  
"vida" : vida,
"nivel" : nivel,
"ataque": ataque,
"defesa" : defesa,
"exp": exp,
"exp necessaria": exp_necessaria,
"moeda de prata": moeda_prata,
"moeda de bronze": moeda_bronze,
"vida do monstro": vida_monstro,
"ataque do monstro": ataque_monstro,
"defesa do monstro": defesa_monstro,
}




nome = input("Digite o nome do jogador: ")

print("\nSeu nome:", nome, "\n vida:", vida, "ataque:", ataque, "defesa:", defesa,)

pergunta = str(input(f"Deseja entrar na caverna {nome} ? (sim ou nao): "))

if pergunta == "nao":
 exit()

if pergunta == "sim":
           chance = random.randint(0, 100)

           if chance <= 39:
            print("um monstro fraco apareceu !")

            monstro_fraco = {
                 vida_monstro = 5,
                 ataque_monstro = 2,
                 defesa_monstro = 0,
                 xp = 1,
                 moeda_bronze = 1
            }
            

           elif chance == 40 and chance <=69:
            print("Um monstro médio apareceu!")
            vida_monstro = 10
            ataque_monstro = 4
            defesa_monstro = 1
            xp = 3
            moeda_bronze = 3

           elif chance == 70 and chance <= 89:
            print("Um monstro difícil apareceu!")
            vida_monstro = 15
            ataque_monstro = 6
            defesa_monstro = 2
            xp = 10
            moeda_bronze = 10

           elif chance == 90 and chance <= 99:
            print("O Boss apareceu! (se fudeu kkkk)")
            vida_monstro = 50
            ataque_monstro = 10
            defesa_monstro = 5
            xp = 100
            moeda_prata = 1

while vida > 0:
        pergunta = str(input(f"Deseja entrar na caverna {nome} ? (sim ou nao): "))

        if pergunta == "nao":
            break

        if pergunta == "sim":
           chance = random.randint(0, 100)

           if chance <= 39:
            print("um monstro fraco apareceu !")
            vida_monstro = 5
            ataque_monstro = 2
            defesa_monstro = 0
            xp = 1
            moeda_bronze = 1

           elif chance == 40 and chance <=69:
            print("Um monstro médio apareceu!")
            vida_monstro = 10
            ataque_monstro = 4
            defesa_monstro = 1
            xp = 3
            moeda_bronze = 3

           elif chance == 70 and chance <= 89:
            print("Um monstro difícil apareceu!")
            vida_monstro = 15
            ataque_monstro = 6
            defesa_monstro = 2
            xp = 10
            moeda_bronze = 10

           elif chance == 90 and chance <= 99:
            print("O Boss apareceu! (se fudeu kkkk)")
            vida_monstro = 50
            ataque_monstro = 10
            defesa_monstro = 5
            xp = 100
            moeda_prata = 1

        
        print ("||||||| a batalha começou !!! |||||||")

        while vida_monstro > 0 and vida > 0:      
            print("1: Atacar")
            print("2: Abandonar caverna")
            batalha = input("Escolha uma opção: ")

            if batalha == "2":
                 print("Voce fugiu da batalha")
                 break

            elif batalha == "1":
                 dano_jogador = max(ataque - defesa_monstro, 0)
                 vida_monstro -= dano_jogador
                 print(f"Você causou {dano_jogador} de dano. Vida do monstro: {max(vida_monstro, 0)}")

                 if vida_monstro <= 0:
                        
                        exp += xp
                        moeda_bronze_player += moeda_bronze
                        moeda_prata_player += moeda_prata
         
                        print("Você derrotou o monstro!")
         

                        exp_necessaria = (nivel + 1) * 1.1
                        while exp >= exp_necessaria:
                            ataque +=1 if nivel %2 == 1 else 0
                            defesa +=1 if nivel %2 == 1 else 0
                            nivel +=1
                            vida+=1
                            exp_necessaria = (nivel + 1) * 1.1

                 vida_pos_batalha = vida
                 break

        dano_monstro = max(ataque_monstro - defesa, 0)
        vida -= dano_monstro
        print(f"O monstro causou {dano_monstro} de dano. Sua vida: {max(vida, 0)}")

                


        if vida <= 0:
         
         print("Voce morreu...")
         print(personagem)
        
            












