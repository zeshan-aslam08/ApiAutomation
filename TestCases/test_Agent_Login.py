import requests

from Methods.LoginAgent import loginPage
# This is First Test Case

class TestLogin(loginPage):
    def test_login_with_valid_cridentials(self, flag=None):
        flag = self.login_with_valid_cridentials()
        assert flag is True
