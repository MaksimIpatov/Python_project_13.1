# импорт Product не работает
from src.Product_1 import Product


class Category:
    """Класс категория обладает свойствами название, описание и списком товары"""
    title: str
    description: str
    products: []
    number_categories: int
    unique_products: int

    def __init__(self, title, description, products, number_categories, unique_products):
        """Инициализация экземпляров класса Category"""
        self.title = title
        self.description = description
        self.__products = products
        self.number_categories = number_categories
        self.unique_products = unique_products

    def add_product(self, new_product):
        self.__products.append(new_product)
    @property
    def get_product(self, product):
        for i in product:
            print(f"Продукт, int({self.price}) руб. Остаток: {self.quantity_in_stock} шт")





