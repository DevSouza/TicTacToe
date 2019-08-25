from time import sleep
from random import randint
import sys

pts_jogador1 = 0
pts_jogador2 = 0

while True:

    j = ''
    primeiro = ''
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    lv = 'livre'
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
    jogada = 0
    jog_adv = 0
    jogada_aleatoria = 0
    turnos = 1
    vencedor = ''

    tabuleiro_inicial = '''
--- COMO JOGAR ---
Quando for sua vez, digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.
Por exemplo, digamos que você queira jogar no centro, então você digita 5.
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    '''

    print(tabuleiro_inicial)

    print('Jogador 1 quer ser o X (xis) ou a O (bola)?', end=' ')

    while j != 'O' and j != 'X':
        j = str(input('Digite X ou O e pressione Enter para escolher: ')).strip().upper()
        if j != 'O' and j != 'X':
            print('\nEscolha inválida!\n')

    if j == 'O':
        adv = 'X'
        print('\nJogador 2 fica com o X.')
    elif j == 'X':
        adv = 'O'
        print('\nJogador 2 fica com a O.')

    print('\nQuem joga primeiro?', end=' ')

    while primeiro != 'J1' and primeiro != 'J2':
        instr = 'Digite J1 para jogador 1, ou digite J2 para o jogador 2: '
        primeiro = str(input(instr)).strip().upper()
        if primeiro != 'J2' and primeiro != 'J1':
            print('\nEscolha inválida!\n')

    if primeiro == 'J1':
        print('\nJogador 1 começa.\n')
    elif primeiro == 'J2':
        print('\nJogador 2 começa.\n')

    def atualizar_tabuleiro():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        tabuleiro = '''
     |     |   
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
        '''.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print(tabuleiro)

    def jogada_j1():
        global jogada

        while True:
            try:
                jogada = int(input('Jogador 1, digite a posição da sua jogada (1 a 9) e pressione Enter: '))
                break
            except ValueError:
                print('\nValor digitado inválido. Digite um número inteiro de 1 a 9!\n')

    def rotina_j1():
        global jogada
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        msg_ocupado = '\nEste espaço já está ocupado!\n'

        jogada_j1()

        while jogada not in range(1, (9 + 1)):
            jogada_j1()

            if jogada not in range(1, (9 + 1)):
                print('\nNúmero inválido!\n')

        while jogada == 1 and pos1 == 'ocupada' or \
            jogada == 2 and pos2 == 'ocupada' or \
            jogada == 3 and pos3 == 'ocupada' or \
            jogada == 4 and pos4 == 'ocupada' or \
            jogada == 5 and pos5 == 'ocupada' or \
            jogada == 6 and pos6 == 'ocupada' or \
            jogada == 7 and pos7 == 'ocupada' or \
            jogada == 8 and pos8 == 'ocupada' or \
                jogada == 9 and pos9 == 'ocupada':
            print(msg_ocupado)
            rotina_j1()

    def atualizar_jogadas_j1():
        global jogada
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if jogada == 1:
            p1 = j
            pos1 = 'ocupada'
        elif jogada == 2:
            p2 = j
            pos2 = 'ocupada'
        elif jogada == 3:
            p3 = j
            pos3 = 'ocupada'
        elif jogada == 4:
            p4 = j
            pos4 = 'ocupada'
        elif jogada == 5:
            p5 = j
            pos5 = 'ocupada'
        elif jogada == 6:
            p6 = j
            pos6 = 'ocupada'
        elif jogada == 7:
            p7 = j
            pos7 = 'ocupada'
        elif jogada == 8:
            p8 = j
            pos8 = 'ocupada'
        elif jogada == 9:
            p9 = j
            pos9 = 'ocupada'

