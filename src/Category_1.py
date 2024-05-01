
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
        self.products = products
        self.number_categories = number_categories
        self.unique_products = unique_products