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
    IMG_BALA_V = pg.image.load('#')
    IMG_BALA_Z = pg.image.load('#')

except:
    IMG_VACA = pg.Surface((100,100),pg.SRCALPHA)
    IMG_ZUMBI = pg.Surface((100,100),pg.SRCALPHA)

Y_VACA = (ALTURA/2)/2
Y_ZUMBI = ALTURA/2

PAREDE_ESQUERDA = 0 + IMG_VACA.get_width()/2
PAREDE_DIREITA = LARGURA - IMG_VACA.get_width()/2

PAREDE_CIMA = IMG_BALA_V.get_height()/2
PAREDE_BAIXO = IMG_BALA_Z.get_height()/2

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

ZUMBI_INICIAL = Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, 2, 3)
ZUMBI_FINAL = Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, 2, 3)
ZUMBI_VOLTANDO = Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, -2, -3)
ZUMBI_FINAL_VOLTANDO = Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, -2, -3)


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
LEITE_ATIRAR = Leite(v.x, 35)
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
BALA_ATIRAR = Bala(z.x, 20)
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