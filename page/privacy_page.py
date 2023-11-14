# coding = utf-8
# Author: Zoe
# File: privacy_page.py
# Time: 2023/10/25 2:55 下午
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from base.base import BaseElement
from page.gameplay_guide_page import GamePlayGuide
from base.base_app import SortBallApp


class PrivacyPage(BaseElement, SortBallApp):
    ballsort_package = "game.ballsort.inner"
    ballsort_ios_package = "ios.game.ballsort.inner"
    package_name = "BallSort"

    ballsort_ios_install = r"/Users/amber/Downloads/BallSort_IOS_1040_1.ipa"
    system_notifications_button = Template(r"../picture/privacy_page/system_notifications_button.png",
                                           record_pos=(0.001, 0.447), resolution=(1440, 3088))
    accept_button = Template(r"../picture/privacy_page/accept_button.png", target_pos=6, record_pos=(-0.256, 0.194),
                             resolution=(1440, 3088))

    language = "英语_13pro_max"
    name = rf"{language}/{language}"
    word = "解锁"

    #
    def file_path(self, folder_name):
        path = f"/Users/mac/PycharmProjects/Sortball/page/log/{folder_name}"
        if os.path.exists(path):
            return
        else:
            os.makedirs(path)
        return self

    def first_open(self):
        """
        首次打开游戏，进入隐私弹窗页面
        :return:
        """
        # 卸载iOS包
        self.uninstall_ios(self.ballsort_ios_package)
        self.sleep_time()
        # 安装iOS包
        self.install_ios(self.ballsort_ios_install)
        # 首次打开iOS包
        self.ios_open_app(self.package_name)
        self.sleep_time()
        self.image_click([644, 1739])
        self.sleep_time()
        self.image_click([640, 1570])
        self.sleep_time()
        self.image_click([644, 1570])
        return self

    def first_open_android(self):
        """
        首次打开游戏安卓
        :return:
        """
        self.clear_app(self.ballsort_package)
        self.sleep_time()
        self.start_app(self.ballsort_package)
        self.sleep_time(4)
        self.image_click([712, 2482])
        self.sleep_time(4)
        return self

    def click_accept(self):
        """
        在隐私弹窗页面点击接受按钮
        :return:新手引导页面
        """
        if exists(self.accept_button):
            self.image_click(self.accept_button)
        else:
            self.image_click([629, 1393])
        self.sleep_time(4)
        return GamePlayGuide


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    PrivacyPage().first_open()
