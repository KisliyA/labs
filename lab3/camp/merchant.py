from ..core.unknown_code_error import UnknownCodeError
from ..hero.hero import Hero
from ..item.item import Item
from ..item.item_catalog import ItemCatalog
SELL_PRICE_PERCENT = 50
class Merchant:
    def __init__(self, catalog: ItemCatalog, assortment: list[str]):
        self._catalog = catalog
        self._assortment = tuple(assortment)
    @property
    def showcase(self) -> list[Item]: return [self._catalog.create(code) for code in self._assortment]
    def buy(self, hero: Hero, code: str) -> Item:
        if code not in self._assortment: raise UnknownCodeError("Товар", code)
        item = self._catalog.create(code)
        hero.spend_gold(item.price)
        hero.add_item(item)
        return item
    def sell(self, hero: Hero, item: Item) -> int:
        price = self.sell_price(item)
        hero.remove_item(item)
        hero.add_gold(price)
        return price
    def sell_price(self, item: Item) -> int: return item.price * SELL_PRICE_PERCENT // 100