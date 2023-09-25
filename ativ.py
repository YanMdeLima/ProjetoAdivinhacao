from random import randint
from time import sleep

print("Carregando")
sleep(1)
print("Carregando.")
sleep(0.7)
print("Carregando..")
sleep(0.5)
print("Carregando...")
sleep(0.3)

# Função inicio com boas-vindas. Retorna o input player / número esoolhido.
def start():
    print("Você selecionou o modo Singleplayer")
    sleep(1)
    print("="*70)
    print("Olá! Boas-vindas, nesse jogo, você precisa escolher um numero entre")
    print("1 a 10, você começa com 50 pontos, caso chegue a zero, você perde.")
    print("Boa sorte!")
    print("="*70)  

def startMult():
    print("Você selecionou o modo Multiplayer")
    sleep(1)
    print("="*70)
    print("Olá! Boas-vindas, nesse jogo, você precisa escolher um numero entre")
    print("1 a 10, ganha quem acertar primeiro.")
    print("Boa sorte!")
    print("="*70)  

def inGame():
    bot_num = randint(1,10) 
    pontos_player = 50
    ganhou = False
    while pontos_player > 0 and not ganhou:
        player = int(input("Selecione um numero: "))
        if player == bot_num:
            ganhou = True 
        else:
            pontos_player -= 10 
            print(f"Foi mal, mas você errou... seus pontos agora são {pontos_player}")
    if ganhou and pontos_player == 50:
        print("Meus parabens! Você fez a pontuação perfeita!")

    elif ganhou:
        print("="*70)  
        print(f"Ganhou, sua pontuação total foi {pontos_player} pontos.")
        print("="*70)

    else:
        print("="*70)  
        restart = input("Perdeu, gostaria de tentar novamente? Sim ou não: ").upper()[0]
        print("="*70) 
        while not restart in "SN":
            print("Digite algo válido.")
            restart = input("Perdeu, gostaria de tentar novamente? Sim ou não: ").upper()[0]
        if restart == "S":
            inGame()
        else:
            print("Espero te ver outra hora!")
            
def criarJogador(num_player):
    nome = input(f"Digite seu nome jogador {num_player}: ")
    player = {"playerName": nome,"numRandom": randint(1,10), "Ganhou": False, "numPlayer": 0}
    return player


# Players sem ponto, quem acertar primeiro, ganha.
def inGameMult():
    playerOne = criarJogador(1)
    playerTwo = criarJogador(2)
    while not playerOne["Ganhou"] and not playerTwo["Ganhou"]:
        playerOne["numPlayer"] = int(input(f"Vez do {playerOne['playerName']}! Escolha um numero: "))

        if playerOne["numPlayer"] == playerOne["numRandom"]:
            playerOne["Ganhou"] = True 
        else: 
            print("Errou")
        playerTwo["numPlayer"] = int(input(f"Vez do {playerTwo['playerName']}! Escolha um numero: "))
        if playerTwo["numPlayer"] == playerTwo["numRandom"]:
            playerTwo["Ganhou"] = True
        else:
            print("Errou")

    if playerOne["Ganhou"]:
        if playerTwo["Ganhou"]:
            print("Empate")
        else:
            print(f"{playerOne['playerName']} ganhou!")
    else:
        print(f"{playerTwo['playerName']} ganhou!")




print("="*70)
print("--- Bem vindo ao jogo da adivinhaçao! Escolha seu modo de jogo: ---")
print("="*70)
modo = str(input("Você prefere jogar Singleplayer ou Multiplayer?: ")).upper()[0]
print("="*70)  

while not modo in "SM": 
    print("Coloque algo válido!")
    modo = str(input("Você prefere jogar Singleplayer ou Multiplayer?: ")).upper()[0]

if modo == "S":
    sleep(1)
    start()
    try:
        inGame()
    except: 
        print("\nOps, rolou um erro...Saindo do jogo...")
        exit(1)
else:
    sleep(1)
    startMult()
    try:
        inGameMult()
    except:
        print("\nOps, rolou um erro...Saindo do jogo...")
        exit(1)
