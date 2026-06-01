class Plant:
    def  __init__(self, name: str, height: float, age:int, growth:float) -> None:
        self.__name = name
        self.__height = height
        self.__age = age
        self.growth = growth
    @property    
    def get_name(self) -> str:
        return self.name
    @name.setter
    def name(self, new_name) -> None:
        self.name = new_name
    @property
    def get_height(self) -> None:
        return self.height
    @height.setter
    def height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{name} : Error, height can’t be negative")
            print("Height update rejected")
            return
        self._height = new_height
    @property
    def get_age(self):
        return self.age
    @age.setter
    def age(self, new_age)
        if (new_age)
            print(f"{name} : Error, age can’t be negative")
            print("Age update rejected")
        self._age = new_age
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

