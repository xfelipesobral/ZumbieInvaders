#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dados import *
import math
import random


'''
====================
	  FUNCOES
====================
'''

'''
mover_vaca: Vaca -> Vaca
Produz a próxima vaca (ou seja, fazer ela andar)
'''
def mover_vaca(vaca):
    if vaca.x < 0 or vaca.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo x
        vaca.x = vaca.x + vaca.dx

        if vaca.x > PAREDE_DIREITA:
            vaca.x = PAREDE_DIREITA
        elif vaca.x < PAREDE_ESQUERDA:
            vaca.x = PAREDE_ESQUERDA

        return vaca

'''
mover_zumbi: Zumbi -> Zumbi
Mover o Zumbi no eixo x usando o dx
'''
def mover_zumbi(zumbi):
    if zumbi.x < 0 or zumbi.x > LARGURA:
        return "Erro: zumbi invalida"
    else:
        #calcula novo dx
        if (zumbi.x == PAREDE_DIREITA and zumbi.dx > 0) \
                or (zumbi.x == PAREDE_ESQUERDA and zumbi.dx < 0):  
            zumbi.dx = - zumbi.dx ## DEIXA O DX NEGATIVO PARA ELE VOLTAR
            zumbi.y = zumbi.y+DESLOCAMENTO_ZUMBI ## CONDIÇÃO PARA O ZUMBI DESCER DE LINHA

        #calcula novo x
        zumbi.x = zumbi.x + zumbi.dx

        if zumbi.x > PAREDE_DIREITA:
            zumbi.x = PAREDE_DIREITA
        elif zumbi.x < PAREDE_ESQUERDA:
            zumbi.x = PAREDE_ESQUERDA

        return zumbi

'''
mover_leite: Leite -> Leite
Mover o Leite da vaca no eixo y usando o dy
'''
def mover_leite(leite):
    if leite.y < 0 or leite.y > ALTURA:
        return "Erro: leite invalida"
    else:
        #calcula novo dy
        if (leite.y == PAREDE_BAIXO and leite.dy > 0):
            leite.dy = - leite.dy

        #calcula novo y
        leite.y = leite.y + leite.dy

        if leite.y > PAREDE_BAIXO:
            leite.y = PAREDE_BAIXO
        elif leite.y < PAREDE_CIMA:
            leite.y = PAREDE_CIMA

        return leite

'''
mover_bala: Bala -> Bala
Mover a bala do zumbi no eixo y usando o dy
'''
def mover_bala(bala):
    if bala.y < 0 or bala.y > ALTURA:
        return "Erro: bala invalida"
    else:
        #calcula novo y
        bala.y = bala.y + bala.dy

        if bala.y > PAREDE_BAIXO:
            bala.y = PAREDE_BAIXO
        elif bala.y < PAREDE_CIMA:
            bala.y = PAREDE_CIMA

        return bala

'''
municao_respawn: Municao -> Municao
Caso municao for coletada, ela da respwan em algum lugar do eixo X gerado aleatoriamente
'''
def municao_respawn(municao):
    if municao.x < 0:
        return "Erro: Municao fora do mapa"
    else:
        municao.x = random.randint(PAREDE_ESQUERDA, PAREDE_DIREITA)

        return municao

'''
recarrega_municao: Leites -> Leites
Recebe leites da vaca e recarrega ele, acrescentando leites na lista até chegar a 5
'''
def recarrega_municao(leites):

    if len(leites) == 0:
        leites.extend([Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0), Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0), Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0), Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0), Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)])
    elif len(leites) >= 10:
        return leites
    else:
        leites.append(Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0))

    return leites 


'''
distancia: Int Int Int Int -> Float
Calcula a distancia entre dois pontos
'''
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

'''
colidir_municao: Vaca, Municao -> Verifica e chama funcao de RESPAWN ->  Tru or False
'''
def colidir_municao(vaca, municao):
    raio_vaca = IMG_VACA.get_width()/2
    raio_municao = IMG_MUNICAO.get_width()/2

    d = distancia(vaca.x, Y_VACA, municao.x, Y_VACA) ## SE A VACA COLIDIR COM A MUNICAO = MUNICAO RESPAWN

    if d <= raio_vaca + raio_municao:
        municao = municao_respawn(municao)
        return True

    return False

