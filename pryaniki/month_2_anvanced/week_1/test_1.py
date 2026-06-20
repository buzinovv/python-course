class Laptop:
    def __init__(self, name, gpu, ram, price):
        self.name = name
        self.gpu = gpu
        self.ram = ram
        self.price = price
    
    def __str__(self):
        return f"Ноутбук: {self.name}, Видеокарта: {self.gpu}, ОЗУ: {self.ram}"
    
    # Метод 1 — простое вычисление на основе данных объекта
    def get_price_with_discount(self, discount_percent):
        """Считает цену со скидкой."""
        discount_amount = self.price * (discount_percent / 100)
        return self.price - discount_amount
    
    # Метод 2 — проверка условия, возвращает True/False
    def is_gaming_ready(self):
        """Проверяет, подходит ли ноутбук для игр (по видеокарте RTX)."""
        return "RTX" in self.gpu
    
    # Метод 3 — изменяет данные самого объекта
    def upgrade_ram(self, new_ram):
        """Обновляет объём ОЗУ ноутбука."""
        print(f"Обновляем ОЗУ с {self.ram} на {new_ram}")
        self.ram = new_ram
    
    # Метод 4 — сравнение с другим объектом того же класса
    def is_more_expensive_than(self, other_laptop):
        """Сравнивает цену с другим ноутбуком."""
        return self.price > other_laptop.price

laptop1 = Laptop("ACER", "RTX 5080", "16 GB", 150000)
laptop2 = Laptop("LENOVO", "GTX 1650", "8 GB", 70000)

print(laptop1)
# Метод 1 — расчёт скидки
print(laptop1.get_price_with_discount(20))
# 120000.0  (150000 минус 20%)

# Метод 2 — проверка для игр
print(laptop1.is_gaming_ready())  # True (есть RTX)
print(laptop2.is_gaming_ready())  # False (GTX, не RTX)

# Метод 3 — изменение данных
laptop2.upgrade_ram("16 GB")
# Обновляем ОЗУ с 8 GB на 16 GB
print(laptop2.ram)  # 16 GB — данные реально изменились!

# Метод 4 — сравнение объектов
print(laptop2.is_more_expensive_than(laptop1))  # True