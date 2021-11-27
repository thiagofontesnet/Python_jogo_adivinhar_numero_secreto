import random
import os

def play():
    print('O jogo foi iniciado')

    #   definindo numero secreto e tentativas do player
    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0


    #   definindo dificuldade
    print('Escolha a dificuldade do jogo')
    dificuldade = int(input('escolha (1)fácil, (2)normal, (3)difícil'))
    if dificuldade == 1:
        total_de_tentativas = 15
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5

    #  loop das rodadas
    for rodada in range(1, total_de_tentativas + 1):
        print('você esta na tentativa:{} de {}'.format(rodada, total_de_tentativas))   
        chute_input = input('chute um número para tentar acertar: ')
        chute = int(chute_input)

        if chute < 1 or chute > 100:
            print('você deve colocar apenas numeros entre 1 e 100.')
            total_de_tentativas = total_de_tentativas + 1
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('você acertou!!! O numero é:', numero_secreto)
            break
        else:
            if(maior):
                print('***********************************************')
                print('você errou, o numero secreto é menor')
            elif(menor):
                print('***********************************************')
                print('Você errou, o numero secreto é maior')
    print(f'o jogo foi concluído, obrigado por jogar. O número secreto era: {numero_secreto}. Aguarde um momento que iremos limpar sua tela.')

    os.system('sleep 10')
    os.system('clear')