'''
colidirem: Vaca, Leite, Bala, Zumbi -> 1 (perdeu) or 2 (ganhou)
1- Verifica se a vaca e o zumbi colidiram
2- Verifica se a bala colidiu com a vaca
3- Verifica se o zumbi colidiu com o Y da vaca
4- Verifica se o leite da vaca colidiu com o zumbi
'''
def colidirem(vaca, leite, bala, zumbi, feno):
    raio1 = IMG_VACA.get_width()/2
    raio2 = IMG_ZUMBI.get_width()/2
    raio3 = IMG_BALA_V.get_width()/2
    raio4 = IMG_BALA_Z.get_width()/2
    raio5 = IMG_FENO.get_width()/2


    ## COLISÕES QUE FAZEM PERDER
    d = distancia(vaca.x, Y_VACA, zumbi.x, zumbi.y) ## VACA /=/ ZUMBI == PERDEU
    if d <= raio1 + raio2:
        return 1

    d = distancia(bala.x, bala.y, vaca.x, Y_VACA) ## BALA /=/ VACA == PERDEU
    if d <= raio1 + raio4:
        return 1

    if zumbi.y >= PAREDE_BAIXO-raio2: ## ZUMBI X == PAREDE BAIXO |== PERDEU
        return 1

    ##COLISÕES QUE FAZEM GANHAR
    if leite != None: 
        d = distancia(leite.x, leite.y, zumbi.x, zumbi.y) ## LEITE /=/ ZUMBI = GANHOU
        if d <= raio3 + raio2:
            return 2

    ##COLISAO COM O FENO
    if feno != None:
        d = distancia(bala.x, bala.y, feno.x, feno.y)
        if d <= raio4+raio5:
            bala.y = PAREDE_BAIXO
            return 0

        d = distancia(leite.x, leite.y, feno.x, feno.y)
        if d <= raio3+raio5:
            leite.y = PAREDE_CIMA
            return 3

        d = distancia(zumbi.x, zumbi.y, feno.x, feno.y)
        if d <= raio2+raio5:
            return 3

    return 0

'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
'''
def mover_jogo(jogo):
    zumbis_vivos = len(jogo.zumbis) ## CONTA QUANTOS ZUMBIS ESTÃO 'VIVOS', QUANTOS ZUMBIS QUE ESTÃO NA LISTA

    for zumbi in jogo.zumbis:
        if colidirem(jogo.vaca, None, jogo.bala, zumbi, None) == 1: ## SE BALA DO ZUMBI OU ZUMBI CHEGAR A VACA_Y == PERDEU
            jogo.game_over = True
            return jogo

        for leite in jogo.leites:
            if colidirem(jogo.vaca, leite, jogo.bala, zumbi, None) == 2:
                jogo.leites.remove(leite)

                if zumbis_vivos == 1: ## SE TIVER SÓ UM ZUMBI VIVO, QUANDO ELE MORRER...
                    jogo.zumbis.remove(zumbi)
                    jogo.game_ganho = True
                    return jogo

                jogo.zumbis.remove(zumbi)

            for feno in jogo.fenos:
                if colidirem(jogo.vaca, leite, jogo.bala, zumbi, feno) == 3:
                    jogo.fenos.remove(feno)
                    return jogo




    #else
    mover_vaca(jogo.vaca)

    if colidir_municao(jogo.vaca, jogo.municao) == True:
        recarrega_municao(jogo.leites)

    # CASO O LEITE ESTEJA NO Y INICIAL
    for leite in jogo.leites:
        if leite.y >= PAREDE_BAIXO-(IMG_VACA.get_height()):
            leite.x = jogo.vaca.x #SE SIM, ELE RECEBE X DA VACA

        mover_leite(leite)

        if leite.y == PAREDE_CIMA:
            jogo.leites.remove(leite)

    
    # SE O Y FOR > QUE A PAREDE BAIXO | ESSA CONDIÇÃO FAZ COM QUE A BALA SAIA SEMPRE DO ZUMBI
    if jogo.bala.y>=PAREDE_BAIXO:
        
        if zumbis_vivos >= 1:
            novaBala = random.randint(0,(zumbis_vivos-1))
        else:
            novaBala = 0

        jogo.bala.x = jogo.zumbis[novaBala].x # X DA BALA RECEBE X DO ZUMBI
        jogo.bala.y = jogo.zumbis[novaBala].y # Y DA BALA RECEBE Y DO ZUMBI

    for zumbi in jogo.zumbis:

        # SE O Y DA BALA == PAREDE_CIMA, OU SEJA COMEÇAR PARA FORA DO JOGO; A BALA RECEBE X DO ZUMBI
        if jogo.bala.y == PAREDE_CIMA: 
            novaBala = random.randint(0,(zumbis_vivos-1))  
            jogo.bala.x = jogo.zumbis[novaBala].x

        mover_zumbi(zumbi)  # funcao auxiliar (helper)

    mover_bala(jogo.bala)

    return jogo




'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na tela
'''
def desenha_vaca(vaca):
    TELA.blit(IMG_VACA,
        (vaca.x - IMG_VACA.get_width() / 2,
        Y_VACA - IMG_VACA.get_height() / 2))



'''
desenha_zumbi: Zumbi -> Imagem
Desenha o zumbi
'''
def desenha_zumbi(zumbi):
    if zumbi.dx < 0:
        TELA.blit(IMG_ZUMBI_V,
                  (zumbi.x - IMG_ZUMBI_V.get_width()/2,
                   zumbi.y - IMG_ZUMBI_V.get_height()/2))
    else:
        TELA.blit(IMG_ZUMBI,
                  (zumbi.x- IMG_ZUMBI.get_width()/2,
                   zumbi.y - IMG_ZUMBI.get_height()/2))

