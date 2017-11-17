import unittest
from main import *

import math

class MeusTestes(unittest.TestCase):
    def testMover_vaca(self):
        # Vaca andando para frente (sem bater na parede)
        self.assertEqual(mover_vaca(Vaca(x=PAREDE_ESQUERDA, dx=10)), Vaca(x=PAREDE_ESQUERDA + 10, dx=10))
        self.assertEqual(mover_vaca(Vaca(LARGURA / 2, 10)), Vaca(LARGURA / 2 + 10, 10))

        # Vaca andando para tras (sem bater na parede)
        self.assertEqual(mover_vaca(Vaca(LARGURA / 2, -10)), Vaca(LARGURA / 2 - 10, -10))

        # Vaca no limite direito, e tendo que voltar
        self.assertEqual(mover_vaca(Vaca(PAREDE_DIREITA, 10)), Vaca(PAREDE_DIREITA - 10, -10))

        # Vaca no limite esquerdo, e tendo que voltar
        self.assertEqual(mover_vaca(Vaca(PAREDE_ESQUERDA, -10)), Vaca(PAREDE_ESQUERDA + 10, 10))

        # Vaca quase atingindo limite direito, e parando no limite
        self.assertEqual(mover_vaca(Vaca(PAREDE_DIREITA - 2, 10)), Vaca(PAREDE_DIREITA, 10))
        self.assertEqual(mover_vaca(Vaca(PAREDE_DIREITA - 1, 10)), Vaca(PAREDE_DIREITA, 10))

        # Vaca quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(mover_vaca(Vaca(PAREDE_ESQUERDA + 2, -10)), Vaca(PAREDE_ESQUERDA, -10))
        self.assertEqual(mover_vaca(Vaca(PAREDE_ESQUERDA + 1, -10)), Vaca(PAREDE_ESQUERDA, -10))

    def testMover_zumbi(self):
        # Zumbi andando para frente (sem bater na parede)
        self.assertEqual(mover_vaca(Zumbi(x=PAREDE_ESQUERDA, dx=1)), Zumbi(x=PAREDE_ESQUERDA + 1, dx=1))
        self.assertEqual(mover_zumbi(Zumbi(LARGURA / 2, 1)), Zumbi(LARGURA / 2 + 1, 1))

        # Zumbi andando para tras (sem bater na parede)
        self.assertEqual(mover_zumbi(Zumbi(LARGURA / 2, -1)), Zumbi(LARGURA / 2 - 1, -1))

        # Zumbi no limite direito, e tendo que voltar
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA, 1)), Zumbi(PAREDE_DIREITA - 1, -1))

        # Zumbi no limite esquerdo, e tendo que voltar
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA, -1)), Zumbi(PAREDE_ESQUERDA + 1, 1))

        # Zumbi quase atingindo limite direito, e parando no limite
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA - 1, 1)), Zumbi(PAREDE_DIREITA, 1))
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA - 1, 1)), Zumbi(PAREDE_DIREITA, 1))

        # Zumbi quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA + 2, -1)), Zumbi(PAREDE_ESQUERDA, -1))
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA + 1, -1)), Zumbi(PAREDE_ESQUERDA, -1))

    def testTrata_tecla(self):
        #VACA ANDANDO PARA DIREITA
        self.assertEqual(trata_tecla_vaca(Vaca(50, 10), pg.K_LEFT), Vaca(50, -10))

        #VACA ANDANDO PARA ESQUERDA
        self.assertEqual(trata_tecla_vaca(Vaca(50, -10), pg.K_RIGHT), Vaca(50, 10))

        #VACA ATIRANDO
        self.assertEqual(trata_tecla_vaca(Vaca(50, 10), pg.K_SPACE), Leite(50, 30))



    def testDistancia(self):
        self.assertEqual(distancia(0, 4, 3, 0), 5) 
        self.assertEqual(distancia(1, 2, 3, 4), math.sqrt((3 - 1) ** 2 + (4 - 2) ** 2))


    def testMover_jogo(self):
        self.assertEqual(mover_jogo(
            jogo(vaca=Vaca(PAREDE_ESQUERDA, 3),
                zumbi=Zumbi(jogo.zumbi.x, PAREDE_CIMA, 3),
                game_over=False)),

            Jogo(vaca=Vaca(PAREDE_ESQUERDA + 3, 3),
                zumbi=Zumbi(jogo.zumbi.x, PAREDE_CIMA + 3, 3),
                game_over=False))

        self.assertEqual(mover_jogo(
            Jogo(vaca=Vaca(jogo.zumbi.x, 3),
                 zumbi=Zumbi(jogo.zumbi.x, Y_VACA, 3),
                 game_over=False)),
            Jogo(vaca=Vaca(jogo.zumbi.x, 3),
                 zumbi=Zumbi(jogo.zumbi.x, Y_VACA, 3),
                 game_over=True))


    def testColidirem(self):
        self.assertFalse(colidirem(VACA_INICIAL, ZUMBI_INICIAL))
        self.assertTrue(colidirem(Vaca(jogo.zumbi.x, 10), Chupacabra(jogo.zumbi.x, Y_VACA, 10)))
        self.assertTrue(colidirem(
                        Vaca(jogo.zumbi.x, 10),
                        Chupacabra(jogo.zumbi.x, Y_VACA - IMG_VACA.get_width()//2 + 3, 10)))
            # unittest.main()

