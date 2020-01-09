from Tools.driver import Driver

class MainPage(Driver):

    def schedule_button(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/tab_title_label", text="日程")

    def message_button(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/tab_title_label", text="消息")

    def honor(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/iv_dialog_honor_badge")

    def click_schedule_button(self):
        try:
            while self.honor().exists:
                self.honor().click()
        except:
            pass
        self.schedule_button().click()