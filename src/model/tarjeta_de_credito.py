TASA_DE_USURA = 12.4

from src.model.compra import Compra
from dataclasses import dataclass, field

@dataclass
class TarjetaDeCredito:
    tasa_interes: float
    compras: list[Compra] = field(default_factory=list)

    def agregar_compra(self, compra:Compra):
        self.compras.append(compra)

    def calcular_total_interes(self) -> float:
        pass
