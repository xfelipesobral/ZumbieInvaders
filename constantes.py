from universe import *

'''
====================
 TELA E CONSTANTES
====================
'''

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