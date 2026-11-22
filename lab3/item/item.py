import copy
from abc import ABC, abstractmethod
from .enchantment import Enchantment
class Item(ABC):
    def __init__(self, code: str, name: str, base_price: int):
        self._code = code
        self._name = name
        self._base_price = base_price
        self._enchantments = []
    def copy(self) -> "Item":
        clone = copy.copy(self)
        clone._enchantments = list(self._enchantments)
        return clone
    @property
    @abstractmethod
    def possible_enchantments(self) -> tuple[Enchantment, ...]: pass
    @property
    @abstractmethod
    def description(self) -> str: pass
    def enchant(self, enchantment: Enchantment):
        if enchantment not in self.possible_enchantments:
            raise ValueError(f"Зачарование '{enchantment.name}' не подходит для '{self._name}'")
        self._enchantments.append(enchantment)
    @property
    def code(self) -> str: return self._code
    @property
    def name(self) -> str: return self._name
    @property
    def price(self) -> int: return self._base_price + sum(e.bonus_price for e in self._enchantments)
    @property
    def enchantments(self) -> tuple[Enchantment, ...]: return tuple(self._enchantments)