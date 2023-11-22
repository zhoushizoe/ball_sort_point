import subprocess

from airtest.cli.parser import cli_setup
from airtest.core.api import *
from page.gameplay_guide_page import GamePlayGuide
from page.privacy_page import PrivacyPage
from base.base import BaseElement
from page.game_page import GamePage
from page.home_page import HomePage
from page.shop_page import ShopPage
from base.base_point import GetPoint

# def connect_adb(device_ip, port=5037):
#     command = f"adb connect {device_ip}:{port}"
#     subprocess.run(command, shell=True)
#
# # 调用函数连接ADB
# connect_adb("10.10.1.246")




class TestPoint(BaseElement, GetPoint):
    auto_setup(__file__, logdir=True,
               devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&"])

    # def setup(self):
    #     auto_setup(__file__, logdir=True,
    #                devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    def test1_first_open(self):
        """
        首次打开游戏
        测试埋点为：app_first_open
        :return:
        """
        point = "app_first_open"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.PrivacyPage.first_open_android()
        self.contrast_step(point)

    def test2_privacy_pv(self):
        """
        隐私弹窗展示	启动页结束后，隐私弹窗页面展示
        :return:
        """

        command = f"adb connect 10.10.1.246:5555"
        subprocess.run(command, shell=True)

        # 调用函数连接ADB
        point = "privacy_pv"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.PrivacyPage.first_open_android()
        self.contrast_step(point)

    def test3_terms_of_service_click(self):
        point = "terms_of_service_click"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.image_click([774, 1361])
        self.contrast_step(point)
