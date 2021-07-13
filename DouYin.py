import time
import uiautomator2 as u2
from uiautomator2 import Direction


class DouYin:

    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.package = "com.ss.android.ugc.aweme.lite"

    # 签到
    def signIn(self):
        d = u2.connect(self.deviceId)
        d.app_stop(self.package)
        d.app_start(self.package)
        time.sleep(10)

        self.handleStartUpDialog(d)
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
        time.sleep(5)
        signSuccess = True
        while signSuccess is False:
            isJobCenter = d.xpath('//*[@resource-id="com.ss.android.ugc.aweme.lite:id/a8g"]').exists()
            if isJobCenter != -1:
                d.click(0.481, 0.725)  # 点击 "签到"按钮
                time.sleep(3)
                signSuccess = True
            else:
                d.click(0.51, 0.709)  # 点击"我知道了"
                time.sleep(2)
                d.click(0.788, 0.065)  # 点击领奖圆圈
                time.sleep(2)
        d.app_stop(self.package)
        return signSuccess

    def tixian(self):
        pass

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
        time.sleep(3)

        self.doJob(d)
        d.app_stop(self.package)

    # 处理启动各种弹窗
    def handleStartUpDialog(self, d):
        print(self.package, "****** handleStartUpDialog ******")

        print(self.package, "邀请好友弹窗处理")
        byeExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/bai").exists(timeout=5)
        if byeExist:
            d(resourceId="com.ss.android.ugc.aweme.lite:id/bai").click()

        print(self.package, " 通讯录弹窗判断处理")
        noNeedExist = d(text="暂时不要").exists(timeout=5)
        if noNeedExist:
            d(text="暂时不要").click()

        print(self.package, "朋友推荐弹窗处理")
        friendExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/dat").exists(timeout=5)
        if friendExist:
            d.click(0.857, 0.223)

        print(self.package, "进入儿童/青少年模式弹窗处理")
        childModeExist = d(text="进入儿童/青少年模式").exists(timeout=5)
        if childModeExist:
            d.click(0.489, 0.684)

    # 处理启动各种弹窗
    def handleJobDialog(self, d):
        print(self.package, "****** handleJobDialog ******")

        print(self.package, "今日签到")
        signInExist = d(text="今日签到").exists(timeout=5)
        if signInExist:
            d.click(0.459, 0.625)

        dialogExist = d(text="签到提醒").exists(timeout=5)
        if dialogExist:
            d.click(0.51, 0.63)
            time.sleep(60)
            d.click(0.92, 0.04)

        dialogExist = d(description="坚持退出").exists(timeout=5)
        if dialogExist:
            d.click(0.496, 0.569)
            time.sleep(60)
            d.click(0.92, 0.04)

    # 做进入任务页赚钱
    def doJob(self, d):
        print(self.package, "做任务赚钱")
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
        time.sleep(5)
        self.handleJobDialog(d)
        print(self.package, "看广告赚金币")
        btnExist = d(text="看广告赚金币").exists(timeout=5)
        if btnExist:
            d.click(0.8, 0.5)
            time.sleep(60)
            d.click(0.92, 0.04)
            self.handleJobDialog(d)

    # 提现
    def withDrawal(self):
        print(self.package, "withDrawal")
