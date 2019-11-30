import unittest
from PageObject.loginPage import LoginPage
from PageObject.mainPage import MainPage
from PageObject.schedule.mainSchedulePage import MainSchedulePage

class Cases(unittest.TestCase):

    def setUp(self) -> None:
        self.driver=LoginPage()
        self.driver.login_action()
        self.mainPage=MainPage(self.driver.driver)
        self.mainSchPage=MainSchedulePage(self.driver.driver)

    def test_nomarl_meeting(self):
        self.mainPage.click_schedule_button()
        self.mainSchPage.new_meeting_click()


if __name__ == '__main__':
    unittest.main()