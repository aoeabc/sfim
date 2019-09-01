import uiautomator2 as u2
import time
d=u2.connect()
sfim='com.pubinfo.sfim'
# d.app_start(sfim) #启动APP
# d.app_stop(sfim)   #停止app
driver=d.session(sfim)
time.sleep(3)
driver(resourceId="com.pubinfo.sfim:id/editUserid").send_keys('80004202')
time.sleep(3)
driver(resourceId="com.pubinfo.sfim:id/editPassword").send_keys(',Xiaochen622')
time.sleep(3)
driver(resourceId="com.pubinfo.sfim:id/login_bt").click()