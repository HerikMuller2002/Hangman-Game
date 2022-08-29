#Nome: Jogo da forca
#Desenvolvido por: Herik Muller dos Reis

#Bibliotecas
import random

#Introdução ao jogo
print('\033[1;7m-=\033[m'*20)
print('\033[1;7m{:^40}\033[m'.format('Jogo da Forca'))
print('\033[1;7m-=\033[m'*20)
#Regras:
print("\n\033[1m-O objetivo do jogo é acertar a 'palavra secreta' escolhida pelo computador antes de 'enforcar' o boneco \n-O jogador deve chutar apenas uma letra por vez; \n-O jogador pode errar até 5 vezes, se errar 6 o jogo acaba; \n-Se o jogador quiser sair basta escrever 'sair'.\033[m\n")

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

#Variáveis:
lista_palavras = []
palavra = ''
palavra_secreta = ''
letras_descobertas = []
banco_palavras = 0
letras_tentadas = []
alfabeto = ''
tentativa = 0
tema = 0
temas_possiveis = []
letras = ''
erros = 0

#Escolhendo o tema do jogo
print("\033[33;1mEscolha o tema que quer jogar: \nDigite 1 para o tema 'Times' \nDigite 2 para o tema 'Animais'\n")
#Variável de verificação de temas
temas = False

while not temas:
    #lista de números possíveis para se digitar
    temas_possiveis = ['1','2']

    tema = str(input('Digite o número do tema: \033[m'))
    if len(tema) > 1 or tema not in temas_possiveis:
        print('\n\033[31mDigite 1 ou 2!\033[m\n')
        continue
    else:
        #Verificando qual foi o tema escolhido
        if tema == "1":
            print('\nVocê escolheu o tema: TIMES')
            # criando uma lista com as palavras do banco de palavras (arquivo.txt)
            banco_palavras = open('Times.txt', 'r').read().split()
            for i in banco_palavras:
                lista_palavras.append(i)
            # Ecolhendo a palavra secreta aleatóriamento da lista de palavras
            palavra = random.choice(lista_palavras).upper()
            # criando uma lista com os caracteres da palavra
            palavra_secreta = list(palavra)

        elif tema == "2":
            print('\nVocê escolheu o tema: ANIMAIS')
            # criando uma lista com as palavras do banco de palavras (arquivo.txt)
            banco_palavras = open('Animais.txt', 'r').read().split()
            for i in banco_palavras:
                lista_palavras.append(i)
            # Ecolhendo a palavra secreta aleatóriamento da lista de palavras
            palavra = random.choice(lista_palavras).upper()
            # criando uma lista com os caracteres da palavra
            palavra_secreta = list(palavra)
        #Fim do loop
        temas = True

#Escondendo a palavra
for i in range(0, len(palavra_secreta)):
    #criando uma lista com o mesmo tamanho da palavra secreta, com "*" no lugar das "letras"
    letras_descobertas.append('*')


#criando uma lista com os possíveis chutes do jogador (apenas letras do alfabeto + "ç")
alfabeto = 'abcdefghijklmnopqrstuvwxyzç'.upper()
alfabeto = list(alfabeto)

#variável de verificação do loop
acertou = False
#loop do chute do jogador e a análise dele - (se a letra digitada está correta ou não)
while not acertou:
    #printando o board
    if erros == 0:
        print(board[0])
    elif erros == 1:
        print(board[1])
    elif erros == 2:
        print(board[2])
    elif erros == 3:
        print(board[3])
    elif erros == 4:
        print(board[4])
    elif erros == 5:
        print(board[5])

    #Mostrando a palavra na tela com as letras já descobertas
    print("\033[1;7mPalavra: ",letras_descobertas,'\033[m')
    print("Letras já digitadas: ",letras_tentadas)

    #lendo o chute do jogador
    chute = str(input('\033[34mDigite uma letra: \033[m')).upper()
    #Se o jogador escrever sair, o jogo encerra
    if chute == 'SAIR':
        print("\033[32m\nTenha um bom dia!\033[m")
        break
    #Verificando se o chute está dentro dos chutes possíveis (uma letra do alfabeto)
    elif len(chute) > 1 or chute not in alfabeto:
        print('\n\033[31mErro! \nSó pode digitar uma letra!\033[m\n')
        continue
    #Se o chute foi permitido e o jogador não quis sair então verificamos o chute
    else:
        if chute in letras_tentadas:
            print('\033[33mVocê já digitou essa letra!\033[m')
        else:
            letras_tentadas.append(chute)
            #Verificando se o chute do jogador está certo e então substituímos os "*" pela letra chutada
            for i in range(0, len(palavra_secreta)):
                if chute == palavra_secreta[i]:
                    letras_descobertas[i] = chute
            # erros
            if chute not in letras_descobertas:
                erros += 1

            #Verificando se o jogador ganhou
            if letras_descobertas == palavra_secreta:
                print('\n\033[32mVocê acertou! \nA palavra era %s!\033[m'%(palavra))
                acertou = True

            # Verificando se o jogador perdeu
            if erros == 6:
                print(board[6])
                print("\033[31m\nVocê Perdeu!")
                print("A palavra era %s\033[m"%(palavra))
                break