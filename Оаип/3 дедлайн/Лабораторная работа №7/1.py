from dataclasses import dataclass
@dataclass(frozen=True)
class Product:
    name:str
    price:float
    weight:float
    is_available:bool
    def order_cost(self,quantity):
        return self.price*quantity