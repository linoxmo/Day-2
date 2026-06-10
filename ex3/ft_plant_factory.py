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
        print(f"{self.name}: {round(self.height):.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def aging(self) -> None:
        self.age += 1

    def age_growth(self, i: int) -> None:
        print(f"=== Day {i} ===")
        self.aging()
        self.grow()


def main() -> None:
    plants = [
        Plant("Rose", 25.0, 30, 0.0),
        Plant("Oak", 200.0, 365, 0.0),
        Plant("Cactus", 5.0, 90, 0.0),
        Plant("Sunflower", 80.0, 45, 0.0),
        Plant("Fern", 15.0, 120, 0.0),
    ]

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
