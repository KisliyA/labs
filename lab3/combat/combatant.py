from abc import ABC, abstractmethod
from .hit import Hit
class Combatant(ABC):
    @property
    @abstractmethod
    def code(self) -> str: pass
    @property
    @abstractmethod
    def name(self) -> str: pass
    @property
    @abstractmethod
    def health(self) -> int: pass
    @property
    @abstractmethod
    def max_health(self) -> int: pass
    @abstractmethod
    def is_alive(self) -> bool: pass
    @abstractmethod
    def roll_damage(self) -> Hit: pass
    @abstractmethod
    def receive_hit(self, damage: int) -> int: pass