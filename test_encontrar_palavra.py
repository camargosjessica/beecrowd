from unittest import TestCase

from encontrar_palavra import a_contains_b


class Test(TestCase):
    def test_happy_path(self):
        self.assertTrue(a_contains_b('casamento', 'casamento'))
        self.assertTrue(a_contains_b('casamento', 'menta'))
        self.assertTrue(a_contains_b('casamento', 'mesa'))

    def test_different_char(self):
        self.assertFalse(a_contains_b('casamento', 'abobora'))
        self.assertFalse(a_contains_b('vassoura', 'abobora'))

    def test_different_char_size(self):
        self.assertFalse(a_contains_b('menta', 'casamento'))
        self.assertFalse(a_contains_b('mesa', 'mesas'))
        self.assertFalse(a_contains_b('mesa', 'mel'))

    def test_empty_char(self):
        with self.assertRaises(AttributeError):
            a_contains_b('casamento', '')
        with self.assertRaises(AttributeError):
            a_contains_b('', 'casamento')
        with self.assertRaises(AttributeError):
            a_contains_b('', '')

    def test_none_char(self):
        with self.assertRaises(AttributeError):
            a_contains_b('casamento', None)
        with self.assertRaises(AttributeError):
            a_contains_b(None, 'casamento')
        with self.assertRaises(AttributeError):
            a_contains_b(None, None)

