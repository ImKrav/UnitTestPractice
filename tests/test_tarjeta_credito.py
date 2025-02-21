import pytest


from src.model.tarjeta_de_credito import TarjetaDeCredito
from src.model.compra import Compra

from src.errors.error_tasa_usura import ErrorTasaUsura
from src.errors.error_monto_invalido import ErrorMontoInvalido
from src.errors.error_cuota_negativa import ErrorCuotaNegativa

def test_caso_36_cuotas():
    tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
    compra: Compra = Compra(200000,36,3.1)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes : float = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 134726.53

def test_caso_24_cuotas():
    tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
    compra: Compra = Compra(850000,24,3.4)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes : float = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 407059.97

def test_caso_0_interes():
    tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
    compra: Compra = Compra(480000,48,0)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes : float = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0

def test_caso_usura():
    with pytest.raises(ErrorTasaUsura):
        tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
        compra: Compra = Compra(50000,60,12.5)
        tarjeta_de_credito.agregar_compra(compra)
        tarjeta_de_credito.calcular_total_interes()

def test_caso_cuota_unica():
    tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
    compra: Compra = Compra(90000,1,2.4)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes : float = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0

def test_caso_monto_invalido():
    with pytest.raises(ErrorMontoInvalido):
        tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
        compra: Compra = Compra(0,60,2.4)
        tarjeta_de_credito.agregar_compra(compra)

def test_caso_cuota_negativa():
    with pytest.raises(ErrorCuotaNegativa):
        tarjeta_de_credito : TarjetaDeCredito = TarjetaDeCredito(3.1)
        compra: Compra = Compra(50000,-10,1)
        tarjeta_de_credito.agregar_compra(compra)
