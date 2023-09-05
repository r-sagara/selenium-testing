from pytest import mark

pytestmark = mark.login

@mark.positive
class TestPositiveCases:
    def test_login_page(self, LoginPage, AccountPage):
        username = "test"
        password = "TEST"

        LoginPage.open()
        LoginPage.do_login(username, password)
        AccountPage.verify_login(username)


@mark.negative
class TestNegativeCases:
    @mark.parametrize("username, password, expected_error_message",
                      [("wrong_test", "TEST", "is not registered on this site"),
                      ("test", "WRONG_TEST", "password.*is incorrect")],
                      ids=['wrong-user', 'wrong-pass'])
    def test_login_page(self, LoginPage, username, password, expected_error_message):
        LoginPage.open()
        LoginPage.do_login(username, password)
        LoginPage.verify_error_message(expected_error_message)