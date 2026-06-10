class Plant:
    class Stat:
        def __init__(self) -> None:
            self.__nog = 0
            self.__noa = 0
            self.__nos = 0

        def set_nog(self, new_nog:  int) -> None:
            self.__nog = new_nog

        def get_nog(self) -> int:
            return self.__nog

        def set_noa(self, new_noa: int) -> None:
            self.__noa = new_noa

        def get_noa(self) -> int:
            return self.__noa

        def set_nos(self, new_nos: int) -> None:
            self.__nos = new_nos

        def get_nos(self) -> int:
            return self.__nos

    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth
        self.stat = self.Stat()

    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def show(self) -> None:
        if (round(self.height) == 0 or self.age == 0):
            self.anonymous()
        else:
            print(f"{self.name}: {round(self.height)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def aging(self) -> None:
        self.age += 1
        self.stat.set_noa(self.stat.get_noa() + 1)

    def age_growth(self) -> None:
        self.aging()
        self.grow()

    @classmethod
    def anonymous(cls) -> "Plant":
        return (Plant("Unknown", round(0.0), 0, round(0)))

    @staticmethod
    def check_age(value: int) -> None:
        if (value > (360)):
            print(f"Is {value} days more than a year -> True")
        else:
            print(f"Is {value} days more than a year? -> False")

    def show_stats(self) -> None:
        print(f"Stats : {self.stat.get_nog()} grow", end=" ")
        print(f"Stats : {self.stat.get_noa()} age", end=" ")
        print(f"Stats : {self.stat.get_nos()} show")


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
        print(f"Tree {self.name} now produces a shade of", end="")
        print(" {self.height}cm long and {self._trunk_diameter} cm wide.")

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


class Seed (Flower):
    def __init__(self, name: str, height: float, age: int,
                 growth: float, color: str, nbr_seed: int) -> None:
        super().__init__(name, height, age, growth, color)
        self.nbr_seed = nbr_seed

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.nbr_seed}")


if (__name__ == '__main__'):
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    rose.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    rose.show_stats()
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0, 5.0)
    oak.show()
    oak.show_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_stats()
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 42)
    sunflower.show()
    print()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.aging()
    sunflower.aging()
    sunflower.bloom()
    sunflower.show()
    sunflower.show_stats()
    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    unknown.show_stats()
