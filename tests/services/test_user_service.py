import unittest
from unittest.mock import MagicMock, Mock

from flask import Flask

from web.app.services.web_services import user_services as services


class MockDb:
    def __init__(self):
        pass

    def connect(self):
        pass

    def cursor(self):
        pass


class TestCase(unittest.TestCase):
    @unittest.mock.patch("mysql.connector.connect", MagicMock())
    def setUp(self):
        app = Flask(__name__)
        app.config["FLASK_ENV"] = "development"
        with app.app_context():
            self.user_service = services.UserService()

    def test_check_exists(self):
        cursor = MagicMock()
        cursor.__iter__ = Mock(return_value=iter(["user"]))
        self.user_service.connection.cursor.return_value = cursor

        username_test = "user1"
        right_query = f'SELECT * FROM user WHERE username="{username_test}"'

        self.assertTrue(self.user_service.check_exist(username_test))
        cursor.execute.assert_called_once()
        cursor.execute.assert_called_with(right_query)

    def test_check_exists_failed(self):
        cursor = MagicMock()
        cursor.__len__ = 0
        self.user_service.connection.cursor.return_value = cursor

        username_test = "user1"
        right_query = f'SELECT * FROM user WHERE username="{username_test}"'

        cursor.return_value = []
        cursor.execute.side_effect = None

        self.assertFalse(self.user_service.check_exist(username_test))
        cursor.execute.assert_called_once()
        cursor.execute.assert_called_with(right_query)

    def test_check_login(self):
        cursor = MagicMock()
        cursor.__iter__ = Mock(return_value=iter(["user"]))

        self.user_service.connection.cursor.return_value = cursor

        username_test = "user1"
        psw_test = "password"
        right_query = f"SELECT * FROM user WHERE username='{username_test}' and password='{psw_test}'"

        self.assertTrue(
            self.user_service.check_credentials(username_test, psw_test, id=False)
        )
        cursor.execute.assert_called_once()
        cursor.execute.assert_called_with(right_query)

    def test_check_login_failed(self):
        cursor = MagicMock()
        cursor.__len__ = 0

        self.user_service.connection.cursor.return_value = cursor

        username_test = "user1"
        psw_test = "password"

        right_query = f"SELECT * FROM user WHERE username='{username_test}' and password='{psw_test}'"

        cursor.return_value = []
        cursor.execute.side_effect = None

        self.assertFalse(
            self.user_service.check_credentials(username_test, psw_test, id=False)
        )
        cursor.execute.assert_called_once()
        cursor.execute.assert_called_with(right_query)

    def test_signup(self):
        cursor = MagicMock()
        self.user_service.connection.cursor.return_value = cursor

        username_test = "user1"
        psw_test = "password"
        right_query = f'INSERT INTO user (username, password) VALUES ("{username_test}", "{psw_test}")'

        self.assertTrue(self.user_service.signup(username_test, psw_test))
        self.assertEqual(cursor.execute.call_count, 2)
        self.user_service.connection.commit.assert_called_once()
        cursor.execute.assert_called_with(right_query)


if __name__ == "__main__":
    unittest.main()
