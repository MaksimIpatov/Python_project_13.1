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
        self.price = price
        self.quantity_in_stock = quantity_in_stock
