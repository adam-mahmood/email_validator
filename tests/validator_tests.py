from validators import EmailValidator as ev
from unittest import TestCase


class EmailValidatorTestCase(TestCase):
    def setUp(self):
        self.validator = ev()

    def test_no_at(self):
        self.assertFalse(self.validator.validate("notanemail"))

    def test_simplest_email(self):
        self.assertTrue(self.validator.validate("simple@example.com"))

    def test_dotted_email(self):
        self.assertTrue(self.validator.validate("simple.dotted@example.com"))

    def test_dotted_end_local_email(self):
        self.assertFalse(self.validator.validate("simple.@example.com"))

    def test_multi_dotted_email(self):
        self.assertFalse(self.validator.validate("simple..wrong@exonar.com"))

    def test_multi_part_email(self):
        self.assertTrue(self.validator.validate("simple.right.dotted@exonar.com"))

    def test_multi_subsdomain(self):
        self.assertTrue(self.validator.validate("simple.right.dotted@@ubnet.exonar.com"))
