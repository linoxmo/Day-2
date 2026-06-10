class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self.growth = growth

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self.name} : Error, height can’t be negative")
            print("Height update rejected")
            return
        self._height = new_height

    """
    def get_age(self) -> int :
        return self._age
    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.name} : Error, age can’t be negative")
            print("Age update rejected")
            return
        self._age = new_age
    """
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.name} : Error, age can’t be negative")
            print("Age update rejected")
            return
        self._age = new_age

    def show(self) -> None:
        print(f"Plant created: {self._name}: ", end="")
        print(f"{round(self._height)}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += self.growth
        print(f"Height updated: {round(self.height)}cm")

    def aging(self) -> None:
        self._age += 20
        print(f"Age updated: {self._age} days")

    def show_cur(self) -> None:
        print(f"Current state: {self._name}: {self._height}cm, ", end="")
        print(f"{self._age} days old")

    def age_growth(self) -> None:
        self.aging()
        self.grow()


print("=== Garden Security System ===")

rose = Plant("Rose", 15.0, 10, 1.0)

print("Plant created:", end=" ")
rose.show()

rose.height = 25
print("Height updated: 25cm")

rose.age = 30
print("Age updated: 30 days")

rose.height = -5
print("Height update rejected")

rose.age = -10
print("Age update rejected")

print("Current state:", end=" ")
rose.show()
