import domino 
import random
jogar = input('Você quer iniciar o jogo?(sim/não) ')
while jogar == 'sim':
    print('Olá, bem-vindo ao Jogo Dominó!')
    #Define-se o numero
    num_jog = int(input('Qual a quantidade de participantes?: '))
    print(num_jog)

    #Aqui, estamos pedindo pra que printe, de acordo com a nossa função  cria_pecas, pra que mostre a atd de peças disponiveis para a devida quantidade de jogadores
    #Aqui, cada jogador recebe 7 peças, aí as peças remanescentes vão para o monte
    lista_pecas = domino.cria_pecas()
    divisao_pecas = domino.inicia_jogo(num_jog, lista_pecas)
    print(divisao_pecas)


    sorteia_jogador = random.randint(0,num_jog-1)
        #Inicia o jogo:
        #Para iniciar o jogo, temos que mostrar as peças que estão 
        # dispostas para o jogador
    pecas = divisao_pecas['jogadores'][0] 

    print('O jogador {} inicia o jogo.'.format(sorteia_jogador))
    print('Suas peças são {}'.format(pecas))
    if sorteia_jogador == 0:
        print(pecas)
    
