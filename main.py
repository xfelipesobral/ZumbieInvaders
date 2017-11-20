#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *
import math
import random

''' ZUMBIE INVADERS 0.0.5 '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (800, 600)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_VACA = pg.image.load('img/vaca.png')
    IMG_ZUMBI = pg.image.load('img/zumbi.gif')
    IMG_BACKGROUND = pg.image.load('img/bg.jpg')
    IMG_BALA_Z = pg.image.load('img/bala.png')
    IMG_BALA_V = pg.image.load('img/leite.png')

except:
    IMG_VACA = pg.Surface((100,100),pg.SRCALPHA)
    IMG_ZUMBI = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BACKGROUND = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BALA_Z = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BALA_V = pg.Surface((100,100),pg.SRCALPHA)
    print("IMAGENS NÃO CARREGADAS!!!")

## CONSTANTES DE VACA ##
IMG_VACA = pg.transform.scale(IMG_VACA, (50, 50)) 
Y_VACA = 600 - IMG_VACA.get_width()/2 
DX = 10 # VELOCIDADE VACA
DV = 30 # VELOCIDADE TIRO DA VACA
IMG_BALA_V = pg.transform.scale(IMG_BALA_V, (10,20))

## CONSTANTES DE ZUMBI ##
DZ = 1 # VELOCIDADE ZUMBI
DZZ = 2 # VELOCIDADE TIRO ZUMBI
DESLOCAMENTO_ZUMBI = 80 # REPRESENTA O DESLOCAMENTO DO ZUMBI NA LINHA Y
IMG_ZUMBI = pg.transform.scale(IMG_ZUMBI, (50, 50))
IMG_ZUMBI_V = pg.transform.flip(IMG_ZUMBI, True, False)
IMG_BALA_Z = pg.transform.scale(IMG_BALA_Z,(10,20))

## CONSTANTES GERAIS ##
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
ZUMBI_INICIAL = Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, DZ)
ZUMBI1 = Zumbi(PAREDE_ESQUERDA+70 , PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)
ZUMBI2 = Zumbi(PAREDE_ESQUERDA+140, PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)
ZUMBI3 = Zumbi(PAREDE_ESQUERDA+210, PAREDE_CIMA + (IMG_ZUMBI.get_height())/2, DZ)

ZUMBI4 = Zumbi(PAREDE_ESQUERDA    , PAREDE_BAIXO/8, DZ)
ZUMBI5 = Zumbi(PAREDE_ESQUERDA+70 , PAREDE_BAIXO/8, DZ)
ZUMBI6 = Zumbi(PAREDE_ESQUERDA+140, PAREDE_BAIXO/8, DZ)
ZUMBI7 = Zumbi(PAREDE_ESQUERDA+210, PAREDE_BAIXO/8, DZ)



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
LEITE_INICIAL = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0)
LEITE_FINAL = Leite(PAREDE_CIMA, PAREDE_CIMA,  0)

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

Jogo = namedlist("Jogo", "vaca, zumbis, bala, leite, game_over, game_ganho")



''' 
Jogo eh criado como: Jogo(Vaca, List<Zumbi>, Bala, Leite, Boolean)
interp. Um jogo é composto por uma vaca, vários zumbis, tiro da vaca(leite), tiro do zumbi(bala),
e uma flag (game_over ou game_ganho) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''

JOGO_INICIAL = Jogo(VACA_INICIAL, [ZUMBI7, ZUMBI6, ZUMBI5, ZUMBI4, ZUMBI3, ZUMBI2, ZUMBI1, ZUMBI_INICIAL], BALA_INICIAL, LEITE_INICIAL, False, False)
JOGO_GAME_OVER = Jogo(VACA_INICIAL, ZUMBI_INICIAL, BALA_INICIAL, LEITE_INICIAL, True, False)
JOGO_GAME_GANHO = Jogo(VACA_INICIAL, ZUMBI_INICIAL, BALA_INICIAL, LEITE_INICIAL, False, True)

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
        #usar depurador (debugger)

        #calcula novo x
        zumbi.x = zumbi.x + zumbi.dx

        if zumbi.x > PAREDE_DIREITA:
            zumbi.x = PAREDE_DIREITA
        elif zumbi.x < PAREDE_ESQUERDA:
            zumbi.x = PAREDE_ESQUERDA

        return zumbi

def mover_leite(leite):
    if leite.y < 0 or leite.y > ALTURA:
        return "Erro: leite invalida"
    else:
        #calcula novo dy
        if (leite.y == PAREDE_BAIXO and leite.dy > 0):
            leite.dy = - leite.dy
        if (leite.y == PAREDE_CIMA and leite.dy < 0):  
            leite.dy = 0 ## CASO CHEGUE NA PAREDE CIMA O DV ZERA
            leite.y = PAREDE_BAIXO ## E VOLTA PARA SEU LUGAR PRINCIPAL
        #usar depurador (debugger)

        #calcula novo y
        leite.y = leite.y + leite.dy

        if leite.y > PAREDE_BAIXO:
            leite.y = PAREDE_BAIXO
        elif leite.y < PAREDE_CIMA:
            leite.y = PAREDE_CIMA

        return leite

