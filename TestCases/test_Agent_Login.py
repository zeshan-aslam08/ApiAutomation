import requests

from Methods.LoginAgent import LoginPage


class TestLogin(LoginPage):
    def test_login_with_valid_credentials(self):
        flag = self.login_with_valid_credentials()
        assert flag is True
