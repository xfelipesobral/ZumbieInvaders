#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *
import math

''' ZUMBIE INVADERS 0.1 '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (800, 600)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_VACA = pg.image.load('img/vaca.png')
    IMG_ZUMBI = pg.image.load('img/zumbi.gif').convert()
    IMG_BALA_V = pg.image.load('img/vaca.png')
    IMG_BALA_Z = pg.image.load('img/vaca.png')
    IMG_BACKGROUND = pg.image.load('img/bg.jpg')

except:
    IMG_VACA = pg.Surface((100,100),pg.SRCALPHA)
    IMG_ZUMBI = pg.Surface((100,100),pg.SRCALPHA)

IMG_VACA = pg.transform.scale(IMG_VACA, (50, 50))
IMG_ZUMBI = pg.transform.scale(IMG_ZUMBI, (50, 50))

Y_VACA = 600 - IMG_VACA.get_width()/2
Y_ZUMBI = ALTURA/2

PAREDE_ESQUERDA = 0 + IMG_VACA.get_width()/2
PAREDE_DIREITA = LARGURA - IMG_VACA.get_width()/2

PAREDE_CIMA = 0
PAREDE_BAIXO = ALTURA

'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist
Vaca = namedlist("Vaca", "x, dx") #Estrutura da vaca

''' 
Vaca pode ser criada como: Vaca(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
interp.: representa a posicao x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''

VACA_INICIAL = Vaca(LARGURA/2, 3)
VACA_FINAL = Vaca(PAREDE_DIREITA, 3)
VACA_FINAL2 = Vaca(PAREDE_ESQUERDA, -3)

'''
Template para funções que recebem Vaca:
def fn_para_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        ... v.x
            v.dx

'''

Zumbi = namedlist("Zumbi", "x, y, dx, dy") #Estrutura do Zumbi

'''
Zumbi pode ser criado como: Zumbi(Int[PAREDE_ESQUERDA, PAREDE_DIREITA], Int[PAREDE_ESQUERDA, PAREDE_DIREITA], Int)
Interp.: X e Y representa a posicao do zumbi, dx e dy representam o deslocamento
a cada tick respectivamente no eixo x e y
Exemplos:
'''

ZUMBI_INICIAL = Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, 1, 1)
ZUMBI_FINAL = Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, 1, 1)
ZUMBI_VOLTANDO = Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, -1, -1)
ZUMBI_FINAL_VOLTANDO = Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, -1, -1)


'''
Template para funções que recebem Zumbi:
def fn_para_zumbi(z):
    if z.x < 0 or v.x > LARGURA:
        return "Erro: Zumbi invalido"
    else:
        ... v.x
        v.dx
'''


Leite = namedlist("Leite", "y, dy")

'''
Leite pode ser criado como: Leite(Int[POSICAO_VACA, PAREDE_CIMA], Int)
Interp.: Y representa a posicao do leite, e dy representa o deslocamento
a cada tick respectivamente no eixo y
Exemplos:
'''

LEITE_INICIAL = Leite(0, 0)
##LEITE_ATIRAR = Leite(vaca, 35)
LEITE_FINAL = Leite(PAREDE_CIMA, 35)

'''
Template para funções que recebem Leite:
def fn_para_leite(l):
    if l.y < 0 or l.y > ALTURA:
        return "Erro: Leite invalido"
    else:
        ... l.y
        l.dy
'''

Bala = namedlist("Bala", "y, dy")

'''
Bala pode ser criada como: Bala(Int[POSICAO_ZUMBI, PAREDE_BAIXO], Int)
Interp.: Y representa a posicao do leite, e dy representa o deslocamento
a cada tick respectivamente no eixo y
Exemplos:
'''

BALA_INICIAL = Bala(0, 0)
##BALA_ATIRAR = Bala(zumbi, 20)
BALA_FINAL = Bala(PAREDE_BAIXO, -20)

'''
Template para funções que recebem Bala:
def fn_para_bala(b):
    if b.y < 0 or b.y > ALTURA:
        return "Erro: Bala invalida"
    else:
        ... b.y
        b.dy
'''

Jogo = namedlist("Jogo", "vaca, zumbi, bala, leite, game_over")

''' 
Jogo eh criado como: Jogo(Vaca, List<Zumbi>, Bala, Leite, Boolean)
interp. Um jogo é composto por uma vaca, vários zumbis, tiro da vaca(leite), tiro do zumbi(bala),
e uma flag (game_over) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''

JOGO_INICIAL = Jogo(VACA_INICIAL, ZUMBI_INICIAL, BALA_INICIAL, LEITE_INICIAL, False)
JOGO_GAME_OVER = Jogo(VACA_INICIAL, ZUMBI_INICIAL, BALA_INICIAL, LEITE_INICIAL, True)

'''
Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.zumbi
        jogo.bala
        jogo.leite
        jogo.game_over
'''

#SEGUNDA PARTE
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
mover_zumbi: Zumbi -> Zumbi
Mover o Zumbi no eixo x usando o dx
'''
def mover_zumbi(zumbi):
    if zumbi.x < 0 or zumbi.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dx
        if (zumbi.x == PAREDE_DIREITA and zumbi.dx > 0) \
                or (zumbi.x == PAREDE_ESQUERDA and zumbi.dx < 0):  #se vaca bateu na parede
            zumbi.dx = - zumbi.dx
        #usar depurador (debugger)

        #calcula novo x
        zumbi.x = zumbi.x + zumbi.dx

        if zumbi.x > PAREDE_DIREITA:
            zumbi.x = PAREDE_DIREITA
        elif zumbi.x < PAREDE_ESQUERDA:
            zumbi.x = PAREDE_ESQUERDA

        return zumbi

### ADICIONAR FUNÇÃO DE COLISÃO ###
'''distancia: Int Int Int Int -> Float
Calcula a distancia entre dois pontos
'''
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)



'''
colidirem: Vaca, Chupacabra -> Boolean
Verifica se a vaca e o chupacabra colidiram
'''
def colidirem(vaca, zumbi):
    raio1 = IMG_VACA.get_width()/2
    raio2 = IMG_ZUMBI.get_width()/2
    d = distancia(vaca.x, Y_VACA, zumbi.x, zumbi.y)
    if d <= raio1 + raio2:
        return True
    #else
    return False

'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
!!!
'''
def mover_jogo(jogo):

    for zumbi in jogo.zumbi:
        if colidirem(jogo.vaca, jogo.zumbi):
            jogo.game_over = True
            return jogo

    #else
    mover_vaca(jogo.vaca)

    for zumbi in jogo.zumbi:
        mover_zumbi(jogo.zumbi)  # funcao auxiliar (helper)

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
    TELA.blit(IMG_ZUMBI,
              (zumbi.x - IMG_ZUMBI.get_width() / 2,
               zumbi.y - IMG_ZUMBI.get_height() / 2))

##screen.blit(background, backgroundRect)

'''
desenha_fundo: Background -> Imagem
Desenha o background
'''
def desenha_fundo():
    TELA.blit(IMG_BACKGROUND,
              (LARGURA,
              ALTURA))

'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    if jogo.game_over:
        fonte = pg.font.SysFont("monospace", 40)

        texto = fonte.render("VOCE PERDEU, OTARIO", 1, (255, 0, 0))

        TELA.blit(texto, (LARGURA / 2 - 20, ALTURA / 2 - 20))

    else:
        desenha_vaca(jogo.vaca)
        desenha_zumbi(jogo.zumbi)
        desenha_fundo()

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
    if jogo.game_over and tecla == pg.K_SPACE :
        return JOGO_INICIAL
    else:
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

main(JOGO_INICIAL)

