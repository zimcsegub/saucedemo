import pytest
from pages.login_page import LoginPage
from testcases.base_test import BaseTest


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_testcase(self):
        self.login_page = LoginPage(self.driver)
    @pytest.mark.parametrize()
    # def test_blank_username(self):
    #     self.login_page.perform_login("", "secret_sauce")
    #     username_error_msg = self.login_page.get_error_msg()
    #     assert username_error_msg == "Epic sadface: Username is required"
    @pytest.mark.parametrize("username, password, error",[
        ("standard_user", "", "Epic sadface: Password is required"),
        ("Lucifer", "Morningstar","Epic sadface: Username and password do not match any user in this service")
    ]
    )
    def test_invalid_login(self, username, password, error):
        self.login_page.perform_login(username, password)
        password_error_msg = self.login_page.get_error_msg()
        assert password_error_msg == error

    @pytest.mark.parametrize("username, password, msg", [
        ("standard_user","secret_sauce", "Open Menu")
    ])
    def test_login_with_valid_username_and_password(self, username, password, msg):
        self.login_page.perform_login(username, password)
        check_login = self.login_page.check_login_successfully_or_not()
        assert check_login == msg

