import unittest
from funcoes import *

class MeusTestes(unittest.TestCase):
    def teste_moverVaca(self):

        # MORVER VACA PARA DIREITA
        self.assertEqual(mover_vaca(Vaca(LARGURA/2, 0), Vaca((LARGURA/2)+DX, DX)))

        # MORVER VACA PARA ESQUERDA
        self.assertEqual(mover_vaca(Vaca(LARGURA/2, 0), Vaca((LARGURA/2)-DX, DX)))


    def teste_moverZumbi(self):

        # MOVER ZUMBI PARA DIREITA
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, DZ), Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA+DZ, DZ)))

        #MOVER P/ DIREITA E DESCER
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, DZ), Zumbi(PAREDE_DIREITA, PAREDE_DIREITA+DESLOCAMENTO_ZUMBI, DZ)))

        #MVOER PARA ESQUERDA
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA, PAREDE_DIREITA, DZ), Zumbi(PAREDE_DIREITA-DZ,PAREDE_DIREITA, DZ)))

    def teste_moverLeite(self):

        #mover leite para cima
        self.assertEqual(mover_leite(PAREDE_BAIXO, PAREDE_BAIXO, 0), leite(PAREDE_BAIXO, PAREDE_BAIXO-DZ, DZ))

    def teste_moverBala(self):

        #bala para baixo
        self.assertEqual(mover_bala(PAREDE_CIMA, PAREDE_CIMA, DZZ), bala(PAREDE_CIMA, PAREDE_CIMA+DZZ, DZZ))

    def teste_matarVaca(self):

        #quando o tiro do zumbie acerta a vaca
        self.assertEqual(colidir_municao(VACA_INICIAL, BALA, DZZ)), colidir_municao(VACA_INICIAL, VACA_INICIAL+DZZ)

    def teste_matarZumbie(self):

        #quando o tiro da vaca acerta o zumbie
        self.assertEqual(colidir_municao(ZUMBIE_FINAL, LEITE), colidir_municao(ZUMBIE_FINAL, ZUMBIE_FINAL+DZ))

    






   


    #unittest.main()