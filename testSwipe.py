import time

import uiautomator2 as u2
from uiautomator2 import Direction

# deviceIdXiaoMiOld = "88266af20604"
deviceIdXiaoMiOld = "e108593b"

weishiPackage = "com.tencent.weishi"

d = u2.connect(deviceIdXiaoMiOld)
d.app_stop("com.tencent.weishi")
d.app_start("com.tencent.weishi")
time.sleep(10)
d.click(0.785, 0.35)
time.sleep(10)
d.click(0.785, 0.35)
time.sleep(10)

# time.sleep(3)
# d(text="我知道了").click()

i = 0
while True:
    i = i + 1
    if i % 10 == 0:
        print("move FORWARD ", i)
        d.swipe_ext(Direction.BACKWARD)
        time.sleep(2)
    else:
        print("move BACKWARD ", i)
        d.swipe_ext(Direction.FORWARD)
        time.sleep(15 + i % 10)

    # if i % 30 == 0:
        # d.xpath(
        #     '//*[@resource-id="com.tencent.weishi:id/qsy"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]').click()
        # time.sleep(10)
        # signInExist = d(text="签到领现金").exists(timeout=10)
        # if signInExist:
        #     d(text="签到领现金").click()
        # else:
        #     print("签到领现金不存在")
    # d.swipe_ext(Direction.FORWARD)
    # d.swipe_ext(Direction.HORIZ_FORWARD) # 页面水平右翻
    # d.swipe_ext(Direction.HORIZ_BACKWARD) # 页面水平左翻
