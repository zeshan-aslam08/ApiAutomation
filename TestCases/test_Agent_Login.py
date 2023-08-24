

from Methods.LoginAgent import LoginPage


class TestLogin(LoginPage):
    def test_login_with_valid_credentials(self):
        """
         Login With Valid credentials Test Case
        """
        flag = self.login_with_valid_credentials()
        assert flag is True

    def test_login_with_invalid_credentials(self):
        """
         Login With in-Valid credentials Test Case
        """
        flag = self.login_with_invalid_credentials()
        assert flag is True

    def test_login_with_invalid_Name(self):
        """
         Login With in-Valid credentials Test Case
        """
        flag = self.login_with_invalid_Name()
        assert flag is True
