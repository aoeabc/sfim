from Tools.driver import Driver

class MainSchedulePage(Driver):

    def new_button(self):
        return self.driver.xpath('//*[@resource-id="com.pubinfo.sfim:id/tabs"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]')

    def new_meeting_button(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/iv_pop_meeting")

    def guide(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/iv_pop_guide")

    def new_meeting_click(self):
        try:
            self.guide().click()
        except:
            pass

        self.new_button().click()
        self.new_meeting_button().click()