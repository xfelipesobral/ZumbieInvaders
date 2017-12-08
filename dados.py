#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *

'''
====================
	 DEF. DADOS
====================
'''

from namedlist import namedlist
Vaca = namedlist("Vaca", "x, dx") #Estrutura da vaca

''' 
Vaca pode ser criada como: Vaca(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
interp.: representa a posicao x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''

VACA_INICIAL = Vaca(LARGURA/2, 0)
VACA_FINAL = Vaca(PAREDE_DIREITA, 0)
VACA_FINAL2 = Vaca(PAREDE_ESQUERDA, 0)

'''
Template para funções que recebem Vaca:
def fn_para_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        ... v.x
            v.dx

'''

Zumbi = namedlist("Zumbi", "x, y, dx") #Estrutura do Zumbi

'''
Zumbi pode ser criado como: Zumbi(Int[PAREDE_ESQUERDA/PAREDE_DIREITA], Int[PAREDE_ESQUERDA/PAREDE_DIREITA], Int)
Interp.: X e Y representa a posicao do zumbi, e dx representa o deslocamento
a cada tick respectivamente no eixo x
Exemplos:
'''

ZUMBI_FINAL = Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, DZ)
ZUMBI_VOLTANDO = Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, -DZ)
ZUMBI_FINAL_VOLTANDO = Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, -DZ)

## PRIMEIRA LINHA ##
L1_ZUMBI1 = Zumbi(PAREDE_ESQUERDA+(70*0), PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)
L1_ZUMBI2 = Zumbi(PAREDE_ESQUERDA+(70*1), PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)
L1_ZUMBI3 = Zumbi(PAREDE_ESQUERDA+(70*2), PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)
L1_ZUMBI4 = Zumbi(PAREDE_ESQUERDA+(70*3), PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)
L1_ZUMBI5 = Zumbi(PAREDE_ESQUERDA+(70*4), PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ) 
L1_ZUMBI6 = Zumbi(PAREDE_ESQUERDA+(70*5), PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)

## SEGUNDA LINHA ##
L2_ZUMBI1 = Zumbi(PAREDE_DIREITA-(70*0.5), PAREDE_BAIXO/8, -DZ)
L2_ZUMBI2 = Zumbi(PAREDE_DIREITA-(70*1.5), PAREDE_BAIXO/8, -DZ)
L2_ZUMBI3 = Zumbi(PAREDE_DIREITA-(70*2.5), PAREDE_BAIXO/8, -DZ)
L2_ZUMBI4 = Zumbi(PAREDE_DIREITA-(70*3.5), PAREDE_BAIXO/8, -DZ)
L2_ZUMBI5 = Zumbi(PAREDE_DIREITA-(70*4.5), PAREDE_BAIXO/8, -DZ) 
L2_ZUMBI6 = Zumbi(PAREDE_DIREITA-(70*5.5), PAREDE_BAIXO/8, -DZ)

## TERCEIRA LINHA ##
L3_ZUMBI1 = Zumbi(PAREDE_ESQUERDA+(70*0.7), PAREDE_BAIXO/8 + IMG_ZUMBI.get_height(), DZ)
L3_ZUMBI2 = Zumbi(PAREDE_ESQUERDA+(70*1.7), PAREDE_BAIXO/8 + IMG_ZUMBI.get_height(), DZ)
L3_ZUMBI3 = Zumbi(PAREDE_ESQUERDA+(70*2.7), PAREDE_BAIXO/8 + IMG_ZUMBI.get_height(), DZ)
L3_ZUMBI4 = Zumbi(PAREDE_ESQUERDA+(70*3.7), PAREDE_BAIXO/8 + IMG_ZUMBI.get_height(), DZ)
L3_ZUMBI5 = Zumbi(PAREDE_ESQUERDA+(70*4.7), PAREDE_BAIXO/8 + IMG_ZUMBI.get_height(), DZ)
L3_ZUMBI6 = Zumbi(PAREDE_ESQUERDA+(70*5.7), PAREDE_BAIXO/8 + IMG_ZUMBI.get_height(), DZ)



'''
Template para funções que recebem Zumbi:
def fn_para_zumbi(z):
    if z.x < 0 or z.x > LARGURA:
        return "Erro: Zumbi invalido"
    else:
        ... z.x
        z.dx
'''


Leite = namedlist("Leite", "x, y, dy")

'''
Leite pode ser criado como: Leite(Int[vaca.x], Int[Y_VACA], Int)
Interp.: Y representa a posicao do leite, e dy representa o deslocamento
a cada tick respectivamente no eixo y
Exemplos:
'''

LEITE_INICIAL2 = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)
LEITE_FINAL = Leite(PAREDE_CIMA, PAREDE_CIMA,  0)

LEITE_INICIAL = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)
L1 = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)
L2 = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)
L3 = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)
L4 = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)

'''
Template para funções que recebem Leite:
def fn_para_leite(l):
    if l.y < 0 or l.y > ALTURA:
        return "Erro: Leite invalido"
    else:
        ... l.y
        l.dy
'''

Bala = namedlist("Bala", "x, y, dy")

'''
Bala pode ser criada como: Bala(Int[zumbi.x], Int[vaca.x], Int)
Interp.: Y representa a posicao do leite, e dy representa o deslocamento
a cada tick respectivamente no eixo y
Exemplos:
'''

BALA_INICIAL = Bala(PAREDE_CIMA, PAREDE_CIMA, DZZ)
BALA_FINAL = Bala(PAREDE_BAIXO, PAREDE_BAIXO, DZZ)

'''
Template para funções que recebem Bala:
def fn_para_bala(b):
    if b.y < 0 or b.y > ALTURA:
        return "Erro: Bala invalida"
    else:
        ... b.y
        b.dy
