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
        d.app_start(self.package)
        time.sleep(15)
        # 邀请好友弹窗判断
        byeExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/bai").exists(timeout=5)
        if byeExist:
            d(resourceId="com.ss.android.ugc.aweme.lite:id/bai").click()
        # 通讯录弹窗判断
        noNeedExist = d(text="暂时不要").exists(timeout=5)
        if noNeedExist:
            d(text="暂时不要").click()

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
        d.app_stop(self.package)

    # 处理启动各种弹窗
    def handleStartUpDialog(self, d):
        print(self.package, "升级窗口判断")
        updateExist = d(resourceId="com.tencent.weishi:id/ov").exists(timeout=5)
        if updateExist:
            d.click(0.784, 0.353)  # 关闭页面

        print(self.package, "朋友推荐弹窗")
        friendExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/dat").exists(timeout=5)
        if friendExist:
            d.click(0.857, 0.223)
