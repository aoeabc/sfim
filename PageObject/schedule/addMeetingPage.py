from Tools.driver import Driver

class AddMeetingPage(Driver):
    def meeting_name_input(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/meeting_name")

    def meeting_type_select(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/meeting_type_text")

    def add_meeting_button(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/tv_meeting_create")

    def save_meeting_button(self):
        return self.driver(resourceId="com.pubinfo.sfim:id/ll_save_draft")

    def create_meeting(self):
        self.meeting_name_input().send_keys("测试会议")
        self.meeting_type_select().click()
        # self.add_meeting_button().click()