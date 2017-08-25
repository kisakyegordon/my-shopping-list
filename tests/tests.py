import unittest
from app.user import User


class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_delete_shopping_list(self):
        self.user.shopping_lists = {'tuesday': ['food', 'fuel'], 'wednesday': ['clothes', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list(
            'tuesday'), {'wednesday': ['clothes', 'tomatoes']})

    def test_shopping_list_initialy_empty(self):
        self.assertEqual(self.user.shopping_lists, {})

    def test_create_shopping_list_successfully(self):
        initial_list_count = len(self.user.shopping_lists)
        tuesday_list = self.user.create_shopping_list('Tuesday')
        self.assertTrue(tuesday_list)
        new_list_count = len(self.user.shopping_lists)
        self.assertEqual(new_list_count - initial_list_count, 1)

    def test_updating_non_existing_shopping_list_item(self):
        self.user.shopping_lists = {'tuesday_list': ['food']}
        self.assertEqual(self.user.update_shopping_list_item('tuesday_list', 'flas', 'flat'),
                         'Item not in list', msg='Item not in list')

    def test_create_shopping_list_when_list_already_exists(self):
        self.user.shopping_lists = {'tuesday': ['food']}
        self.assertEqual(self.user.create_shopping_list('tuesday', 'food'),
                         'Shopping List already exists!', msg='Shopping List already exists!')

    def test_update_shopping_list(self):
        self.user.shopping_lists = {'tuesday': ['food']}
        self.assertEqual(self.user.update_shopping_list(
            'tuesday', 'tuesday_list'), {'tuesday_list': ['food']})

    def test_updating_non_existing_shopping_list(self):
        self.user.shopping_lists = {'Tuesday': ['food']}
        self.assertEqual(self.user.update_shopping_list('Shoe', 'flats'),
                         'list name does not exist here', msg='list name does not exist here')

    def test_update_shopping_list_item(self):
        self.user.shopping_lists = {'food': ['apple']}
        self.assertEqual(self.user.update_shopping_list_item(
            'food', 'apple', 'apple'), {'food': ['apple']})


    def test_read_shopping_list_items(self):
        self.user.shopping_lists = {'food': ['onions', 'apples']}
        self.assertEqual(self.user.read_list('food'), ['onions', 'apples'])


