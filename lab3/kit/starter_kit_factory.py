from abc import ABC, abstractmethod
from ..item.armor import Armor
from ..item.weapon import Weapon
class StarterKitFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon: pass
    @abstractmethod
    def create_armor(self) -> Armor: pass