def mover_bala(bala):
    if bala.y < 0 or bala.y > ALTURA:
        return "Erro: bala invalida"
    else:
        #calcula novo y
        bala.y = bala.y + bala.dy
        bala.dy = bala.dy

        if bala.y > PAREDE_BAIXO:
            bala.y = PAREDE_BAIXO
        elif bala.y < PAREDE_CIMA:
            bala.y = PAREDE_CIMA

        return bala


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
def colidirem(vaca, leite, bala, zumbi):
    raio1 = IMG_VACA.get_width()/2
    raio2 = IMG_ZUMBI.get_width()/2
    raio3 = IMG_BALA_V.get_width()/2
    raio4 = IMG_BALA_Z.get_width()/2

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
    d = distancia(leite.x, leite.y, zumbi.x, zumbi.y) ## LEITE /=/ ZUMBI = GANHOU
    if d <= raio3 + raio2:
        return 2

    return 0

'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
!!!
'''
def mover_jogo(jogo):
    zumbis_vivos = len(jogo.zumbis) ## CONTA QUANTOS ZUMBIS ESTÃO 'VIVOS', QUANTOS ZUMBIS QUE ESTÃO NA LISTA

    for zumbi in jogo.zumbis:

        if colidirem(jogo.vaca, jogo.leite, jogo.bala, zumbi) == 1: ## SE BALA DO ZUMBI OU ZUMBI CHEGAR A VACA_Y == PERDEU
            jogo.game_over = True
            return jogo

        if colidirem(jogo.vaca, jogo.leite, jogo.bala, zumbi) == 2:
            jogo.leite = Leite(PAREDE_BAIXO, PAREDE_BAIXO, 0) ## VOLTA A BALA PARA O SEU ESTADO INICIAL

            if zumbis_vivos == 1: ## SE TIVER SÓ UM ZUMBI VIVO, QUANDO ELE MORRER...
                jogo.zumbis.remove(zumbi)
                jogo.game_ganho = True
                return jogo

            jogo.zumbis.remove(zumbi)


    #else
    mover_vaca(jogo.vaca)


    # CASO O LEITE ESTEJA NO Y INICIAL
    if jogo.leite.y >= PAREDE_BAIXO-(IMG_VACA.get_height()):
        jogo.leite.x = jogo.vaca.x #SE SIM, ELE RECEBE X DA VACA
    

    mover_leite(jogo.leite)
    
    # SE O Y FOR > QUE A PAREDE BAIXO | ESSA CONDIÇÃO FAZ COM QUE A BALA SAIA SEMPRE DO ZUMBI
    if jogo.bala.y>=PAREDE_BAIXO:
        

        novaBala = random.randint(0,(zumbis_vivos-1))
        jogo.bala.x = jogo.zumbis[novaBala].x
        jogo.bala.y = jogo.zumbis[novaBala].y # Y DA BALA RECEBE Y DO ZUMBI



    for zumbi in jogo.zumbis:

        # SE O Y DA BALA == 0, OU SEJA COMEÇAR PARA FORA DO JOGO; A BALA RECEBE X DO ZUMBI
        if jogo.bala.y == 0: 
            novaBala = random.randint(0,(zumbis_vivos-1))
            print(novaBala)  
            jogo.bala.x = jogo.zumbis[novaBala].x

        mover_bala(jogo.bala)
        mover_zumbi(zumbi)  # funcao auxiliar (helper)

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

##screen.blit(background, backgroundRect)

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
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    if jogo.game_over:
        desenha_fundo()
        desenha_vaca(jogo.vaca)
        fonte = pg.font.SysFont("monospace", 40)
        texto = fonte.render("VOCE PERDEU", 1, (255, 255, 255))
        TELA.blit(texto, ((LARGURA/2)-110, ALTURA/2))

    elif jogo.game_ganho:
        desenha_fundo()
        desenha_vaca(jogo.vaca)
        fonte = pg.font.SysFont("monospace", 40)
        texto = fonte.render("VOCE GANHOU", 1, (255, 255, 255))
        TELA.blit(texto, ((LARGURA/2)-110, ALTURA/2))

    else:
        desenha_fundo()
        desenha_bala(jogo.bala)
        desenha_leite(jogo.leite)
        desenha_vaca(jogo.vaca)
        
        for zumbi in jogo.zumbis:
            desenha_zumbi(zumbi)



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
    if leite.y != PAREDE_BAIXO:
        return leite
    else:
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
Trata tecla geral
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
        jogo.leite = trata_tecla_leite(jogo.leite, tecla)
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
             quando_tecla=trata_tecla,
             quando_solta_tecla=trata_solta_tecla)

main(JOGO_INICIAL)

