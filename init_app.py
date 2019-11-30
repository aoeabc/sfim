#   1、启动 D:\Program Files (x86)\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe
#   2、adb connect 127.0.0.1:7555---这个步骤不能省，不然发现不了设备
#   3、adb devices
#   4、python3 -m uiautomator2 init  安装包含httprpc服务的apk到手机+atx-agent, minicap, minitouch
#   5、webedit python -m weditor---Chrome
pakeage_name='com.pubinfo.sfim'