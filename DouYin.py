import time
import uiautomator2 as u2
from uiautomator2 import Direction


class DouYin:

    def __init__(self, connection):
        self.connection = connection
        self.package = "com.ss.android.ugc.aweme.lite"

    def tixian(self):
        pass

    # 刷视频做任务赚钱
    def makeMoney(self):
        d = self.connection
        print(self.package, "重启应用")
        d.app_stop(self.package)
        d.app_start(self.package)

        self.handleStartUpDialog()

        self.doJob()
        playing = True
        timeStart = time.time()
        duration = 0
        i = 0
        while playing:
            self.handleStartUpDialog()
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
                time.sleep(i % 5)
        print(self.package, "total duration = %s" % duration)
        time.sleep(3)

        self.doJob()
        d.app_stop(self.package)

    # 处理启动各种弹窗
    def handleStartUpDialog(self):
        d = self.connection
        print(self.package, "****** handleStartUpDialog ******")

        dialogExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/bai").exists(timeout=5)
        if dialogExist:
            print(self.package, "邀请好友弹窗处理")
            d(resourceId="com.ss.android.ugc.aweme.lite:id/bai").click()

        dialogExist = d(text="暂时不要").exists(timeout=5)
        if dialogExist:
            print(self.package, " 通讯录弹窗判断处理")
            d(text="暂时不要").click()

        dialogExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/dat").exists(timeout=5)
        if dialogExist:
            print(self.package, "朋友推荐弹窗处理")
            d.click(0.857, 0.223)

        dialogExist = d(text="进入儿童/青少年模式").exists(timeout=5)
        if dialogExist:
            print(self.package, "进入儿童/青少年模式弹窗处理")
            d.click(0.489, 0.684)

        dialogExist = d(resourceId="com.ss.android.ugc.aweme.lite:id/bfw").exists(timeout=5)
        if dialogExist:
            print(self.package, "升级弹窗处理")
            d(resourceId="com.ss.android.ugc.aweme.lite:id/bfw").click()

    # 处理启动各种弹窗
    def handleJobDialog(self):
        d = self.connection
        time.sleep(10)
        print(self.package, "****** handleJobDialog ******")

        dialogExist = d(text="今日签到").exists(timeout=5)
        if dialogExist:
            print(self.package, "点击今日签到")
            d.click(0.459, 0.625)

        dialogExist = d(text="检测到更新").exists(timeout=5)
        if dialogExist:
            print(self.package, "点击不更新")
            d.click(0.295, 0.635)

        dialogExist = d(text="签到提醒").exists(timeout=5)
        if dialogExist:
            print(self.package, "点击签到")
            d.click(0.51, 0.63)
            time.sleep(60)
            d.click(0.92, 0.04)

    # 做进入任务页赚钱
    def doJob(self):
        d = self.connection
        print(self.package, "做任务赚钱")
        d.click(0.083, 0.18)
        time.sleep(5)
        self.handleJobDialog()

        btnExist = d(text="去领取").exists(timeout=5)
        if btnExist:
            print(self.package, "点击去领取")
            d(text="去领取").click()
            time.sleep(60)
            print(self.package, "点击关闭广告")
            d.click(0.92, 0.04)

            dialogExist = d(description="坚持退出").exists(timeout=5)
            if dialogExist:
                print(self.package, "点击继续看广告")
                d.click(0.496, 0.569)
                time.sleep(60)
                print(self.package, "点击关闭广告")
                d.click(0.92, 0.04)
            time.sleep(5)

        btnExist = d(text="开宝箱得金币").exists(timeout=5)
        if btnExist:
            print(self.package, "开宝箱得金币")
            d(text="开宝箱得金币").click()
            time.sleep(3)

            btnExist = d(text="看广告视频再赚").exists(timeout=5)
            if btnExist:
                print(self.package, "点击看广告视频再赚")
                d(text="看广告视频再赚").click()
                time.sleep(50)
                print(self.package, "点击关闭广告")
                d.click(0.92, 0.04)

            dialogExist = d(description="坚持退出").exists(timeout=5)
            if dialogExist:
                print(self.package, "点击继续看广告")
                d.click(0.496, 0.569)
                time.sleep(60)
                print(self.package, "点击关闭广告")
                d.click(0.92, 0.04)

        print(self.package, "点击返回按钮")
        d.press("back")

    # 提现
    def withDrawal(self):
        print(self.package, "withDrawal")
