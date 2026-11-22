from lab3.console_view import ConsoleView
from lab3.core.dice import Dice
from lab3.hero.hero import Hero
from lab3.hero.hero_class import HeroClass
from lab3.item.default_catalog import IRON_SWORD, create_default_catalog
from lab3.item.enchantment import FIERY
from lab3.world.crypt import Crypt
from lab3.world.forest import Forest
def main():
    catalog = create_default_catalog()
    view = ConsoleView()
    print("===== Одиночка =====")
    first = Dice()
    second = Dice()
    print(f"Dice() возвращает один и тот же объект: {first is second}")
    print("\n===== Прототип =====")
    plain_sword = catalog.create(IRON_SWORD)
    fiery_sword = catalog.create(IRON_SWORD)
    fiery_sword.enchant(FIERY)
    print("Первая копия:        " + view.describe(plain_sword))
    print("Вторая копия:        " + view.describe(fiery_sword))
    print("Новая копия шаблона: " + view.describe(catalog.create(IRON_SWORD)))
    print(f"Копии - разные объекты: {plain_sword is not fiery_sword}")
    print("\n===== Абстрактная фабрика =====")
    for hero_class in HeroClass:
        kit = hero_class.starter_kit(catalog)
        print(f"{hero_class.display_name}: {view.describe(kit.create_weapon())}, {view.describe(kit.create_armor())}")
    print("\n===== Строитель =====")
    hero = (Hero.Builder().set_name("Артур").set_hero_class(HeroClass.WARRIOR).set_starter_kit(HeroClass.WARRIOR.starter_kit(catalog)).set_level(3).build())
    view.print_hero(hero)
    try: (Hero.Builder().set_hero_class(HeroClass.MAGE).set_starter_kit(HeroClass.MAGE.starter_kit(catalog)).build())
    except ValueError as error: print(f"Герой без имени не создается: {error}")
    try: Hero.Builder().set_name("Мерлин").build()
    except ValueError as error: print(f"Герой без класса не создается: {error}")
    print("\n===== Фабричный метод =====")
    forest = Forest(catalog)
    crypt = Crypt(catalog)
    view.print_report(forest.explore(hero, 7), forest.display_name)
    print()
    view.print_report(crypt.explore(hero, 7), crypt.display_name)
if __name__ == "__main__": main()