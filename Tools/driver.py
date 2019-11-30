import uiautomator2 as u2
import time
import init_app

class Driver(object):

    def __init__(self,driver=''):
        self.info=init_app.pakeage_name
        if driver != '':
            self.driver=driver
        else:
            self.driver=self.session_app()

    def connect_device(self):
        d=u2.connect()
        return d

    def session_app(self):
        # d.app_start(sfim) #启动APP
        # d.app_stop(sfim)   #停止app
        driver=self.connect_device().session(self.info)
        driver.implicitly_wait(10)
        return driver


