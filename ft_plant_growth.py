class Plant:
    def  __init__(self, name: str, height: float, age:int, growth:float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth
    def get_name(self) -> str:
        return self.name
    def set_name(self, new_name) -> None:
        self.name = new_name
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} years old")
    def grow(self)-> None:
        self.height += self.growth
    def aging(self) -> None:
        self.age += 1
    def age_growth(self, i: int) -> None :
        print(f"=== Day {i} ===")
        self.aging()
        self.grow()


if  __name__ == '__main__':
    i = 0
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30, 0.8)
    for i in range(1, 8, 1):
        rose.age_growth(i)
