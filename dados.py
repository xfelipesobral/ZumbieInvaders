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