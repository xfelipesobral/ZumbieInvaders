#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *
import math
import random

'''

ZUMBIE INVADERS 0.0.6

DESENVOLVEDORES: LUAN UMERES & FELIPE SOBRAL


O QUE FALTA?
ADIÇÃO DOS FENOS
*** TIROS SEGUIDOS *** !!!
'''

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
    IMG_MUNICAO = pg.image.load('img/municao.png')

except:
    IMG_VACA = pg.Surface((100,100),pg.SRCALPHA)
    IMG_ZUMBI = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BACKGROUND = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BALA_Z = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BALA_V = pg.Surface((100,100),pg.SRCALPHA)
    IMG_MUNICAO = pg.Surface((100,100),pg.SRCALPHA)
    print("IMAGENS NÃO CARREGADAS!!!")

## CONSTANTES DE VACA ##
IMG_VACA = pg.transform.scale(IMG_VACA, (50, 50)) 
Y_VACA = 600 - IMG_VACA.get_width()/2 
DX = 10 # VELOCIDADE VACA
DV = 30 # VELOCIDADE TIRO DA VACA
IMG_BALA_V = pg.transform.scale(IMG_BALA_V, (10,20))
IMG_MUNICAO = pg.transform.scale(IMG_MUNICAO, (25, 25))

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
Y_FENO = PAREDE_BAIXO/4


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

## SEGUNDA LINHA ##
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

'''
COMEÇANDO CRIAR PAREDE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Para se criar uma parede será utilizado apenas um valor do eixo X CONSTANTE + Sua devida matriz
'''


#######################################################################################################################################

Jogo = namedlist("Jogo", "vaca, zumbis, bala, leites, municao, game_over, game_ganho")

''' 
Jogo eh criado como: Jogo(Vaca, List<Zumbi>, Bala, List<Leite>, Municao, Boolean)
interp. Um jogo é composto por uma vaca, vários zumbis, a vaca tem carga de 5 tiros (5 Leites na lista), tiro do zumbi(bala),
e duas flagg (game_over ou game_ganho) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''

JOGO_INICIAL    = Jogo(VACA_INICIAL, [ZUMBI7, ZUMBI6, ZUMBI5, ZUMBI4, ZUMBI3, ZUMBI2, ZUMBI1, ZUMBI_INICIAL], BALA_INICIAL, [L4, L3, L2, L1, LEITE_INICIAL], MUNICAO_INICIAL, False, False)
JOGO_GAME_OVER  = Jogo(VACA_INICIAL, [ZUMBI7, ZUMBI6, ZUMBI5, ZUMBI4, ZUMBI3, ZUMBI2, ZUMBI1, ZUMBI_INICIAL], BALA_INICIAL, [L4, L3, L2, L1, LEITE_INICIAL], MUNICAO_INICIAL, True, False)
JOGO_GAME_GANHO = Jogo(VACA_INICIAL, [ZUMBI7, ZUMBI6, ZUMBI5, ZUMBI4, ZUMBI3, ZUMBI2, ZUMBI1, ZUMBI_INICIAL], BALA_INICIAL, [L4, L3, L2, L1, LEITE_INICIAL], MUNICAO_INICIAL, False, True)

'''
Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.zumbis
        jogo.bala
        jogo.leites
        jogo.municao
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
        bala.dy = bala.dy

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

    d = distancia(vaca.x, Y_VACA, municao.x, Y_VACA)
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
    if leite != None: 
        d = distancia(leite.x, leite.y, zumbi.x, zumbi.y) ## LEITE /=/ ZUMBI = GANHOU
        if d <= raio3 + raio2:
            return 2

    return 0

'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
'''
def mover_jogo(jogo):
    zumbis_vivos = len(jogo.zumbis) ## CONTA QUANTOS ZUMBIS ESTÃO 'VIVOS', QUANTOS ZUMBIS QUE ESTÃO NA LISTA

    for zumbi in jogo.zumbis:
        if colidirem(jogo.vaca, None, jogo.bala, zumbi) == 1: ## SE BALA DO ZUMBI OU ZUMBI CHEGAR A VACA_Y == PERDEU
            jogo.game_over = True
            return jogo

        for leite in jogo.leites:
            if colidirem(jogo.vaca, leite, jogo.bala, zumbi) == 2:
                jogo.leites.remove(leite)

                if zumbis_vivos == 1: ## SE TIVER SÓ UM ZUMBI VIVO, QUANDO ELE MORRER...
                    jogo.zumbis.remove(zumbi)
                    jogo.game_ganho = True
                    return jogo

                jogo.zumbis.remove(zumbi)


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
        desenha_municao(jogo.municao)
        
        for leite in jogo.leites:
            desenha_leite(leite)

        desenha_vaca(jogo.vaca)
        
        for zumbi in jogo.zumbis:
            desenha_zumbi(zumbi)


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

        ## EM CONSTRUÇÃO ##
        municao_vaca = len(jogo.leites)

        
        if municao_vaca != 0:

            if  jogo.leites[municao_vaca-1].dy == 0: ### SE LEITE[N] == 0 (ATIRA)  
                jogo.leites[municao_vaca-1] = trata_tecla_leite(jogo.leites[municao_vaca-1], tecla)
            elif jogo.leites[municao_vaca-2].dy == 0: ### SENÃO - SE LEITE[N-1] == 0 (ATIRA)
                    jogo.leites[municao_vaca-2] = trata_tecla_leite(jogo.leites[municao_vaca-2], tecla)

            ## SENÃO (NÃO ATIRA)
            

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

