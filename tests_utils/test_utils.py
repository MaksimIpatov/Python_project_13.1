
import pytest

from src.Category_1 import Category
from src.Product_1 import Product


@pytest.fixture
def test_category():
    return Category('Автотовары', 'Товары для авто', ['Ключи'], 7, 22)
def test_Category(test_category):
    assert test_category.title == 'Автотовары'
    assert test_category.description == 'Товары для авто'
    assert test_category.products == ['Ключи']
    assert test_category.number_categories == 7
    assert test_category.unique_products == 22


@pytest.fixture
def test_product():
    return Product('Хлеб', 'формовой', 49.99, 78)
def test_Product(test_product):
    assert test_product.title == 'Хлеб'
    assert test_product.description == 'формовой'
    assert test_product.price == 49.99
    assert test_product.quantity_in_stock == 78