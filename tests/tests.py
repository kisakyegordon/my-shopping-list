import unittest


class OutcomesTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

    def test_signup(self):
        pass

    def test_login(self):
        pass

    def test_view_list(self):
        pass

    def test_create_list(self):
        pass


if  __name__ == '__main_':
    unittest.main()