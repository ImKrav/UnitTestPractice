import pytest

from src.model.tarjeta_de_credito import TarjetaDeCredito
from src.mode.compra import Compra

def test_caso_36_cuotas():
    tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
    compra: Compra = Compra(200000,36,3.1)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes : float = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 134726.53