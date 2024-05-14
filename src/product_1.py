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
    def create_product(cls, prod_dict):
        title = prod_dict ['name']
        description = prod_dict ['description']
        price = prod_dict ['price']
        quantity_in_stock = prod_dict ['quantity']
        return cls(title, description, price, quantity_in_stock)

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price
    @price.setter
    def price(self, value):
        """Сеттер для проверки цены"""
        price = value
        if price <= 0:
            print('Цена введена некорректная')
            return self.__price
        self.__price = price
















