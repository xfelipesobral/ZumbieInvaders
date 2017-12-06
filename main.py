#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funcoes import *

'''

ZUMBIE INVADERS 0.0.7

DESENVOLVEDORES: LUAN UMERES & FELIPE SOBRAL
'''

'''
====================
      MAIN
====================
'''

''' Jogo -> Jogo '''
''' inicie o mundo com main(JOGO_INICIAL) '''

def main(inic):
    big_bang(inic, tela=TELA,
    		 frequencia = 30,
    		 quando_tick=mover_jogo,
             desenhar=desenha_jogo,
             quando_tecla=trata_tecla,
             quando_solta_tecla=trata_solta_tecla)

main(JOGO_INICIAL)

