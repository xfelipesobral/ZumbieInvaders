#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *
import pygame as pg
import math as mt

''' ZUMBIES INVADERS 0.1 '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (800, 600)
TELA = pg.display.set_mode((LARGURA, ALTURA))

pg.display.set_caption('ZUMBIES INVADERS')

try:
    IMG_VACA_PARADA = pg.image.load('img/vaca.png') #ENDEREÇO VACA PARADA
    IMG_VACA_ANDANDO = pg.image.loag('img/vaca_andando.png') #ENDEREÇO VACA ANDANDO

    IMG_Z_INDO = pg.image.load('img/zumbi.gif') #ENDEREÇO IMAGEM ZUMBI
    IMG_Z_VOLTANDO = pg.transform.flip(IMG_Z_INDO, False, True) #RODAR IMAGEM

    IMG_TIRO_VACA = pg.image.load('img/vaca_andando.png') #ENDERÇO DA IMAGEM DO TIRO DA VACA
    IMG_TIRO_Z = pg.image.load('img/vaca_andando.png') #ENDEREÇO DA IMAGEM DO TIRO DO ZOMBIE

    IMG_BACKGROUND = pg.image.load('img/bg.jpg') #ENDEREÇO IMAGEM DE FUNDO

except:
    IMG_VACA_PARADA = pg.Surface((100,100),pg.SRCALPHA)    #IMAGEM VAZIA (CASO NÃO FUNCIONE AS DE CIMA)
    IMG_VACA_ANDANDO = pg.Surface((100,100),pg.SRCALPHA)
    IMG_Z_INDO = pg.Surface((100,100),pg.SRCALPHA)
    IMG_Z_VOLTANDO= pg.Surface((100,100),pg.SRCALPHA)
    IMG_TIRO_VACA = pg.Surface((100,100),pg.SRCALPHA)
    IMG_TIRO_Z = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BACKGROUND = pg.Surface((100,100),pg.SRCALPHA)

    print("ERRO: Imagens nao foram carregadas.")

BACKGROUND = pygame.image.load('bg.jpg')
TELA.blit(fundo(LARGURA, ALTURA))



Y_VACA = ALTURA // 2
X_ZU = LARGURA // 2

PAREDE_ESQUERDA = 0 + IMG_VACA_PARADA.get_width()//2
PAREDE_DIREITA = LARGURA - IMG_VACA_PARADA.get_width()//2

PAREDE_CIMA = IMG_TIRO_VACA.get_height()//2
PAREDE_BAIXO = ALTURA - IMG_TIRO_Z.get_height()//2


'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist
Vaca = namedlist("Vaca", "x, dx")  #estrutura da VACA

'''
Vaca pode ser criada como: Vaca(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
interp.: representa a posicao x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''
VACA_INICIAL = Vaca(PAREDE_ESQUERDA, 3)
VACA_FIM = Vaca(PAREDE_DIREITA, 3)
VACA_MEIO = Vaca((LARGURA//2), 3)

'''
Template para funções que recebem Vaca:
def fn_para_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        ... v.x
            v.dx

'''

Zumbie = namedlist("Zumbie", "x, y, dx, dy")  #estrutura do ZUMBIE

'''
Zumbie pode ser criada como: Zumbie(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
interp.: representa a posicao x do zumbie, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''
ZU_INICIAL = Zumbie(PAREDE_ESQUERDA, PAREDE_CIMA,3 , 3)
ZU_MEIO = Zumbie(LARGURA//2, PAREDE_CIMA//2, 3, 3)
ZU_FIM = Zumbie(PAREDE_DIREITA, PAREDE_CIMA, 3, 3)

'''
Template para funções que recebem Zumbie:
def fn_para_zu(zu):
    if zu.x < 0 or zu.x > LARGURA:
        return "Erro: zu invalido"
    else:
        ... zu.x
            zu.dx
'''

TiroV = namedlist("TiroV", "d, dy")  #estrutura do LEITE_VACA

'''
Tiro_Vaca pode ser criada como: TiroV(Int[PAREDE_CIMA, PAREDE_BAIXO], Int)
interp.: representa a posicao y do leite, e o deslocamento
a cada tick no eixo y, chamado de dy
Exemplos:
'''
TV_INICIAL = TiroV(PAREDE_BAIXO, 3)
TV_MEIO = TiroV(ALTURA//2, 3)
TV_FIM = TiroV(PAREDE_CIMA, 3)

'''
Template para funções que recebem Tiro_vaca:
def fn_para_tv(tv):
    if tv.y < 0 or tv.y > LARGURA:
        return "Erro: tv invalido"
    else:
        ... tv.y
            tv.dy
'''

TiroZ = namedlist("TiroZ", "d, dz")  #estrutura BALA_ZUMBIE

'''
Tiro_Zombie pode ser criada como: TiroZ(Int[PAREDE_CIMA, PAREDE_BAIXO], Int)
interp.: representa a posicao y da bala, e o deslocamento
a cada tick no eixo y, chamado de dy
Exemplos:
'''
TZ_INICIAL = TiroZ(PAREDE_BAIXO, 3)
TZ_MEIO = TiroZ(ALTURA//2, 3)
TZ_FIM = TiroZ(PAREDE_CIMA, 3)

'''
Template para funções que recebem Tiro_Zumbie:
def fn_para_tz(tz):
    if tz.y < 0 or tz.y > LARGURA:
        return "Erro: tz invalido"
    else:
        ... tz.y
            tz.dy
'''

Jogo = namedlist("Jogo", "vaca, zumbie, tiro_vaca, tiro_zombie,  game_over") #estrutura do JOGO

''' Jogo eh criado como: Jogo(Vaca, Zumbie, Tiro_Vaca, Tiro_Zumbie, Boolean)
interp. Um jogo é composto por uma vaca, alguns zumbies, trios
e uma flag (game_over) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''
JOGO_INICIAL = Jogo(VACA_INICIAL, ZU_INICIAL, TV_INICIAL, TZ_INICIAL, False)
##JOGO_GAME_OVER = Jogo(Vaca(X_ZU, 3), Zumbie(Y_VACA, 3), True)

'''Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.zumbie
        jogo.tiroV
        jogo.tiroZ
        jogo.game_over
'''




'''===================='''
''' Funções: '''

'''
mover_vaca: Vaca -> Vaca
Produz a próxima vaca (ou seja, fazer ela andar)
'''
def mover_vaca(vaca):
    if vaca.x < 0 or vaca.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dx
        if (vaca.x == PAREDE_DIREITA and vaca.dx > 0) \
                or (vaca.x == PAREDE_ESQUERDA and vaca.dx < 0):  #se vaca bateu na parede
            vaca.dx = - vaca.dx
        #usar depurador (debugger)

        #calcula novo x
        vaca.x = vaca.x + vaca.dx

        if vaca.x > PAREDE_DIREITA:
            vaca.x = PAREDE_DIREITA
        elif vaca.x < PAREDE_ESQUERDA:
            vaca.x = PAREDE_ESQUERDA

        return vaca



'''
mover_zumbie: Zumbie -> Zumbie
Mover o zumbie no eixo x usando o dx
'''
def mover_zu(zu):
    if zu.x < 0 or zu.x > LARGURA:
        return "Erro: zumbie invalido"
    else:
        #calcula novo dx
        if (zu.x == PAREDE_DIREITA and zu.dx > 0) \
                or (zu.x == PAREDE_ESQUERDA and zu.dx < 0):  #se o zumbie bateu na parede
            zu.dx = - zu.dx
        #usar depurador (debugger)

        #calcula novo y
        zu.x = zu.x + zu.dx

        if zu.x > PAREDE_DIREITA:
            zu.x = PAREDE_DIREITA
        elif zu.x < PAREDE_ESQUERDA:
            zu.x = PAREDE_ESQUERDA

        return zu

'''
mover_leite: Leite -> Leite
Mover o que a vaca atira no exito y usando dy
'''

def mover_leite(le):
    if le.y < 0 or le.y > LARGURA:
        return "Erro: leite invalido"
    else:
        if (le.y == PAREDE_CIMA and le.dy>0) or (le.y == PAREDE_BAIXO and le.dy < 0):
            le.dy = - le.dy

        le.y = le.y + le.dy

        if le.y > PAREDE_CIMA:
            le.y = PAREDE_CIMA
        elif le.y < PAREDE_BAIXO:
            le.y = PAREDE_BAIXO

        return le

def mover_bala(bl):
    if bl.y < 0 or bl.y > LARGURA:
        return "Erro: leite invalido"
    else:
        if (bl.y == PAREDE_CIMA and bl.dy>0) or (bl.y == PAREDE_BAIXO and bl.dy < 0):
            bl.dy = - bl.dy

        bl.y = bl.y + bl.dy

        if bl.y > PAREDE_CIMA:
            bl.y = PAREDE_CIMA
        elif bl.y < PAREDE_BAIXO:
            bl.y = PAREDE_BAIXO

        return bl

'''
colidirem: Vaca, Zumbi -> Boolean
Verifica se a vaca e o zumbi colidiram
'''
def distancia(x2, x1, y2, y1):
    conta = mt.sqrt(((x2*x2) - (x1*x1)) + ((y2*y2) - (y1 - y1)))
    if (conta==0):
        return True
    else:
        return False

def colidiremPersonagens(vaca, zumbi):
    raio1 = IMG_VACA_PAADA.get_width()
    raio2 = IMG_Z_INDO.get_width()

    bater = distancia(zumbie.x, vaca.x, zumbie.y, vaca.Y)
    #if (bater==True):
    #game over
    #else:
    #continua

def colidiremLeite(leite, zumbi):

    bater = distancia(TiroV.X, zumbie.x, TiroV.y, zumbie.y)
    #if (bater==True):
    #MATA ZUMBIE
    #else:
    #Continua

def colidiremBala(bala, vaca):
    bater = distancia(TiroZ.X, vaca.x, TiroZ.y, vaca.Y)
    #if (bater==True):
    #GAME OVER
    #else:
    #CONTINUA



'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
!!!
'''
def mover_jogo(jogo):
    if not colidirem(jogo.vaca, jogo.zumbie):
        jogo.vaca = mover_vaca(jogo.vaca)
        jogo.zumbie = mover_zu(jogo.zumbie)   # funcao auxiliar (helper)
    else:
        jogo.game_over = True
    return jogo


'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na tela
'''
def desenha_vaca(vaca):
    if vaca.dx < 0:
        TELA.blit(IMG_VACA_ANDANDO,
                  (vaca.x - IMG_VACA_ANDANDO.get_width() // 2,
                   Y_VACA - IMG_VACA_ANDANDO.get_height() // 2))
    else:
        TELA.blit(IMG_VACA_PARADA,
                  (vaca.x - IMG_VACA_PARADA.get_width() // 2,
                   Y_VACA - IMG_VACA_PARADA.get_height() // 2))


'''
desenha_chupacabra: Chupacabra -> Imagem
Desenha o chupacabra
'''
def desenha_zumbie(zumbie):
    TELA.blit(IMG_Z_INDO,
              (X_ZU - IMG_Z_VOLTANDO.get_width() // 2,
               zumbie.y - IMG_Z_VOLTANDO.get_height() // 2))


'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    desenha_vaca(jogo.vaca)
    desenha_zumbie(jogo.zumbie)
    gameDisplay.blit(IMG_BACKGROUND, (0, 0))


'''
trata_tecla_vaca: Vaca, EventoTecla -> Vaca
Quando teclar espaço, inverte a direção da vaca
'''
def trata_tecla_vaca(vaca, tecla):
    if tecla == pg.K_SPACE:
        vaca.dx = - vaca.dx
    return vaca


'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata tecla geral
'''
def trata_tecla(jogo, tecla):
    jogo.vaca = trata_tecla_vaca(jogo.vaca, tecla)
    return jogo



''' ================= '''
''' Main (Big Bang):
'''




''' Jogo -> Jogo '''
''' inicie o mundo com main(JOGO_INICIAL) '''

def main(inic):
    big_bang(inic, tela=TELA,
             quando_tick=mover_jogo,
             desenhar=desenha_jogo,
             quando_tecla=trata_tecla)

# main(JOGO_INICIAL)

