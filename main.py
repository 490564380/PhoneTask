# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sys
import time  # 引入time模块
import uiautomator2 as u2

from DouYin import DouYin
from WeiShi import WeiShi

while True:
    try:
        deviceIdXiaoMiNew = "e108593b"
        deviceIdXiaoMiOld = "88266af20604"
        connection = u2.connect(deviceIdXiaoMiNew)
        weishi = WeiShi(connection)
        douyin = DouYin(connection)


        time.sleep(1)
        ticks = time.time()
        localTime = time.localtime(ticks)
        print("当地时间:", localTime)
        tm_mday = localTime.tm_mday
        tm_hour = localTime.tm_hour
        tm_min = localTime.tm_min
        # 0是周一，6是周日
        tm_wday = localTime.tm_wday

        print("签到完成，做任务")
        if tm_hour >= 9 and tm_hour <= 16:  # 每天09:00-16:00开始刷视频。
            douyin.makeMoney()
            weishi.makeMoney()

        else:
            douyin.makeMoney()
            weishi.makeMoney()
            pass
    except:
        print("Unexpected error", sys.exc_info()[0])
