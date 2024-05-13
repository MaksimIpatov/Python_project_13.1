class Product:
    """Класс продукты обладает свойствами название, описание, цена, количество в наличии"""
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        """Инициализация экземпляров класса Product"""
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock
    @classmethod
    def create_product(cls, prod_str):
        title, description, price = prod_str.split('-')
        return cls(title, description, price)
    @property
    def __price(self):
        """Геттер для получения цены"""
        return self.__price
    @price.setter
    def __price(self, value):
        """Сеттер для изменения цены"""
        price = value
        self.price = price