# Jogador 2

    def jogada_j2():
        global jogada_aleatoria

        while True:
            try:
                jogada_aleatoria = int(input('Jogador 2, digite a posição da sua jogada (1 a 9) e pressione Enter: '))
                break
            except ValueError:
                print('\nValor digitado inválido. Digite um número inteiro de 1 a 9!\n')

    def rotina_j2():
        global jogada_aleatoria
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        msg_ocupado = '\nEste espaço já está ocupado!\n'

        jogada_j2()

        while jogada_aleatoria not in range(1, (9 + 1)):
            jogada_j2()

            if jogada_aleatoria not in range(1, (9 + 1)):
                print('\nNúmero inválido!\n')

        while jogada_aleatoria == 1 and pos1 == 'ocupada' or \
            jogada_aleatoria == 2 and pos2 == 'ocupada' or \
            jogada_aleatoria == 3 and pos3 == 'ocupada' or \
            jogada_aleatoria == 4 and pos4 == 'ocupada' or \
            jogada_aleatoria == 5 and pos5 == 'ocupada' or \
            jogada_aleatoria == 6 and pos6 == 'ocupada' or \
            jogada_aleatoria == 7 and pos7 == 'ocupada' or \
            jogada_aleatoria == 8 and pos8 == 'ocupada' or \
                jogada_aleatoria == 9 and pos9 == 'ocupada':
            print(msg_ocupado)
            rotina_j2()

    def atualizar_jogadas_j2():
        global jogada_aleatoria
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if jogada_aleatoria == 1:
            p1 = adv
            pos1 = 'ocupada'
        elif jogada_aleatoria == 2:
            p2 = adv
            pos2 = 'ocupada'
        elif jogada_aleatoria == 3:
            p3 = adv
            pos3 = 'ocupada'
        elif jogada_aleatoria == 4:
            p4 = adv
            pos4 = 'ocupada'
        elif jogada_aleatoria == 5:
            p5 = adv
            pos5 = 'ocupada'
        elif jogada_aleatoria == 6:
            p6 = adv
            pos6 = 'ocupada'
        elif jogada_aleatoria == 7:
            p7 = adv
            pos7 = 'ocupada'
        elif jogada_aleatoria == 8:
            p8 = adv
            pos8 = 'ocupada'
        elif jogada_aleatoria == 9:
            p9 = adv
            pos9 = 'ocupada'

    def checar_vencedor():
        global j, adv, turnos, vencedor, pts_jogador1, pts_jogador2
        global p1, p2, p3, p4, p5, p6, p7, p8, p9

        if p1 == j and p2 == j and p3 == j or \
           p1 == j and p4 == j and p7 == j or \
           p1 == j and p5 == j and p9 == j or \
           p2 == j and p5 == j and p8 == j or \
           p3 == j and p5 == j and p7 == j or \
           p3 == j and p6 == j and p9 == j or \
           p4 == j and p5 == j and p6 == j or \
           p7 == j and p8 == j and p9 == j:
            print('Jogador 1 GANHOU!\n')
            pts_jogador1 += 1
            vencedor = 'J1'
            turnos = 10

        if p1 == adv and p2 == adv and p3 == adv or \
           p1 == adv and p4 == adv and p7 == adv or \
           p1 == adv and p5 == adv and p9 == adv or \
           p2 == adv and p5 == adv and p8 == adv or \
           p3 == adv and p5 == adv and p7 == adv or \
           p3 == adv and p6 == adv and p9 == adv or \
           p4 == adv and p5 == adv and p6 == adv or \
           p7 == adv and p8 == adv and p9 == adv:
            print('Jogador 2 Ganhou!\n')
            pts_jogador2 += 1
            vencedor = 'J2'
            turnos = 10

    def atualizar_tudo():
        global jogada
        global turnos
        global vencedor

        if primeiro == 'J1':
            rotina_j1()
            atualizar_jogadas_j1()
            atualizar_tabuleiro()
            checar_vencedor()

            if turnos == 5:
                print('EMPATE!\n')
                turnos = 10
                vencedor = 'EMPATE'

            if vencedor == '':
                rotina_j2()
                atualizar_jogadas_j2()
                atualizar_tabuleiro()
                checar_vencedor()

        elif primeiro == 'J2':
            rotina_j2()
            atualizar_jogadas_j2()
            atualizar_tabuleiro()
            checar_vencedor()

            if turnos == 5:
                print('EMPATE!\n')
                turnos = 10
                vencedor = 'EMPATE'

            if vencedor == '':
                rotina_j1()
                atualizar_jogadas_j1()
                atualizar_tabuleiro()
                checar_vencedor()

        jogada = 0
        turnos += 1

    while turnos <= 5:
        atualizar_tudo()

    print('-------- PLACAR --------')
    print('Jogador 1: {} | Jogador 2: {}'.format(pts_jogador1, pts_jogador2))
    print('------------------------')

    while True:
        reiniciar = input('\nQuer jogar de novo? Digite S para sim ou N para não: ').lower()

        if reiniciar in ('s', 'n', '"s"', '"n"'):
            break
        print('\nResposta inválida!')

    if reiniciar == 's' or reiniciar == '"s"':
        print('\n-----------------------------------------------------')
        continue
    else:
        sys.exit(0)