import subprocess

import pytest
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

    def goto_level2(self):
        self.PrivacyPage = PrivacyPage()
        self.PrivacyPage.first_open_android().click_accept()
        self.sleep_time()
        self.GamePage = GamePage()
        self.GamePage.get_debug().get_debug()
        self.GamePage.debug_win()
        self.sleep_time(4)
        self.GamePage.game_victory().get_debug()
        return self

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
        self.contrast_step(point)

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
    #     self.stop_app(ballsort_package)
    #     self.start_app(ballsort_package)
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
        # self.HomePage.home_goto_game()
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
         game_victory().debug_win().setting_close().game_victory().debug_win().ad_close().game_victory())
        self.clear_command()
        self.GamePage.special_play()
        self.contrast_step(point)

    def test16_game_continue_restart(self):
        """
        继续游玩	应用从后台到前台进入关卡继续残局游玩时上报
        特殊关、重开一次、一个步骤
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "game_continue"
        self.GamePage = GamePage()
        # 操作两个步骤
        self.GamePage.get_debug()
        # 点击重开一次
        self.GamePage.click_restart()
        self.sleep_time()
        self.image_click([113, 1450]).image_click([1061, 1474]).image_click([619, 1332]).image_click([1312, 934])
        self.clear_command()
        self.keyevent_command("HOME")
        self.start_app(ballsort_package)
        self.contrast_step(point)

    def test16_game_continue_classic(self):
        """
        继续游玩	应用从后台到前台进入关卡继续残局游玩时上报
        经典关卡、重开两次、无步骤
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "game_continue"
        self.GamePage = GamePage()
        self.GamePage.game_back()
        self.GamePage.quit_special().ad_close()
        self.sleep_time()
        self.GamePage.click_restart().click_restart()
        self.clear_command()
        self.keyevent_command("HOME")
        self.start_app(ballsort_package)
        self.contrast_step(point)

    def test17_same_color_finish_step_time(self):
        """
        同色收集完成	每一个颜色收集完成时上报
        :return:
        """
        point = "same_color_finish"
        self.GamePage = GamePage()
        first_tube = [113, 1504]
        second_tube = [324, 1420]
        third_tube = [521, 1405]
        fourth_tube = [712, 1474]
        fifth_tube = [938, 1445]
        sixth_tube = [1130, 1474]
        seventh_tube = [1332, 1425]
        self.GamePage.get_debug()
        self.image_click(first_tube).image_click(seventh_tube).sleep_time(1)
        self.image_click(first_tube).image_click(sixth_tube).sleep_time(1)
        self.image_click(third_tube).image_click(sixth_tube).sleep_time(1)
        self.image_click(fourth_tube).sleep_time().image_click(sixth_tube).sleep_time(1)
        self.image_click(second_tube).image_click(seventh_tube).sleep_time(1)
        self.image_click(fifth_tube).image_click(third_tube).sleep_time(1)
        self.clear_command()
        self.image_click(fifth_tube).image_click(seventh_tube).sleep_time(1)
        self.contrast_step(point)

    # def test18_game_win1(self):
    #     """
    #     关卡胜利	关卡胜利最后一步的球移动完，礼花特效结束时上报
    #     :return:
    #     """
    #     point = "game_win"
    #     self.GamePage = GamePage()
    #     first_tube = [98, 1401]
    #     second_tube = [265, 1366]
    #     third_tube = [447, 1327]
    #     fourth_tube = [629, 1464]
    #     fifth_tube = [796, 1528]
    #     sixth_tube = [983, 1489]
    #     seventh_tube = [1150, 1435]
    #     eighth_tube = [1351, 1420]
    #     self.GamePage.get_debug().get_debug().get_debug().debug_win().game_victory().get_debug()
    #     self.GamePage.click_restart()
    #     self.sleep_time()
    #     self.image_click(first_tube).image_click(seventh_tube).sleep_time(1)
    #     self.image_click(second_tube).image_click(eighth_tube).sleep_time(1)
    #     self.image_click(fifth_tube).sleep_time(1).image_click(eighth_tube).sleep_time(1)
    #     self.image_click(fourth_tube).image_click(first_tube).sleep_time(1)
    #     self.image_click(fourth_tube).image_click(seventh_tube).sleep_time(1)
    #     self.image_click(fourth_tube).image_click(first_tube).sleep_time(1)
    #     self.image_click(fourth_tube).image_click(seventh_tube).sleep_time(1)
    #     self.image_click(second_tube).image_click(fourth_tube).sleep_time(1)
    #     self.image_click(third_tube).image_click(fourth_tube).sleep_time(1)
    #     self.image_click(third_tube).image_click(second_tube).sleep_time(1)
    #     self.image_click(sixth_tube).image_click(second_tube).sleep_time(1)
    #     self.image_click(sixth_tube).image_click(fourth_tube).sleep_time(1)
    #     self.image_click(sixth_tube).image_click(third_tube).sleep_time(1)
    #     self.image_click(fifth_tube).image_click(second_tube).sleep_time(1)
    #     self.clear_command()
    #     self.image_click(fifth_tube).image_click(fourth_tube).sleep_time(1)
    #     self.contrast_step(point)

    def test18_game_win(self):
        point = "game_win"
        self.PrivacyPage = PrivacyPage()
        self.PrivacyPage.first_open_android().click_accept()
        self.sleep_time(4)
        self.clear_command()
        self.image_click([997, 1455]).image_click([437, 1460])
        self.sleep_time(4)
        self.contrast_step(point)

    def test19_home_page(self):
        """
        首页展示时上报：游戏页面返回首页
        从第一关胜利弹窗点击进入第二关，然后从第二关返回首页
        :return:
        """
        point = "home_page"
        self.GamePage = GamePage()
        self.GamePage.game_victory().goto_setting()
        self.clear_command()
        self.GamePage.goto_home()
        self.sleep_time()
        self.contrast_step(point)

    # def test20_home_page(self):
    #     """
    #     从收藏页面回到首页
    #     :return:
    #     """
    #     point = "home_page"
    #     self.HomePage = HomePage()
    #     self.ShopPage = ShopPage()
    #     self.HomePage.goto_shop()
    #     self.clear_command()
    #     self.ShopPage.shop_back_home()
    #     self.sleep_time()
    #     self.contrast_step(point)

    def test21_game_page(self):
        """
        杀掉进程后进入首页
        :return:
        """
        point = "home_page"
        ballsort_package = "game.ballsort.inner"
        self.stop_app(ballsort_package)
        self.clear_command()
        self.start_app(ballsort_package)
        self.contrast_step(point)

    def test22_home_play_click(self):
        """
        点击首页level按钮
        :return:
        """
        point = "home_play_click"
        self.HomePage = HomePage()
        self.clear_command()
        self.HomePage.home_goto_game()
        self.contrast_step(point)

    def test23_same_color_finish(self):
        """
        测试：step_time
        第一次收集完成上报0
        :return:
        """
        point = "same_color_finish"
        level2_first_tube = [319, 1469]
        level2_second_tube = [742, 1479]
        self.image_click(level2_first_tube)
        self.clear_command()
        self.image_click(level2_second_tube)
        self.contrast_step(point)

    def test24_game_restart(self):
        """
        关卡重开	关卡重开时上报
        retract_num:重开前的一次开局，用了几次撤回
        1.第二关通关，进入第三关
        2.走两个个步骤，使用一次加管，使用一次撤回
        3.等待3秒
        4.点击重开一次
        :return:
        """
        three_first_tube = [216, 1361]
        three_second_tube = [565, 1401]
        three_third_tube = [884, 1386]
        three_fourth_tube = [1214, 1425]
        point = "game_restart"
        self.GamePage = GamePage()
        self.GamePage.get_debug().get_debug()
        self.GamePage.debug_win()
        self.GamePage.game_victory().get_debug()
        self.sleep_time()
        self.image_click(three_first_tube).sleep_time(1).image_click(three_fourth_tube).sleep_time()
        self.image_click(three_third_tube).sleep_time(1).image_click(three_first_tube).sleep_time()
        self.GamePage.add_tube().add_tube()
        self.sleep_time()
        self.GamePage.click_withdraw()
        self.sleep_time(3)
        self.clear_command()
        self.GamePage.click_restart()
        self.contrast_step(point)
        return self

    def test25_game_action_action_type_1(self):
        """
        游戏操作	玩家发生游玩操作时上报
        取消选择。点击相同瓶两次，选中后取消；
        :return:
        """
        three_first_tube = [216, 1361]
        three_second_tube = [565, 1401]
        three_third_tube = [884, 1386]
        three_fourth_tube = [1214, 1425]
        point = "game_action"
        self.sleep_time()
        self.image_click(three_first_tube)
        self.sleep_time(3)
        self.image_click(three_first_tube)
        self.sleep_time()
        self.image_click(three_first_tube)
        self.sleep_time()
        self.clear_command()
        self.image_click(three_first_tube)
        self.contrast_step(point)
        return self

    def test26_game_action_action_type_2(self):
        """
               游戏操作	玩家发生游玩操作时上报
               选中瓶子A后，点击不可倒的瓶子B，瓶子A球落下，瓶子B球抬起
               :return:
               """
        first_tube = [216, 1361]
        second_tube = [452, 1405]
        third_tube = [707, 1425]
        fourth_tube = [997, 1455]
        fifth_tube = [1278, 1568]
        point = "game_action"
        self.sleep_time()
        self.image_click(first_tube)
        self.sleep_time()
        self.image_click(fourth_tube)
        self.sleep_time()
        self.image_click(first_tube)
        self.sleep_time(5)
        self.clear_command()
        self.sleep_time()
        self.image_click(fourth_tube)
        self.contrast_step(point)
        return self

    def test27_game_action_action_type_3(self):
        """
        游戏操作	玩家发生游玩操作时上报
        倒球全部成功，选中N个球，全部移动到另一个位置
        :return:
        """
        first_tube = [216, 1361]
        second_tube = [452, 1405]
        third_tube = [707, 1425]
        fourth_tube = [997, 1455]
        fifth_tube = [1278, 1568]
        point = "game_action"
        self.image_click(fourth_tube)
        self.sleep_time()
        self.image_click(third_tube)
        self.sleep_time()
        self.clear_command()
        self.sleep_time()
        self.image_click(fifth_tube)
        self.contrast_step(point)
        return self

    def test28_game_action_action_type_4(self):
        """
        游戏操作	玩家发生游玩操作时上报
        倒球部分成功，选中N个球，只有部分移动到另一个位置
        :return:
        """
        first_tube = [216, 1361]
        second_tube = [452, 1405]
        third_tube = [707, 1425]
        fourth_tube = [997, 1455]
        fifth_tube = [1278, 1568]
        point = "game_action"
        self.image_click(fifth_tube)
        self.sleep_time()
        self.image_click(first_tube)
        self.sleep_time()
        self.image_click(first_tube)
        self.clear_command()
        self.sleep_time()
        self.image_click(fifth_tube)
        self.contrast_step(point)
        return self

    def test29_item_click_is_free(self):
        """
        道具点击	玩家点击道具button时上报
        免费使用的道具
        :return:
        """
        point = "item_click"
        self.goto_level2()
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.add_tube()
        self.contrast_step(point)
        return self

    def test30_item_click_withdraw(self):
        """
        道具点击	玩家点击道具button时上报
        免费使用的道具
        :return:
        """
        # 第二关，未加管
        first_tube = [314, 1440]
        second_tube = [727, 1455]
        third_tube = [1125, 1430]
        point = "item_click"
        self.goto_level2()
        self.sleep_time()
        self.image_click(first_tube).image_click(second_tube)
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.click_withdraw()
        self.contrast_step(point)
        return self

    def test31_item_click_no_free(self):
        """
        道具点击	玩家点击道具button时上报
        非免费获得的道具
        :return:
        """
        # 第二关，未加管
        first_tube = [314, 1440]
        second_tube = [727, 1455]
        third_tube = [1125, 1430]
        ballsort_package = "game.ballsort.inner"
        point = "item_click"
        self.goto_level2()
        self.sleep_time()
        self.GamePage.add_tube().add_tube()
        self.clear_command()
        self.GamePage.add_tube().add_tool_page()
        self.sleep_time()
        self.stop_app(ballsort_package)
        self.contrast_step(point)
        return self

    def test32_item_click_restart(self):
        """
       道具点击	玩家点击道具button时上报

       :return:
       """
        point = "item_click"
        ballsort_package = "game.ballsort.inner"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        # self.GamePage.ad_close()
        self.sleep_time()
        self.GamePage.game_victory()
        self.GamePage.special_play().game_back().quit_special()
        self.GamePage.ad_close()
        self.sleep_time(10)
        self.clear_command()
        self.GamePage.click_restart()
        self.contrast_step(point)
        return self

    def test33_item_action_action_type(self):
        """
        道具使用成功	玩家发生道具使用时上报
        1	加瓶。使用加瓶道具
        :return:
        """
        point = "item_action"
        ballsort_package = "game.ballsort.inner"
        self.goto_level2()
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.add_tube()
        self.contrast_step(point)
        return self

    def test34_item_action_action_type(self):
        """
        道具使用成功	玩家发生道具使用时上报
        2	撤回。使用撤回道具；
        :return:
        """
        point = "item_action"
        first_tube = [314, 1440]
        second_tube = [727, 1455]
        third_tube = [1125, 1430]
        ballsort_package = "game.ballsort.inner"
        self.goto_level2()
        self.sleep_time()
        self.image_click(first_tube).image_click(second_tube)
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.click_withdraw()
        self.contrast_step(point)
        return self

    def test35_item_action_action_type(self):
        """
        道具使用成功	玩家发生道具使用时上报
        3	重开。点击重开按钮，重开次数+1
        :return:
        """
        point = "item_action"
        ballsort_package = "game.ballsort.inner"
        self.goto_level2()
        self.clear_command()
        self.sleep_time(7)
        self.GamePage.click_restart()
        self.contrast_step(point)
        return self

    def test36_get_item_item_type(self):
        """
        获得道具	每次玩家获得道具，数量增加时上报
        item_type:1加瓶
        :return:
        """
        point = "get_item"
        self.goto_level2()
        self.sleep_time()
        self.GamePage.add_tube().add_tube()
        self.GamePage.add_tube().add_tool_page()
        self.clear_command()
        self.sleep_time()
        self.GamePage.ad_close()
        self.sleep_time()
        self.contrast_step(point)
        return self

    def test37_get_item_item_type(self):
        """
        获得道具	每次玩家获得道具，数量增加时上报
        item_type:2撤回
        :return:
        """
        point = "get_item"
        level2_first_tube = [319, 1469]
        level2_second_tube = [742, 1479]
        self.goto_level2()
        self.sleep_time()
        for i in range(5):
            self.image_click(level2_first_tube).image_click(level2_second_tube)
            self.sleep_time(1)
            self.GamePage.click_withdraw()
        self.GamePage.click_withdraw().add_tool_page()
        self.clear_command()
        self.sleep_time()
        self.GamePage.ad_close()
        self.sleep_time()
        self.contrast_step(point)
        return self

    def test38_get_item_from_chest(self):
        """
        获得道具，每次玩家获得道具，数量增加时上报
        from: level_chest,从关卡宝箱中获取
        :return:
        """
        point = "get_item"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        # self.GamePage.ad_close()
        self.sleep_time()
        self.GamePage.game_victory()
        self.GamePage.special_play().game_back().quit_special()
        self.GamePage.ad_close()
        self.GamePage.victory_ad().debug_win().ad_close().game_victory().debug_win().ad_close().game_victory()
        self.clear_command()
        self.GamePage.claim_click().ad_close()
        self.contrast_step(point)
        return self

    def test39_special_quit_show(self):
        """
        特殊关点击退出弹窗展示	特殊关点击退出弹窗展示时上报
        :return:
        """
        point = "special_quit_show"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        # self.GamePage.ad_close()
        self.sleep_time()
        self.GamePage.game_victory().special_play()
        self.clear_command()
        self.GamePage.game_back()
        self.contrast_step(point)
        return self

    def test40_special_quit_click_close(self):
        """
        特殊关点击退出弹窗展示	点击特殊关退出弹窗
        result:close
        :return:
        """
        point = "special_quit_click"
        self.clear_command()
        self.GamePage = GamePage()
        self.GamePage.setting_close()
        self.contrast_step(point)
        return self

    def test41_special_quit_click_ok(self):
        """
        特殊关点击退出弹窗展示	点击特殊关退出弹窗
        result:ok
        :return:
        """
        point = "special_quit_click"
        self.GamePage = GamePage()
        self.GamePage.game_back()
        self.clear_command()
        self.GamePage.quit_special()
        self.contrast_step(point)
        return self

    def test42_level_chest_show(self):
        """
        关卡宝箱展示	关卡宝箱页开始展示时上报
        :return:
        """
        point = "level_chest_show"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        self.sleep_time()
        self.GamePage.game_victory()
        self.GamePage.special_play().game_back().quit_special()
        self.GamePage.ad_close()
        self.GamePage.victory_ad().debug_win().ad_close().game_victory()
        self.clear_command()
        self.GamePage.debug_win().ad_close()
        # self.GamePage.claim_click().ad_close()
        self.contrast_step(point)
        return self

    def test43_level_chest_open(self):
        """
        关卡宝箱打开	关卡宝箱页打开时上报
        :return:
        """
        point = "level_chest_open"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        self.sleep_time()
        self.GamePage.game_victory()
        self.GamePage.special_play().game_back().quit_special()
        self.GamePage.ad_close()
        self.GamePage.victory_ad().debug_win().ad_close().game_victory()
        self.clear_command()
        self.GamePage.debug_win().ad_close()
        # self.GamePage.claim_click().ad_close()
        self.contrast_step(point)
        return self

    def test44_level_chest_reward_get(self):
        """
        关卡宝箱奖励获取	关卡宝箱奖励成功获取时上报

        :return:
        """
        point = "level_chest_reward_get"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.claim_click()
        self.contrast_step(point)
        return self

    def test45_level_chest_claim_n(self):
        """
        宝箱奖励领取	点击宝箱奖励按钮时点击
        claim_type:N
        """
        point = "level_chest_claim"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        self.sleep_time()
        self.GamePage.game_victory()
        self.GamePage.special_play().game_back().quit_special()
        self.GamePage.ad_close()
        self.GamePage.victory_ad().debug_win().ad_close().game_victory()
        self.GamePage.debug_win().ad_close()
        self.clear_command()
        self.GamePage.double_claim_click().ad_close()
        self.contrast_step(point)
        return self

    def test46_level_chest_claim_1(self):
        """
        宝箱奖励领取	点击宝箱奖励按钮时点击
        claim_type:1
        """
        point = "level_chest_claim"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        for i in range(3):
            self.GamePage.game_victory().debug_win()
        self.GamePage.setting_close().game_victory().debug_win().ad_close().game_victory()
        self.sleep_time()
        self.GamePage.game_victory()
        self.GamePage.special_play().game_back().quit_special()
        self.GamePage.ad_close()
        self.GamePage.victory_ad().debug_win().ad_close().game_victory()
        self.GamePage.debug_win().ad_close()
        self.clear_command()
        self.GamePage.claim_click().ad_close()
        self.contrast_step(point)
        return self

    def test47_collection_pv_game(self):
        """
        收藏界面展示	收藏界面展示时上报
        from:game
        :return:
        """
        point = "collection_pv"
        self.goto_level2()
        self.GamePage.goto_setting()
        self.clear_command()
        self.GamePage.setting_goto_shop()
        self.contrast_step(point)
        return self

    def test48_collection_pv_home(self):
        """
        收藏界面展示	收藏界面展示时上报
        from:home
        :return:
        """
        point = "collection_pv"
        self.GamePage = GamePage()
        self.HomePage = HomePage()
        self.GamePage.game_back().goto_setting().goto_home()
        self.clear_command()
        self.HomePage.goto_shop()
        self.contrast_step(point)
        return self

    def test49_tube_change_success(self):
        """

        更换管子	点击更换管子成功时上报
        :return:
        """
        point = "tube_change_success"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug()
        self.ShopPage = ShopPage()
        self.GamePage.debug_change_level(2, "30").goto_setting().setting_goto_shop()
        self.sleep_time()
        self.clear_command()
        self.image_click([938, 1052])
        self.contrast_step(point)
        return self

    def test50_theme_change_success(self):
        """
        更换背景	点击更换背景成功时上报
        :return:
        """
        point = "theme_change_success"
        self.ShopPage = ShopPage()
        self.ShopPage.goto_background()
        self.clear_command()
        self.image_click([938, 1052])
        self.contrast_step(point)
        return self

    def test51_ball_change_success(self):
        """
        更换球	点击更换球成功时上报
        :return:
        """
        point = "ball_change_success"
        self.ShopPage = ShopPage()
        self.ShopPage.goto_ball()
        self.clear_command()
        self.image_click([938, 1052])
        self.contrast_step(point)
        return self

    def test51_add_coin_click_tube(self):
        """
        点击加金币	点击底部加金币按钮时上报
        page:tube
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "add_coin_click"
        self.ShopPage = ShopPage()
        self.HomePage = HomePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.clear_command()
        self.ShopPage.ad_coins_click()
        self.contrast_step(point)
        return self

    def test52_add_coin_click_theme(self):
        """
        点击加金币	点击底部加金币按钮时上报
        page:theme
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "add_coin_click"
        self.ShopPage = ShopPage()
        self.HomePage = HomePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.ShopPage.goto_background()
        self.sleep_time(1)
        self.clear_command()
        self.ShopPage.ad_coins_click()
        self.contrast_step(point)
        return self

    def test53_add_coin_click_ball(self):
        """
        点击加金币	点击底部加金币按钮时上报
        page:ball
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "add_coin_click"
        self.ShopPage = ShopPage()
        self.HomePage = HomePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.ShopPage.goto_ball()
        self.sleep_time(1)
        self.clear_command()
        self.ShopPage.ad_coins_click()
        self.contrast_step(point)
        return self

    def test54_buy_click_tube(self):
        """
        买皮肤	点击购买管皮肤/主题/球皮肤时上报
        type:tube
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "buy_click"
        self.ShopPage = ShopPage()
        self.HomePage = HomePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.clear_command()
        self.ShopPage.buy_click()
        self.contrast_step(point)
        return self

    def test55_buy_click_theme(self):
        """
        买皮肤
        type:theme
        :return:
        """
        point = "buy_click"
        self.GamePage = GamePage()
        self.ShopPage = ShopPage()
        self.GamePage.setting_close()
        self.ShopPage.goto_background()
        self.clear_command()
        self.ShopPage.buy_click()
        self.contrast_step(point)
        return self

    def test56_buy_click_theme(self):
        """
        买皮肤
        type:ball
        :return:
        """
        point = "buy_click"
        self.GamePage = GamePage()
        self.ShopPage = ShopPage()
        self.GamePage.setting_close()
        self.ShopPage.goto_ball()
        self.clear_command()
        self.ShopPage.buy_click()
        self.contrast_step(point)
        return self

    def test57_collection_award_popup(self):
        """"
        奖品弹窗
        皮肤奖励弹窗展示
        获得主题背景
        """
        point = "collection_award_popup"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug()
        self.GamePage.debug_change_level(2, "8")
        self.sleep_time()
        self.GamePage.debug_win().ad_close()
        self.clear_command()
        self.GamePage.game_victory()
        self.contrast_step(point)
        return self

    def test58_collection_award_popup_click(self):
        """
        奖品弹窗点击	皮肤奖励弹窗点击
        :return:
        button:later
        """
        point = "collection_award_popup_click"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.reward_page_no_use()
        self.contrast_step(point)
        return self

    def test59_collection_award_popup(self):
        """"
        奖品弹窗
        皮肤奖励弹窗展示
        获得管背景
        """
        point = "collection_award_popup"
        self.GamePage = GamePage()
        self.GamePage.debug_change_level(2, "18")
        self.sleep_time()
        self.GamePage.debug_win().ad_close()
        self.clear_command()
        self.GamePage.game_victory()
        self.contrast_step(point)
        return self

    def test60_collection_award_popup_click(self):
        """
        奖品弹窗点击	皮肤奖励弹窗点击
        :return:
        button:user
        """
        point = "collection_award_popup_click"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.reward_page_use()
        self.contrast_step(point)
        return self

    def test61_collection_award_popup(self):
        """"
        奖品弹窗
        皮肤奖励弹窗展示
        获得球奖励
        """
        point = "collection_award_popup"
        self.GamePage = GamePage()
        self.GamePage.debug_change_level(2, "28")
        self.sleep_time()
        self.GamePage.debug_win().ad_close()
        self.clear_command()
        self.GamePage.game_victory()
        self.contrast_step(point)
        return self

    def test62_collection_award_popup_click(self):
        """
        奖品弹窗点击	皮肤奖励弹窗点击
        :return:
        button:user
        """
        point = "collection_award_popup_click"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.reward_page_use()
        self.contrast_step(point)
        return self

    def test63_click_get_new_skin(self):
        """
        点击获得新皮肤（未成功）	点击奖励弹窗现在使用，或者商城页点击获得时上报
        from:reward
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "click_get_new_skin"
        self.GamePage = GamePage()
        self.GamePage.debug_change_level(2, "38")
        self.sleep_time()
        self.GamePage.debug_win().ad_close()
        self.GamePage.game_victory()
        self.clear_command()
        self.GamePage.reward_page_use()
        self.stop_app(ballsort_package)
        self.contrast_step(point)
        return self

    def test64_click_get_new_skin(self):
        """
         点击获得新皮肤（未成功）	点击奖励弹窗现在使用，或者商城页点击获得时上报
        from:shop
        is_ad : ture
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "click_get_new_skin"
        self.HomePage = HomePage()
        self.ShopPage = ShopPage()
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.clear_command()
        self.ShopPage.ad_claim()
        self.contrast_step(point)
        self.stop_app(ballsort_package)
        return self

    def test65_click_get_new_skin(self):
        """
         点击获得新皮肤（未成功）	点击奖励弹窗现在使用，或者商城页点击获得时上报
        from:shop
        is_ad : false
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "click_get_new_skin"
        self.HomePage = HomePage()
        self.ShopPage = ShopPage()
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.clear_command()
        self.ShopPage.buy_click()
        self.contrast_step(point)
        return self

    def test66_get_new_skin(self):
        """
        成功获得新皮肤	点击奖励弹窗现在使用，或者商城页点击获得时上报
        is_ad:ture
        from:shop
        :return:
        """
        point = "get_new_skin"
        self.GamePage = GamePage()
        self.ShopPage = ShopPage()
        self.GamePage.setting_close()
        self.ShopPage.ad_claim()
        self.clear_command()
        self.GamePage.ad_close()
        self.contrast_step(point)
        return self

    def test67_get_new_skin(self):
        """
        成功获得新皮肤	点击奖励弹窗现在使用，或者商城页点击获得时上报
        is_ad:ture
        from: reward
        :return:
        """
        point = "get_new_skin"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug()
        self.GamePage.debug_change_level(2, "88")
        self.sleep_time()
        self.GamePage.debug_win().ad_close()
        self.GamePage.game_victory()
        self.GamePage.reward_page_use()
        self.clear_command()
        self.GamePage.ad_close()
        self.contrast_step(point)
        return self

    def test68_get_new_skin(self):
        """
        成功获得新皮肤	点击奖励弹窗现在使用，或者商城页点击获得时上报
        is_ad:ture
        from: reward
        :return:
        """
        point = "get_new_skin"
        self.GamePage = GamePage()
        self.HomePage = HomePage()
        self.ShopPage = ShopPage()
        self.GamePage.goto_setting().goto_home()
        self.HomePage.goto_shop()
        for i in range(2):
            self.ShopPage.goto_ball().ad_coins_click()
            self.GamePage.ad_close()
            self.sleep_time(302)
        self.ShopPage.goto_ball().ad_coins_click()
        self.GamePage.ad_close()
        self.clear_command()
        self.ShopPage.buy_click()
        self.contrast_step(point)
        return self

    def test69_settings_pv(self):
        """
        设置弹窗展示	设置弹窗展示时上报
        from: game
        :return:
        """
        point = "settings_pv"
        self.goto_level2()
        self.clear_command()
        self.GamePage.goto_setting()
        self.contrast_step(point)
        return self

    def test70_settings_sound(self):
        """
        打开/关闭音效	设置弹窗点击音效开关时上报
        result:off
        :return:
        """
        point = "settings_sound"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.setting_close_sound()
        self.contrast_step(point)
        return self

    def test71_settings_sound(self):
        """
        打开/关闭音效	设置弹窗点击音效开关时上报
        result:on
        :return:
        """
        self.test70_settings_sound()

    def test72_settings_vibration(self):

        """
        打开/关闭振动	设置弹窗点击振动开关时上报
        result:off
        :return:
        """
        point = "settings_vibration"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.setting_close_vibration()
        self.contrast_step(point)
        return self

    def test73_settings_vibration(self):
        """
        打开/关闭振动	设置弹窗点击振动开关时上报
        result:on
        :return:
        """
        point = "settings_vibration"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.setting_open_vibration()
        self.contrast_step(point)
        return self

    def test74_settings_shop_click(self):
        """
        从设置打开商店页	设置点击商店入口时上报
        :return:
        """
        point = "settings_shop_click"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.setting_goto_shop()
        self.contrast_step(point)
        return self

    def test75_settings_contact(self):
        """
        联系我们	设置弹窗点击contact时上报
        :return:
        """
        point = "settings_contact"
        self.GamePage = GamePage()
        self.ShopPage = ShopPage()
        self.ShopPage.shop_back_home()
        self.GamePage.goto_setting()
        self.clear_command()
        self.GamePage.goto_contact_us()
        self.contrast_step(point)

    def test76_settings_language(self):
        """
        语言选择	设置弹窗修改语言时上报
        将英语调整为葡萄牙语
        :return:
        """
        point = "settings_language"
        self.keyevent_command("back").keyevent_command("back")
        self.GamePage = GamePage()
        self.GamePage.goto_setting().setting_language()
        self.GamePage.change_language_espanol()
        self.clear_command()
        self.GamePage.language_ok()
        self.contrast_step(point)

    def test77_settings_pv(self):
        """
         设置弹窗展示	设置弹窗展示时上报
        from: game
        :return:
        """

        point = "settings_pv"
        self.GamePage = GamePage()
        self.GamePage.goto_home()
        self.clear_command()
        self.GamePage.goto_setting()
        self.contrast_step(point)
        return self

    def test78_settings_sound(self):
        """
        打开/关闭音效	设置弹窗点击音效开关时上报
        from: home
        :return:
        """
        self.test70_settings_sound()
        return self

    def test79_settings_vibration(self):
        """
        打开/关闭振动	设置弹窗点击振动开关时上报
        from: home
        :return:
        """
        self.test72_settings_vibration()
        return self

    def get_rating_guide(self):
        """
        得到评分引导页面
        :return:
        """
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        self.GamePage.game_victory().debug_win().game_victory().debug_win()
        return self

    def test80_rating_guide_pv(self):
        """
        评分引导弹窗展示	评分引导弹窗展示时上报
        :return:
        """
        point = "rating_guide_pv"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug().debug_win()
        self.GamePage.game_victory().debug_win().game_victory()
        self.clear_command()
        self.GamePage.debug_win()
        # self.sleep_time()
        self.contrast_step(point)
        return self

    def test81_rating_guide_click(self):
        """
        评分引导弹窗点击	评分引导弹窗点击时上报
        result:0
        :return:
        """
        point = "rating_guide_click"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.rating_zero_star()
        self.contrast_step(point)
        return self

    def test82_rating_guide_click(self):
        """
        评分引导弹窗点击	评分引导弹窗点击时上报
        result:1
        :return:
        """
        point = "rating_guide_click"
        self.GamePage = GamePage()
        self.GamePage.click_one_star()
        self.clear_command()
        self.GamePage.rating_one_star()
        self.contrast_step(point)
        return self

    def test83_rating_guide_click(self):
        """
        评分引导弹窗点击	评分引导弹窗点击时上报
        result:5
        :return:
        """
        point = "rating_guide_click"
        self.GamePage = GamePage()
        self.get_rating_guide()
        self.GamePage.click_five_Star()
        self.clear_command()
        self.GamePage.rating_five_star()
        self.contrast_step(point)
        return self

    def test84_home_back_click(self):
        """
        游戏中返回主页	游戏设置点击home时上报
        :return:
        """
        point = "home_back_click"
        self.goto_level2()
        self.GamePage.goto_setting()
        self.clear_command()
        self.GamePage.goto_home()
        self.contrast_step(point)

    def test85_add_item_pop_show(self):
        """
        加道具弹窗展示	加道具弹窗展示时上报
        item_type:1
        :return:
        """
        point = "add_item_pop_show"
        self.goto_level2()
        self.sleep_time()
        self.GamePage.add_tube().add_tube()
        self.clear_command()
        self.GamePage.add_tube()
        self.contrast_step(point)
        return self

    def test86_add_item_pop_click(self):
        """
        加道具弹窗点击	点击加道具弹窗时上报
        item_type:1
        click_where:ad
        :return:
        """
        point = "add_item_pop_click"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.add_tool_page()
        self.contrast_step(point)
        return self

    def test87_add_item_pop_click(self):
        """
        加道具弹窗点击	点击加道具弹窗时上报
        where :money_buy
        :return:
        """
        point = "add_item_pop_click"
        ballsort_package = "game.ballsort.inner"
        self.GamePage = GamePage()
        self.HomePage = HomePage()
        self.ShopPage = ShopPage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.home_goto_game()
        self.GamePage.add_tube()
        self.clear_command()
        self.ShopPage.ad_coins_click()
        self.contrast_step(point)
        return self

    def test88_add_item_pop_click(self):
        """
        加道具弹窗点击	点击加道具弹窗时上报
        where :add_coin
        :return:
        """
        point = "add_item_pop_click"
        self.GamePage = GamePage()
        self.GamePage.setting_close()
        self.clear_command()
        self.GamePage.add_coin_click()
        self.contrast_step(point)

    def test89_item_pop_show(self):
        point = "add_item_pop_click"
        level2_first_tube = [255, 1346]
        level2_second_tube = [540, 1405]
        self.GamePage = GamePage()
        self.GamePage.setting_close().setting_close()
        self.sleep_time(3)
        for i in range(5):
            self.image_click(level2_first_tube)
            self.sleep_time(1)
            self.image_click(level2_second_tube)
            self.sleep_time(1)
            self.GamePage.click_withdraw()
        self.GamePage.click_withdraw()
        self.clear_command()
        self.GamePage.setting_close()
        self.contrast_step(point)
        return self

    def test90_get_coins_popshow(self):
        """
        加金币弹窗展示
        type:tube
        from:no_money_buy_skin
        :return:
        """
        point = "get_coins_popshow"
        self.ShopPage = ShopPage()
        self.goto_level2()
        self.GamePage.goto_setting().setting_goto_shop()
        self.clear_command()
        self.ShopPage.get_coins()
        self.contrast_step(point)
        return self

    def test91_get_coins_popshowclick(self):
        """
        加金币弹窗点击
        from: no_money_buy_skin
        :return:
        """
        point = "get_coins_popshowclick"
        self.ShopPage = ShopPage()
        self.clear_command()
        self.ShopPage.click_get_coin_ad()
        self.contrast_step(point)
        return self

    def test92_get_coins_popshow(self):
        """
        加金币弹窗展示
        type:theme
        from:no_money_buy_skin
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "get_coins_popshow"
        self.ShopPage = ShopPage()
        self.HomePage = HomePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(3)
        self.HomePage.goto_shop()
        self.ShopPage.goto_background()
        self.clear_command()
        self.ShopPage.get_coins()
        self.contrast_step(point)
        return self

    def test93_get_coins_popshowclick(self):
        """
        加金币弹窗点击
        from: no_money_buy_skin
        :return:
        """
        point = "get_coins_popshowclick"
        self.ShopPage = ShopPage()
        self.clear_command()
        self.ShopPage.click_get_coin_ad()
        self.contrast_step(point)
        return self

    def test94__get_coins_popshow(self):
        """
        加金币弹窗展示
        type:ball
        from:no_money_buy_skin
        :return:
        """
        ballsort_package = "game.ballsort.inner"
        point = "get_coins_popshow"
        self.ShopPage = ShopPage()
        self.HomePage = HomePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(3)
        self.HomePage.goto_shop()
        self.ShopPage.goto_ball()
        self.clear_command()
        self.ShopPage.get_coins()
        self.contrast_step(point)
        return self

    def test95_get_coins_popshowclick(self):
        """
        加金币弹窗点击
        from: no_money_buy_skin
        :return:
        """
        point = "get_coins_popshowclick"
        self.ShopPage = ShopPage()
        self.clear_command()
        self.ShopPage.click_get_coin_ad()
        self.contrast_step(point)
        return self

    def test96_get_coins_popshow(self):
        """
        加金币弹窗展示
        type：item
        from: no_money_buy_item
        :return:
        """
        point = "get_coins_popshow"
        self.ShopPage = ShopPage()
        self.goto_level2()
        self.GamePage.add_tube().add_tube().add_tube()
        self.clear_command()
        self.ShopPage.ad_coins_click()
        self.contrast_step(point)
        return self

    def test97_get_coins_popshowclick(self):
        """
        加金币弹窗点击
        from: no_money_buy_item
        where:close
        :return:
        """
        point = "get_coins_popshowclick"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.setting_close()
        self.contrast_step(point)
        return self

    def test98_get_coins_popshow(self):
        """
        结算页面点击金币加号
        :return:
        """
        point = "get_coins_popshow"
        self.ShopPage = ShopPage()
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug()
        self.GamePage.debug_win()
        self.clear_command()
        self.GamePage.add_coin_click()
        self.contrast_step(point)
        return self

    def test99_get_coins_popshowclick(self):
        """
        结算页面点击金币加号
        :return:
        """
        point = "get_coins_popshowclick"
        self.GamePage = GamePage()
        self.clear_command()
        self.GamePage.setting_close()
        self.contrast_step(point)
        return self

    def test100_get_coins_popshow(self):
        """
        收藏页面加号入口
        :return:
        """
        point = "get_coins_popshow"
        ballsort_package = "game.ballsort.inner"
        self.HomePage = HomePage()
        self.ShopPage = ShopPage()
        self.GamePage = GamePage()
        self.stop_app(ballsort_package)
        self.start_app(ballsort_package)
        self.sleep_time(4)
        self.HomePage.goto_shop()
        self.clear_command()
        self.GamePage.add_coin_click()
        self.contrast_step(point)
        return self

    def test101_get_coins_popshowclick(self):
        """
        收藏页面点击金币加号
        :return:
        """
        self.test99_get_coins_popshowclick()
        return self

    def test102_get_coins_popshow(self):
        """
        获得道具页面点击加号
        :return:
        """
        point = "get_coins_popshow"
        self.goto_level2()
        self.GamePage.add_tube().add_tube().add_tube()
        self.clear_command()
        self.GamePage.add_coin_click()
        self.contrast_step(point)
        return self

    def test103_get_coins_popshowclick(self):
        """
        获得管页面点击点击加号
        :return:
        """
        self.test99_get_coins_popshowclick()
        return self

    def test104_get_coins_popshow(self):
        """
        获得撤回道具页面点击加号
        :return:
        """
        point = "get_coins_popshow"
        self.GamePage = GamePage()
        self.GamePage.setting_close()
        level2_first_tube = [255, 1346]
        level2_second_tube = [540, 1405]
        self.sleep_time(3)
        for i in range(5):
            self.image_click(level2_first_tube)
            self.sleep_time(1)
            self.image_click(level2_second_tube)
            self.sleep_time(1)
            self.GamePage.click_withdraw()
        self.GamePage.click_withdraw()
        self.clear_command()
        self.GamePage.add_coin_click()
        self.contrast_step(point)
        return self

    def test105_get_coins_popshowclick(self):
        """
        获得撤回道具页面点击点击加号
        :return:
        """
        point = "get_coins_popshowclick"
        self.ShopPage = ShopPage()
        self.clear_command()
        self.ShopPage.click_get_coin_ad()
        self.contrast_step(point)
        return self

