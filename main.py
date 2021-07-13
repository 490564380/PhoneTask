# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import time  # 引入time模块

from DouYin import DouYin
from WeiShi import WeiShi

# deviceIdXiaoMiOld = "88266af20604"
deviceIdXiaoMiNew = "e108593b"
weishi = WeiShi(deviceIdXiaoMiNew)
douyin = DouYin(deviceIdXiaoMiNew)
while True:
    time.sleep(1)
    ticks = time.time()
    localTime = time.localtime(ticks)
    print("当地时间:", localTime)
    tm_mday = localTime.tm_mday
    tm_hour = localTime.tm_hour
    tm_min = localTime.tm_min
    # 0是周一，6是周日
    tm_wday = localTime.tm_wday


    if tm_hour == 7:  # 每天09:00-16:00开始刷视频。
        print("各软件签到")
        weishiSignSuccess = weishi.signIn()  # 微视签到
        # douyinSignSuccess = douyin.signIn()#做任务的时候可以顺带完成签到



        print("各软件提现")
        weishiSignSuccess = weishi.withDrawal()  # 微视签到
        douyin.withDrawl()


    print("签到完成，做任务")
    if tm_hour >= 9 and tm_hour <= 16:  # 每天09:00-16:00开始刷视频。
        weishi.makeMoney()
        douyin.makeMoney()
    else:
        douyin.makeMoney()
        weishi.makeMoney()
        pass