'''

Municao = namedlist("Municao", "x")

'''
Municao pode ser criada utilizando apenas o valor do eixo X que será gerado na "COLOCAR NOME DA FUNCAO"
'''

MUNICAO_INICIAL = Municao(PAREDE_ESQUERDA + 70)

'''
Template para funções que recebem Municao:
def fn_para_municao(municao):
    if municao.x < 0:
        return "Erro: Municao fora do mapa"
    else:
        municao.x = random.randint(PAREDE_ESQUERDA, PAREDE_DIREITA)

        ...
'''

Feno = namedlist("Feno","x,y")

'''
Feno pode ser criado utilizando apenas valores de x e y
'''

# TUPLA FENO 1
F1_1 = Feno(PAREDE_ESQUERDA+170, ALTURA-150)
F1_2 = Feno(PAREDE_ESQUERDA+170+(IMG_FENO.get_height()), ALTURA-150)
F1_3 = Feno(PAREDE_ESQUERDA+170+(IMG_FENO.get_height()/2), ALTURA-200)

# TUPLA FENO 2
F2_1 = Feno(PAREDE_DIREITA-170, ALTURA-150)
F2_2 = Feno(PAREDE_DIREITA-170-(IMG_FENO.get_height()), ALTURA-150)
F2_3 = Feno(PAREDE_DIREITA-170-(IMG_FENO.get_height()/2), ALTURA-200)

# TUPLA FENO 3
F3_1 = Feno(PAREDE_DIREITA/2-17, ALTURA-150) 
F3_2 = Feno(PAREDE_DIREITA/2-17+(IMG_FENO.get_height()), ALTURA-150)
F3_3 = Feno(PAREDE_DIREITA/2-17+(IMG_FENO.get_height()/2), ALTURA-200)

# TUPLA FENO 4
F4_1 = Feno(PAREDE_ESQUERDA+(IMG_FENO.get_height()/2), ALTURA-150)
F4_2 = Feno(PAREDE_ESQUERDA+(IMG_FENO.get_height()/2)+(IMG_FENO.get_height()), ALTURA-150)
F4_3 = Feno(PAREDE_ESQUERDA+(IMG_FENO.get_height()/2)+(IMG_FENO.get_height()/2), ALTURA-200)

# TUPLA FENO 5
F5_1 = Feno(PAREDE_DIREITA-(IMG_FENO.get_height()/2), ALTURA-150)
F5_2 = Feno(PAREDE_DIREITA-(IMG_FENO.get_height()/2)-(IMG_FENO.get_height()), ALTURA-150)
F5_3 = Feno(PAREDE_DIREITA-(IMG_FENO.get_height()/2)-(IMG_FENO.get_height()/2), ALTURA-200)


'''
Template para funções que recebem Municao:
def desenha_feno(feno):
    tela.BLIT(IMG_FENO,(feno.x, feno.y))
        ...
'''




Jogo = namedlist("Jogo", "vaca, zumbis, bala, leites, municao, fenos, game_over, game_ganho")

''' 
Jogo eh criado como: Jogo(Vaca, List<Zumbi>, Bala, List<Leite>, Municao, Boolean)
interp. Um jogo é composto por uma vaca, vários zumbis, a vaca tem carga de 5 tiros (5 Leites na lista), tiro do zumbi(bala),
e duas flagg (game_over ou game_ganho) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''

JOGO_INICIAL    = Jogo(VACA_INICIAL,
                  [L1_ZUMBI6, L1_ZUMBI5, L1_ZUMBI4, L1_ZUMBI3, L1_ZUMBI2, L1_ZUMBI1, L3_ZUMBI6, L3_ZUMBI5, L3_ZUMBI4, L3_ZUMBI3, L3_ZUMBI2, L3_ZUMBI1, L2_ZUMBI6, L2_ZUMBI5, L2_ZUMBI4, L2_ZUMBI3, L2_ZUMBI2, L2_ZUMBI1],
                  BALA_INICIAL, [L4, L3, L2, L1, LEITE_INICIAL], MUNICAO_INICIAL,
                  [F1_1, F1_2, F1_3, F2_1, F2_2, F2_3, F3_1, F3_2, F3_3, F4_3, F4_2, F4_1, F5_1, F5_2, F5_3], False, False)

JOGO_GAME_OVER  = Jogo(VACA_INICIAL,
                        [L2_ZUMBI4, L2_ZUMBI3, L2_ZUMBI2, L2_ZUMBI1, L1_ZUMBI4, L1_ZUMBI3, L1_ZUMBI2, L1_ZUMBI1],
                        BALA_INICIAL, [L4, L3, L2, L1, LEITE_INICIAL], MUNICAO_INICIAL,
                        [F1_1, F1_2, F1_3, F2_1, F2_2, F2_3, F3_1, F3_2, F3_3, F4_3, F4_2, F4_1, F5_1, F5_2, F5_3], True, False)

JOGO_GAME_GANHO = Jogo(VACA_INICIAL,
                        [L2_ZUMBI4, L2_ZUMBI3, L2_ZUMBI2, L2_ZUMBI1, L1_ZUMBI4, L1_ZUMBI3, L1_ZUMBI2, L1_ZUMBI1],
                        BALA_INICIAL, [L4, L3, L2, L1, LEITE_INICIAL], MUNICAO_INICIAL,
                        [F1_1, F1_2, F1_3, F2_1, F2_2, F2_3, F3_1, F3_2, F3_3, F4_3, F4_2, F4_1], False, True)

'''
Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.zumbis
        jogo.bala
        jogo.leites
        jogo.municao
        jogo.feno
        jogo.game_over
'''