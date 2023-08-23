import requests

from Methods.LoginAgent import LoginPage
from Logs import loggers


class TestLogin(LoginPage):
    logs = loggers.log_fun()

    def test_login_with_valid_credential(self, flag=None):
        flag = self.login_with_valid_credentials()
        assert flag is False

    def test_login_with_invalid_credential(self, flag=None):
        flag = self.login_with_invalid_credentials()
        assert flag is False
    #
    def test_login_with_invalid_Name(self, flag=None):
        flag = self.login_with_invalid_Name()
        assert flag is False

    # def test_login_with_invalid_Name_valid_password(self, flag=None):
    #     flag = self.login_with_valid_cridentials()
    #     assert flag is True
