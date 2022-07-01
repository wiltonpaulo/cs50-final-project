from project import add_customer, delete_customer, list_customer, add_product, delete_product, list_product, add_invoice, list_invoice
from project import startup, add_customer
import mock
import builtins
import re

global db
db, config = startup("test")


def test_add_customer():
    assert add_customer(db, 'Harvard CS50', 'Cambridge, MA, United States',
                        '+55 123 12123434') == "SUCCESS: Customer Harvard CS50 added"


def test_delete_customer():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert delete_customer(db) == 'SUCCESS: Customer id 1 removed'


def test_list_customer():
    assert list_customer(
        db) == "WARNING: There are no customer data. Please add a new"
    add_customer(db, 'Harvard CS50', 'Cambridge, MA, United States',
                 '+55 123 12123434') == "SUCCESS: Customer Harvard CS50 added"
    assert re.search(r'.*CS50.*Cambridge.*12123434.*', str(list_customer(db)))


def test_add_product():
    assert add_product(db, 'Development', 'Develop products using Python',
                       '1000') == "SUCCESS: Product Development added"


def test_delete_product():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert delete_product(db) == 'SUCCESS: Product id 1 removed'


def test_list_product():
    assert list_product(
        db) == "WARNING: There are no product data. Please add a new"
    add_customer(db,
                 'Harvard CS50', 'Cambridge, MA, United States', '+55 123 12123434') == "SUCCESS: Customer Harvard CS50 added"
    assert re.search(r'.*CS50.*Cambridge.*12123434.*', str(list_customer(db)))


def test_add_invoice():
    assert add_invoice(db, 'Test Customer', 'Test Product', '1000',
                       "Test Product Description", '10', '01/01/2022', '01/02/2022') == 1


def test_list_invoice():
    assert re.search(r'.*2022.*Test.*1000.*', str(list_invoice(db)))
