# pylint: skip-file
import unittest
from unittest.mock import patch

from utility import (get_letter, get_user_email, get_user_name,
                     get_user_option, get_user_password, get_y_n_value,
                     hash_user_password, is_email_valid)


class TestUtility(unittest.TestCase):
    @patch("builtins.input", return_value=2)
    def test_get_user_option(self, mock_input):
        result = get_user_option()
        self.assertEqual(result, 2)

    @patch("builtins.input", return_value="Name")
    def test_get_user_name(self, mock_input):
        result = get_user_name()
        self.assertEqual(result, "Name")

    @patch("builtins.input", return_value="d@d.lt")
    def test_get_user_email(self, mock_input):
        result = get_user_email()
        self.assertEqual(result, "d@d.lt")

    @patch("builtins.input", return_value="password")
    def test_get_user_password(self, mock_input):
        result = get_user_password()
        self.assertEqual(result, "password")

    def test_hash_user_password(self):
        result = hash_user_password("password")
        self.assertEqual(result, "passwordwhysoserious?")

    def test_is_email_valid(self):
        result_one = is_email_valid("d@d.lt")
        result_two = is_email_valid("123")
        self.assertEqual(result_one, True)
        self.assertEqual(result_two, False)

    @patch("builtins.input", return_value="y")
    def test_get_y_value(self, mock_input):
        result = get_y_n_value()
        self.assertEqual(result, "y")

    @patch("builtins.input", return_value="n")
    def test_get_n_value(self, mock_input):
        result = get_y_n_value()
        self.assertEqual(result, "n")

    @patch("builtins.input", return_value="a")
    def test_get_letter_lower(self, mock_input):
        result = get_letter()
        self.assertEqual(result, "A")

    @patch("builtins.input", return_value="A")
    def test_get_letter_uper(self, mock_input):
        result = get_letter()
        self.assertEqual(result, "A")


if __name__ == "__main__":
    unittest.main()