'''
desenha_fundo: Background -> Image
mDesenha o background
'''
def desenha_fundo():
    TELA.blit(IMG_BACKGROUND,
              (0,
              0))

'''
desenha_leite: Leite -> Imagem
Desenha o tiro da vaca
'''
def desenha_leite(leite):
    TELA.blit(IMG_BALA_V,(leite.x - IMG_BALA_V.get_width()/2, leite.y - IMG_BALA_V.get_height()/2))

'''
desenha_bala: Bala -> Imagem
desenha o tiro do Zumbi
'''
def desenha_bala(bala):
    TELA.blit(IMG_BALA_Z,(bala.x - IMG_BALA_Z.get_width()/2, bala.y - IMG_BALA_Z.get_width()/2))

'''
desenha_municao: Municao -> Imagem
desenha a municao da vaca
'''
def desenha_municao(municao):
    TELA.blit(IMG_MUNICAO,(municao.x - IMG_MUNICAO.get_width()/2, Y_VACA - IMG_MUNICAO.get_width()/2))

######################################################################################################
    # EDITANDO AQUI
def desenha_feno(feno):

    TELA.blit(IMG_FENO,(feno.x - IMG_FENO.get_width()/2, feno.y - IMG_FENO.get_width()/2))

#####################################################################################################


'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    if jogo.game_over:
        desenha_fundo()
        desenha_vaca(jogo.vaca)
        TELA.blit(IMG_LOSE,(PAREDE_DIREITA/2 - IMG_LOSE.get_width()/2, PAREDE_BAIXO/2- IMG_LOSE.get_width()/2))

    elif jogo.game_ganho:
        desenha_fundo()
        desenha_vaca(jogo.vaca)
        TELA.blit(IMG_WIN,(PAREDE_DIREITA/2 - IMG_WIN.get_width()/2, PAREDE_BAIXO/2- IMG_WIN.get_width()/2))

    else:
        desenha_fundo()
        desenha_bala(jogo.bala)
        desenha_municao(jogo.municao)
        
        for leite in jogo.leites:
            desenha_leite(leite)

        desenha_vaca(jogo.vaca)
        
        for zumbi in jogo.zumbis:
            desenha_zumbi(zumbi)

        for feno in jogo.fenos:
            if feno != False:
                desenha_feno(feno)

        municao = str(len(jogo.leites))
        fonte = pg.font.SysFont("monospace", 40)

        if len(jogo.leites)<=3:
            texto = fonte.render(municao, 1, (255, 0, 0))
        if len(jogo.leites)>3 and len(jogo.leites)<=7:
            texto = fonte.render(municao, 1, (255, 255, 255))
        if len(jogo.leites)>7:
            texto = fonte.render(municao, 1, (0, 255, 0))

        TELA.blit(texto, (PAREDE_DIREITA-20, PAREDE_BAIXO-40))





'''
trata_tecla_vaca: Vaca, EventoTecla -> Vaca
Quando teclar as setas direcionais a vaca se movimenta
'''
def trata_tecla_vaca(vaca, tecla):
    if (tecla == pg.K_LEFT) or (tecla == pg.K_LEFT and pg.K_SPACE):
        vaca.dx = -DX

    elif (tecla == pg.K_RIGHT) or (tecla == pg.K_RIGHT and pg.K_SPACE):
        vaca.dx = DX

    return vaca


'''
trata_tecla_leite: Leite, EventoTecla -> "tiro" leite
Quando teclar espaço, a vaca atira o leite
'''
def trata_tecla_leite(leite, tecla):
    if tecla == pg.K_SPACE:
       
        leite.dy = DV
 
    return leite

'''                                             
trata_solta_tecla: Vaca, EventoTecla -> Vaca    
Trata solta tecla vaca   

se a tecla for ESPAÇO, ele apenas retorna a vaca, caso for outra ele para              
'''
def trata_solta_tecla_vaca(vaca, tecla):
    if(tecla==pg.K_SPACE):
        return vaca
    elif(tecla==pg.K_RIGHT or tecla==pg.K_LEFT):
        vaca.dx = 0
        return vaca

    return vaca

'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata solta tecla geral
'''
def trata_solta_tecla(jogo, tecla):
    jogo.vaca = trata_solta_tecla_vaca(jogo.vaca, tecla)
    return jogo

'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata tecla geral
'''
def trata_tecla(jogo, tecla):

    ## PRECISA ARRUMAR ESSA PARTE
    if (jogo.game_over == True)  and tecla == pg.K_F1:
        return JOGO_INICIAL

    if (jogo.game_ganho == True) and tecla == pg.K_F1:
        return JOGO_INICIAL
    ## -----------
    else:
        jogo.vaca = trata_tecla_vaca(jogo.vaca, tecla)

        municao_vaca = len(jogo.leites) ## PEGA O TAMANHO DA LISTA

        
        if municao_vaca != 0: ## SE TIVER ALGO NA LISTA

            for leite in jogo.leites: ## ATIRE LEITE
                
                if leite.dy == 0:
                    leite = trata_tecla_leite(leite, tecla)
                    break
            

        return jogo