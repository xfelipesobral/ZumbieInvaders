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