from src.model.tarjeta_de_credito import TarjetaDeCredito
from src.model.compra import Compra

compra = Compra(100000,24,3.1)
tarjeta_de_credito = TarjetaDeCredito(3.1)
tarjeta_de_credito.agregar_compra(compra)