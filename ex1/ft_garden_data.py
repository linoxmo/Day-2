class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} years old")


if __name__ == '__main__':
    print("=== Garden Plant Registry ===")
    Rose = Plant("Rose", 25, 30)
    Rose.show()
    Sunflower = Plant("Sunflower", 80, 30)
    Sunflower.show()
    Cactus = Plant("Cactus", 15, 120)
    Cactus.show()
