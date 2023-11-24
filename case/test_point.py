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
    # auto_setup(__file__, logdir=True,
    #            devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&"])

    def setup_class(self):
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

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
        point = "privacy_pv"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.PrivacyPage.first_open_android()
        self.contrast_step(point)

    def test3_terms_of_service_click(self):
        """
        点击进入服务条款h5页面
        测试埋点为：terms_of_service_click
        :return:
        """
        point = "terms_of_service_click"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.PrivacyPage.click_terms_of_service()
        self.contrast_step(point)

    def test4_privacy_policy_click(self):
        """
        点击进入服务条款h5页面
        测试埋点为：privacy_policy_click
        :return:
        """
        point = "privacy_policy_click"
        self.PrivacyPage = PrivacyPage()
        self.PrivacyPage.click_policy_close()
        self.clear_command()
        self.PrivacyPage.click_privacy_policy()
        # self.contrast_step(point)

    def test5_privacy_click(self):
        """
        隐私弹窗页面点击同意
        :return:
        """
        point = "privacy_click"
        self.PrivacyPage = PrivacyPage()
        self.PrivacyPage.click_policy_close()
        self.clear_command()
        self.PrivacyPage.click_accept()
        self.contrast_step(point)

    def test6_app_open(self):
        """
        杀掉进程，非首次进入游戏：app_open
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "app_open"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.stop_app(ballsort_package)
        self.sleep_time()
        self.start_app(ballsort_package)
        self.contrast_step(point)

    def test7_app_open(self):
        """
        从后台回到前台，app_open
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "app_open"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.keyevent_command("HOME")
        self.sleep_time()
        self.start_app(ballsort_package)
        self.contrast_step(point)

    # def test8_app_quit(self):
    #     """
    #     杀掉进程，退出游戏：app_quit
    #     :return:
    #     """
    #     ballsort_package = "game.ballsort.inner"
    #     point = "app_quit"
    #     self.PrivacyPage = PrivacyPage()
    #     self.clear_command()
    #     self.kill_app()
    #     self.contrast_step(point)

    def test9_app_quit(self):
        """
        返回后台，非退出游戏：app_quit
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "app_quit"
        self.PrivacyPage = PrivacyPage()
        self.clear_command()
        self.keyevent_command("HOME")
        self.contrast_step(point)

    # def test10_app_kill(self):
    #     """
    #     杀游戏进程
    #     :return:
    #     """
    #     ballsort_package = "game.ballsort.inner"
    #     point = "app_kill"
    #     self.PrivacyPage = PrivacyPage()
    #     self.clear_command()
    #     self.stop_app(ballsort_package)
    #     self.contrast_step(point)

    def test11_app_init(self):
        ballsort_package = "game.ballsort.inner"
        point = "app_init"
        self.PrivacyPage = PrivacyPage()
        self.stop_app(ballsort_package)
        self.clear_command()
        self.start_app(ballsort_package)
        self.contrast_step(point)

    def test12_game_new_start(self):
        """
        第二关开局
        game_new_start：activity_id：0，activity_name：classic
        :return:
        """
        point = "game_new_start"
        self.HomePage = HomePage()
        self.GamePage = GamePage()
        self.HomePage.home_goto_game()
        self.GamePage.get_debug().get_debug().debug_win()
        self.clear_command()
        self.GamePage.game_victory()
        self.contrast_step(point)

    def test13_game_new_start_scene(self):
        """
        game_new_start埋点，scene：item
        :return:
        """
        point = "game_new_start"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.click_restart()
        self.contrast_step(point)

    def test14_game_new_start_scene(self):
        """
        game_new_start埋点，scene：initialization
        :return:
        """
        point = "game_new_start"
        ballsort_package = "game.ballsort.inner"
        self.PrivacyPage = PrivacyPage()
        self.HomePage = HomePage()
        # 前置条件
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(5)
        # 清除数据
        self.clear_command()
        # 操作步骤
        self.HomePage.home_goto_game()
        # 得到埋点
        self.contrast_step(point)

    def test15_game_new_start_activity_name(self):
        """
        game_new_start中的acticity_start
        activity_name：special
        1.打开debug
        2.点击胜利至特殊关卡
        3.进入特殊关卡
        :return:
        """
        point = "game_new_start"
        self.GamePage = GamePage()
        (self.GamePage.get_debug().get_debug().debug_win().game_victory().debug_win().
         game_victory().debug_win().setting_close().game_victory().debug_win().game_victory())
        self.clear_command()
        self.GamePage.special_play()
        self.contrast_step(point)

    def test16_game_continue(self):
        """
        继续游玩	应用从后台到前台进入关卡继续残局游玩时上报
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "game_continue"
        self.GamePage = GamePage()
        # 操作两个步骤
        self.GamePage.get_debug()
        self.image_click([113, 1450]).image_click([1061, 1474]).image_click([619, 1332]).image_click([1312, 934])
        # 点击重开一次
        self.GamePage.click_restart()
        self.clear_command()
        self.keyevent_command("HOME")
        self.start_app(ballsort_package)
        self.contrast_step(point)





