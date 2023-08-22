import requests

from Methods.LoginAgent import loginPage


class TestLogin(loginPage):
    def test_login_with_valid_cridentials(self, flag=None):
        flag = self.login_with_valid_cridentials()
        assert flag is True
