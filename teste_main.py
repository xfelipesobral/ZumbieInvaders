import unittest
from main import *


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

    def testTrata_tecla(self):
        self.assertEqual(trata_tecla_vaca(Vaca(50, 10), pg.K_LEFT), Vaca(50, -10))
        self.assertEqual(trata_tecla_vaca(Vaca(50, -10), pg.K_RIGHT), Vaca(50, 10))
        self.assertEqual(trata_tecla_vaca(Vaca(50, 10), pg.K_SPACE), Leite(50, 30))

    def testMover_zumbi(self):
        # Chupacabra andando para frente (sem bater na parede)
        self.assertEqual(mover_zumbi(Zumbi(x=PAREDE_ESQUERDA, dx=5)), Vaca(x=PAREDE_ESQUERDA + 5, dx=5))
        self.assertEqual(mover_zumbi(Zumbi(LARGURA / 2, 5)), Vaca(LARGURA / 2 + 10, 10))

        # Vaca andando para tras (sem bater na parede)
        self.assertEqual(mover_zumbi(Zumbi(LARGURA / 2, -5)), Vaca(LARGURA / 2 - 5, -5))

        # Vaca no limite direito, e tendo que voltar
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA, 5)), Vaca(PAREDE_DIREITA - 5, -5))

        # Vaca no limite esquerdo, e tendo que voltar
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA, -5)), Vaca(PAREDE_ESQUERDA + 10, 5))

        # Vaca quase atingindo limite direito, e parando no limite
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA - 2, 5)), Vaca(PAREDE_DIREITA, 5))
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_DIREITA - 1, 5)), Vaca(PAREDE_DIREITA, 5))

        # Vaca quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA + 2, -5)), Vaca(PAREDE_ESQUERDA, -5))
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA + 1, -5)), Vaca(PAREDE_ESQUERDA, -5))




    def testDistancia(self):
        self.assertEqual(distancia(0, 4, 3, 0), 5)
        import math
        self.assertEqual(distancia(1, 2, 3, 4), math.sqrt((3 - 1) ** 2 + (4 - 2) ** 2))


    def testMover_jogo(self):
        self.assertEqual(mover_jogo(
                            Jogo(vaca=Vaca(PAREDE_ESQUERDA, 3),
                                zumbi=zumbi(X_CC, PAREDE_CIMA, 3),
                                game_over=False)),
                         Jogo(vaca=Vaca(PAREDE_ESQUERDA + 3, 3),
                              chupacabra=Chupacabra(X_CC, PAREDE_CIMA + 3, 3),
                              game_over=False) )

        self.assertEqual(mover_jogo(
            Jogo(vaca=Vaca(X_CC, 3),
                 chupacabra=Chupacabra(X_CC, Y_VACA, 3),
                 game_over=False)),
            Jogo(vaca=Vaca(X_CC, 3),
                 chupacabra=Chupacabra(X_CC, Y_VACA, 3),
                 game_over=True))


    def testColidirem(self):
        self.assertFalse(colidirem(VACA_INICIAL, CC_INICIAL))
        self.assertTrue(colidirem(Vaca(X_CC, 3), Chupacabra(X_CC, Y_VACA, 3)))
        self.assertTrue(colidirem(
                        Vaca(X_CC, 3),
                        Chupacabra(X_CC, Y_VACA - IMG_VACA_INO.get_width()//2 + 3, 3)))
            # unittest.main()

