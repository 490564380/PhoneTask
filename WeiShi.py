import time
import uiautomator2 as u2
from uiautomator2 import Direction


class WeiShi:

    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.package = "com.tencent.weishi"

    # 签到
    def signIn(self):
        print(self.package, "***signIn签到***")
        d = u2.connect(self.deviceId)

        print(self.package, "重启")
        d.app_stop(self.package)
        d.app_start(self.package)
        time.sleep(15)

        self.handleStartUpDialog(d)

        d.click(0.788, 0.065)  # 点击领奖圆圈,进入"任务中心"
        time.sleep(5)
        signSuccess = False
        while signSuccess is False:
            pageInfo = d.app_current()
            isJobCenter = pageInfo["activity"].find("WebviewBaseActivity")  # 判断进入"任务中心"
            if isJobCenter != -1:
                d.click(0.481, 0.725)  # 点击 "签到"按钮
                time.sleep(2)
                signSuccess = True
            else:
                d.click(0.51, 0.709)  # 点击"我知道了"
                time.sleep(2)
                d.click(0.788, 0.065)  # 点击领奖圆圈
                time.sleep(2)
        d.app_stop(self.package)
        return signSuccess

    # 提现
    def withDrawal(self):
        print(self.package, "***withDrawal提现***")
        d = u2.connect(self.deviceId)

        print(self.package, "重启")
        d.app_stop(self.package)
        d.app_start(self.package)
        time.sleep(15)

        self.handleStartUpDialog(d)

        d.click(0.788, 0.065)  # 点击领奖圆圈,进入"任务中心"
        time.sleep(5)
        withDrawalSuccess = False
        while withDrawalSuccess is False:
            pageInfo = d.app_current()
            isJobCenter = pageInfo["activity"].find("WebviewBaseActivity")  # 判断进入"任务中心"
            if isJobCenter != -1:
                d.click(0.408, 0.149)  # 点击 "提现"按钮
                time.sleep(4)
                d.click(0.781, 0.244)  # 点击"立即提现"按钮
                time.sleep(4)
                d.click(0.916, 0.134)  # 广告页面，点击空白位置，弹框消失
                time.sleep(1)
                d.click(0.777, 0.467)  # 广告页面，点击"确认提现。
                time.sleep(4)
                withDrawalSuccess = True
            else:
                d.click(0.51, 0.709)  # 点击"我知道了"
                time.sleep(2)
                d.click(0.788, 0.065)  # 点击领奖圆圈
                time.sleep(2)
        d.app_stop(self.package)
        return withDrawalSuccess


    # 刷视频做任务赚钱
    def makeMoney(self):
        d = u2.connect(self.deviceId)

        print(self.package, "重启应用")
        d.app_stop(self.package)
        d.app_start(self.package)
        self.handleStartUpDialog(d)

        playing = True
        timeStart = time.time()
        duration = 0
        i = 0
        while playing:
            duration = time.time() - timeStart
            playing = duration < 20 * 60

            i = i + 1
            if i % 10 == 0:
                print(self.package, "move FORWARD %s" % i)
                d.swipe_ext(Direction.BACKWARD)
                time.sleep(2)
                d.swipe_ext(Direction.FORWARD)
                time.sleep(2)
            else:
                print(self.package, "move BACKWARD %s" % i)
                d.swipe_ext(Direction.FORWARD)
                time.sleep(15 + i % 10)
        print(self.package, "total duration = %s" % duration)
        d.click(0.788, 0.065)  # 点击领奖圆圈
        time.sleep(3)
        d.app_stop(self.package)

    # 处理启动各种弹窗
    def handleStartUpDialog(self, d):
        print(self.package, "升级窗口判断")
        updateExist = d(resourceId="com.tencent.weishi:id/ov").exists(timeout=5)
        if updateExist:
            d.click(0.784, 0.353)  # 关闭页面
