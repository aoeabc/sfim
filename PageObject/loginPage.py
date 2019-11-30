from Tools.driver import Driver


class LoginPage(Driver):

    def username_input(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/editUserid")

    def password_input(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/editPassword")

    def submit_button(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/login_bt")

    def login_action(self):
        try:
            self.username_input().send_keys('80004202')
            self.password_input().send_keys('..Xiaochen622')
            self.submit_button().click()
        except:
            pass



if __name__ == '__main__':
    l=LoginPage()
    l.login_action()
