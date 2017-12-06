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
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, DZ), Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, DZ)+DZ, DZ))

        # ZUMBI CAINDO NO Y

        ### SELF            FUNC_T              OBJETO SENDO TESTADO                             RESULTADO ESPERADO
        self.assertEqual(mover_zumbi(Zumbi(PAREDE_ESQUERDA, PAREDE_ESQUERDA, DZ), Zumbi(PAREDE_ESQUERDA, PAREDE_DIREITA-DESLOCAMENTO_ZUMBI, DZ)-DZ, DZ))

    unittest.main([teste_moverVaca, teste_moverZumbi])