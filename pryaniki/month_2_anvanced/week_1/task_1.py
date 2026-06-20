
class Laptop:
    def __init__(self, name: str, gpu: str, ram: int) -> None:
        self.name = name
        self.gpu = gpu
        self.ram = ram
    def __str__(self):
        return f"Ноутбук: {self.name}, Видеокарта: {self.gpu}, ОЗУ: {self.ram} GB"
    def __repr__(self):
        return f"Laptop(name ='{self.name}', gpu='{self.gpu}', ram={self.ram})"
    def gpu_for_game(self, game_ram: int) -> bool:
        return self.ram >= game_ram
class GamingLaptop(Laptop):
    def __init__(self, name: str, gpu: str, ram: int, rgb_keyboard: str) -> None:
        super().__init__(name, gpu, ram)
        self.rgb_keyboard = rgb_keyboard
    def __str__(self):
        return f"Ноутбук: {self.name}, Видеокарта: {self.gpu}, ОЗУ: {self.ram} GB, RGB клавиатура: {self.rgb_keyboard}"
          
laptop1 = Laptop("ACER", "RTX 5080", 16)
laptop2 = Laptop("LENOVO", "RTX 4060", 32)
laptops = [laptop1, laptop2]
gaming_laptop1 = GamingLaptop("ASUS", "RTX 5080", 32, "Да")
print(f"Хватает ОЗУ для игры?: {laptop1.gpu_for_game(64)}")
print(laptops)
#ТЕСТОВЫЙ КОММЕНТАРИЙ