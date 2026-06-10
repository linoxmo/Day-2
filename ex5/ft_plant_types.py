class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def show(self) -> None:
        print(f"{self.name}: {round(self.height)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def aging(self) -> None:
        self.age += 1

    def age_growth(self) -> None:
        self.aging()
        self.grow()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, age, growth)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        if not (self._bloomed):
            print("[asking the rose to bloom]")
            self._bloomed = True
            self.show()

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not (self._bloomed):
            print(f"{self.name} has not bloomed yet!")
        if (self._bloomed):
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade", end="")
        print(f"of {self.height}cm long and {self._trunk_diameter} cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, season: str, NV: float) -> None:
        super().__init__(name, height, age, growth)
        self._season = season
        self._NV = NV

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._season}\nNutritional value: {self._NV}")


if (__name__ == '__main__'):
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Marguerite = Flower("Marguerite", 8, 13, 0.2, "blanche")
    Marguerite.show()
    Marguerite.bloom()
    print()
    print("=== Tree")
    Chestnuts = Tree("Chestnutes", 200, 365, 0, 5)
    Chestnuts.show()
    Chestnuts.produce_shade()
    print("\n=== Vegetable")
    Tomato = Vegetable("Tomato", 5, 10, 2.1, "April", 20)
    Tomato.show()
    print("[make tomato grow and age for 20 days]")
    Tomato.show()
