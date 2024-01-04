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
from base.base_point_user import GetPointUser


class TestPoint(BaseElement, GetPoint):
    # auto_setup(__file__, logdir=True,
    #            devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&"])
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

    # def correct_point_time(self, correct_point, about_time_key):
    #     """
    #     得到正确的埋点的关于time的值 time_between_last_finish:3.0
    #     :return:
    #     """
    #     # correct_point = "same_color_finish => {activity_id:0,activity_name:classic,levelid:5,step_num:5,finish_times:2,step_between_last_finish:2,time_between_last_finish:3.0,level_restart_num:0,level_start_num:1,rank_lid:5,"
    #     last_time_start = correct_point.find(f"{about_time_key}") + len(f"{about_time_key}")
    #     last_time_end = correct_point.find(",", last_time_start)
    #     last_time = float(correct_point[last_time_start:last_time_end])
    #     return last_time

    def get_point_time(self, point, about_time_key):
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        last_time_start = result.find(f"{about_time_key}") + len(f"{about_time_key}")
        last_time_end = result.find(",", last_time_start)
        last_time = float(result[last_time_start:last_time_end])
        print(last_time)
        return last_time

    def extract_string_point(self, correct_point, about_time_key):
        """
        正确的埋点的除去时间部分
        :param about_time_key:
        :param correct_point:
        :return:
        """
        last_time_start = correct_point.find(f"{about_time_key}") + len(f"{about_time_key}")
        last_time_end = correct_point.find(",", last_time_start)
        extract_string = correct_point[:last_time_start] + correct_point[last_time_end:]
        print(extract_string)
        return extract_string

    def get_point_extract_string(self, point, about_time_key):
        """
        得到的埋点的除去时间部分
        :param point:
        :param about_time_key:
        :return:
        """
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        last_time_start = result.find(f"{about_time_key}") + len(f"{about_time_key}")
        last_time_end = result.find(",", last_time_start)
        extract_string = result[:last_time_start] + result[last_time_end:]
        print(extract_string)
        return extract_string

    def setup_class(self):
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    def assert_result(self, point, correct_point):
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        assert result == correct_point

    def test17_same_color_finish_step_time(self):
        """
        同色收集完成	每一个颜色收集完成时上报
        :return:
        """
        point = "same_color_finish"
        data = "same_color_finish => {activity_id:0,activity_name:classic,levelid:5,step_num:5,finish_times:2,step_between_last_finish:2,time_between_last_finish:3.0,level_restart_num:0,level_start_num:1,rank_lid:5,"
        about_time_key = "time_between_last_finish:"
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug()
        self.GamePage.debug_win().game_victory().debug_win().game_victory().debug_win().setting_close().game_victory()
        first_tube = [113, 1504]
        second_tube = [324, 1420]
        third_tube = [521, 1405]
        fourth_tube = [712, 1474]
        fifth_tube = [938, 1445]
        sixth_tube = [1130, 1474]
        seventh_tube = [1332, 1425]
        self.GamePage.get_debug()
        self.image_click(first_tube).image_click(sixth_tube).sleep_time(1)
        self.image_click(second_tube).image_click(sixth_tube).sleep_time(1)
        self.image_click(fourth_tube).image_click(sixth_tube).sleep_time(1)
        self.image_click(fifth_tube).image_click(sixth_tube).sleep_time(1)
        self.image_click(first_tube).image_click(seventh_tube).sleep_time(1)
        self.clear_command()
        self.image_click(third_tube).image_click(seventh_tube).sleep_time(1)
        self.contrast_step(point)
        assert 2 <= self.get_point_time(point, about_time_key) <= 4
        string1 = self.extract_string_point(data, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False

        # self.assert_result(point, correct_point)

        return self

    def test23_same_color_finish(self):
        """
        测试：step_time
        第一次收集完成上报0
        :return:
        """
        point = "same_color_finish"
        about_time_key = "time_between_last_finish:"
        correct_point = "same_color_finish => {activity_id:0,activity_name:classic,levelid:2,step_num:0,finish_times:1,step_between_last_finish:0,time_between_last_finish:0.0,level_restart_num:0,level_start_num:1,rank_lid:2,"
        level2_first_tube = [319, 1469]
        level2_second_tube = [742, 1479]
        self.goto_level2()
        self.image_click(level2_first_tube)
        self.clear_command()
        self.image_click(level2_second_tube)
        self.contrast_step(point)
        # assert 2 <= self.get_point_time(point, about_time_key) <= 4
        # string1 = self.extract_string_point(correct_point, about_time_key)
        # string2 = self.get_point_extract_string(point, about_time_key)
        # if string1 == string2:
        #     assert True
        # else:
        #     assert False
        self.assert_result(point, correct_point)

    def test18_game_win(self):
        point = "game_win"
        about_time_key1 = "level_time:"
        about_time_key2 = "win_time:"
        correct_point = "game_win => {activity_id:0,activity_name:classic,levelid:1,game_start_scene:initialization,level_restart_num:0,level_start_num:1,retract_num:0,add_tube_num:0,level_add_tube_num:0,level_time:9.3,win_time:9.3,win_step:0,pass_num:1,win_num:1,rank_lid:1,"
        self.PrivacyPage = PrivacyPage()
        self.PrivacyPage.first_open_android().click_accept()
        self.sleep_time(4)
        self.clear_command()
        self.image_click([997, 1455]).image_click([437, 1460])
        self.sleep_time(4)
        self.contrast_step(point)
        assert 8 <= self.get_point_time(point, about_time_key1) <= 10
        assert 8 <= self.get_point_time(point, about_time_key2) <= 10
        string1 = self.extract_string_point(correct_point, about_time_key1)
        string2 = self.get_point_extract_string(point, about_time_key1)
        string3 = self.extract_string_point(correct_point, about_time_key2)
        string4 = self.get_point_extract_string(point, about_time_key2)
        if string1 == string2 and string3 == string4:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
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
        about_time_key = "pause_time:"
        correct_point = "game_action => {activity_id:0,activity_name:classic,levelid:3,action_type:1,level_restart_num:1,level_start_num:2,pause_time:4.5,status_later:bbcc, ccaa, aabb, 0000, 00,rank_lid:3,"
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
        assert 4 <= self.get_point_time(point, about_time_key) <= 5
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
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
        about_time_key = "pause_time:"
        correct_point = "game_action => {activity_id:0,activity_name:classic,levelid:3,action_type:2,level_restart_num:1,level_start_num:2,pause_time:9.5,status_later:bb00, ccaa, aabb, cc00, 00,rank_lid:3,"
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
        assert 9 <= self.get_point_time(point, about_time_key) <= 10
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
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
        about_time_key = "pause_time:"
        correct_point = "game_action => {activity_id:0,activity_name:classic,levelid:3,action_type:3,level_restart_num:1,level_start_num:2,pause_time:6.5,status_later:bb00, ccaa, aa00, cc00, bb,rank_lid:3,"
        self.image_click(fourth_tube)
        self.sleep_time()
        self.image_click(third_tube)
        self.sleep_time()
        self.clear_command()
        self.sleep_time()
        self.image_click(fifth_tube)
        self.contrast_step(point)
        assert 6 <= self.get_point_time(point, about_time_key) <= 7
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
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
        about_time_key = "pause_time:"
        correct_point = "game_action => {activity_id:0,activity_name:classic,levelid:3,action_type:4,level_restart_num:1,level_start_num:2,pause_time:4.5,status_later:bb00, ccaa, aa00, cc00, bb,rank_lid:3,"
        self.image_click(fifth_tube)
        self.sleep_time()
        self.image_click(first_tube)
        self.sleep_time()
        self.image_click(first_tube)
        self.clear_command()
        self.sleep_time()
        self.image_click(fifth_tube)
        self.contrast_step(point)
        assert 4 <= self.get_point_time(point, about_time_key) <= 5
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
        return self

    def test29_item_click_is_free(self):
        """
        道具点击	玩家点击道具button时上报
        免费使用的道具
        :return:
        """
        point = "item_click"
        about_time_key = "use_time:"
        correct_point = "item_click => {activity_id:0,activity_name:classic,levelid:2,use_time:9,move_num:0,level_restart_num:0,level_start_num:1,is_free:True,action_type:1,rank_lid:2,"
        self.goto_level2()
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.add_tube()
        self.contrast_step(point)
        assert 8 <= self.get_point_time(point, about_time_key) <= 10
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
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
        about_time_key = "use_time:"
        correct_point = "item_click => {activity_id:0,activity_name:classic,levelid:2,use_time:10,move_num:1,level_restart_num:0,level_start_num:1,is_free:True,action_type:2,rank_lid:2,"
        self.goto_level2()
        self.sleep_time()
        self.image_click(first_tube).image_click(second_tube)
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.click_withdraw()
        self.contrast_step(point)
        assert 9 <= self.get_point_time(point, about_time_key) <= 11
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
        return self

    def test32_item_click_restart(self):
        """
       道具点击	玩家点击道具button时上报

       :return:
       """
        point = "item_click"
        about_time_key = "use_time:"
        correct_point = "item_click => {activity_id:0,activity_name:classic,levelid:6,use_time:10,move_num:0,level_restart_num:0,level_start_num:1,is_free:True,action_type:3,rank_lid:7,"
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
        assert 9 <= self.get_point_time(point, about_time_key) <= 11
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外的埋点不正确")
            assert False
        # self.assert_result(point, correct_point)
        return self

    def test36_item_click_is_free_false(self):
        """
        点击道具button，看广告的
        :return:
        """
        point = "item_click"
        about_time_key = "use_time:"
        ballsort_package = "game.ballsort.inner"
        correct_point = "item_click => {activity_id:0,activity_name:classic,levelid:2,use_time:13,move_num:0,level_restart_num:0,level_start_num:1,is_free:False,action_type:1,rank_lid:2,"
        self.goto_level2()
        self.GamePage.add_tube().add_tube()
        self.sleep_time(5)
        self.clear_command()
        self.GamePage.add_tube()
        self.contrast_step(point)
        assert 12 <= self.get_point_time(point, about_time_key) <= 15
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外的埋点不正确")
            assert False
        # self.assert_result(point, correct_point)
        return self

    def test37_item_action_is_free_false(self):
        point = "item_action"
        about_time_key = "use_time:"
        correct_point = "item_action => {activity_id:0,activity_name:classic,levelid:2,action_type:1,use_time:9.0,move_num:0,level_restart_num:0,level_start_num:1,is_free:False,rank_lid:2,"
        self.goto_level2()
        self.GamePage.add_tube().add_tube().add_tube()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time()
        self.contrast_step(point)
        assert 8 <= self.get_point_time(point, about_time_key) <= 10
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外的埋点不正确")
            assert False

    def test33_item_action_action_type(self):
        """
        道具使用成功	玩家发生道具使用时上报
        1	加瓶。使用加瓶道具
        :return:
        """
        point = "item_action"
        about_time_key = "use_time:"
        ballsort_package = "game.ballsort.inner"
        correct_point = "item_action => {activity_id:0,activity_name:classic,levelid:2,action_type:1,use_time:9,move_num:0,level_restart_num:0,level_start_num:1,is_free:True,rank_lid:2,"
        self.goto_level2()
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.add_tube()
        self.contrast_step(point)
        assert 8 <= self.get_point_time(point, about_time_key) <= 10
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外的埋点不正确")
            assert False
        # self.assert_result(point, correct_point)
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
        about_time_key = "use_time:"
        correct_point = "item_action => {activity_id:0,activity_name:classic,levelid:2,action_type:2,use_time:10,move_num:1,level_restart_num:0,level_start_num:1,is_free:True,rank_lid:2,"
        self.goto_level2()
        self.sleep_time()
        self.image_click(first_tube).image_click(second_tube)
        self.clear_command()
        self.sleep_time(5)
        self.GamePage.click_withdraw()
        self.contrast_step(point)
        assert 9 <= self.get_point_time(point, about_time_key) <= 11
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外的埋点不正确")
            assert False
        # self.assert_result(point, correct_point)
        return self

    def test35_item_action_action_type(self):
        """
        道具使用成功	玩家发生道具使用时上报
        3	重开。点击重开按钮，重开次数+1
        :return:
        """
        point = "item_action"
        ballsort_package = "game.ballsort.inner"
        about_time_key = "use_time:"
        correct_point = "item_action => {activity_id:0,activity_name:classic,levelid:2,action_type:3,use_time:11,move_num:0,level_restart_num:0,level_start_num:1,is_free:True,rank_lid:2,"
        self.goto_level2()
        self.clear_command()
        self.sleep_time(7)
        self.GamePage.click_restart()
        self.contrast_step(point)
        assert 10 <= self.get_point_time(point, about_time_key) <= 12
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外的埋点不正确")
            assert False
        # self.assert_result(point, correct_point)
        return self

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
        about_time_key = "last_time:"
        correct_point = "game_restart => {activity_id:0,activity_name:classic,levelid:3,retract_num:0,add_tube_num:2,game_start_scene:new,level_restart_num:1,level_start_num:2,last_time:21,last_move:2,rank_lid:3,"
        self.GamePage = GamePage()
        self.goto_level2()
        self.GamePage.get_debug().get_debug().get_debug()
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
        assert 20 <= self.get_point_time(point, about_time_key) <= 22
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            assert False
        # self.assert_result(point, correct_point)
        return self
