# coding = utf-8
# Author: Zoe
# File: SortBall_language.py
# Time: 2023/10/26 2:30 下午
import os
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from page.gameplay_guide_page import GamePlayGuide
from page.privacy_page import PrivacyPage
from base.base import BaseElement
from page.game_page import GamePage
from page.home_page import HomePage
from page.shop_page import ShopPage

# 暂时关闭截图
ST.SAVE_IMAGE = False
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class SortBallLanguage:
    language = "英语"
    name = rf"{language}/{language}"

    def __init__(self):
        self.GamePlayGuide = GamePlayGuide
        self.PrivacyPage = PrivacyPage
        self.BaseElement = BaseElement
        self.GamePage = GamePage
        self.HomePage = HomePage
        self.ShopPage = ShopPage

    def file_path(self, folder_name):
        path = f"/Users/amber/PycharmProjects/Sortball_副本/case/log/{folder_name}"
        if os.path.exists(path):
            return self
        else:
            os.makedirs(path)
        return self

    def policy_page_ios(self):
        """
        iOS隐私弹窗页面截图
        :return:
        """
        self.PrivacyPage().first_open()
        filename = "隐私弹窗"
        self.BaseElement().get_snapshot(filename, self.name)
        return self

    def policy_page_android(self):
        """
        安卓的隐私弹窗截图
        :return:
        """
        self.PrivacyPage().first_open_android()
        filename = "隐私弹窗"
        self.BaseElement().get_snapshot(filename, self.name)
        return self

    def game_guide(self):
        """
        关于新手引导的截图
        :return:
        """
        first_step = "新手引导第一步"
        second_step = "新手引导第二步"
        self.PrivacyPage().click_accept()
        self.BaseElement().get_snapshot(first_step, self.name)
        self.GamePlayGuide().first_guide_step1()
        self.BaseElement().get_snapshot(second_step, self.name)
        return self

    def victory_page(self):
        """
        新手引导之后胜利页面的截图与第二关的引导截图
        :return:
        """
        victory = "胜利页面"
        second_guide = "第二关引导文案"
        victory_banner = "胜利横幅页面"
        self.GamePlayGuide().first_guide_step2()
        self.BaseElement().get_snapshot(victory_banner, self.name)
        self.BaseElement().sleep_time()
        self.BaseElement().get_snapshot(victory, self.name)
        self.GamePage().game_victory()
        self.BaseElement().get_snapshot(second_guide, self.name)
        return self

    def setting_page(self):
        """
        对设置页面进行截图
        :return:
        """
        setting = "设置页面"
        contact = "邮件页面"
        language_page_one = "多语言页面1"
        language_page_two = "多语言页面2"
        self.GamePage().goto_setting()
        self.BaseElement().get_snapshot(setting, self.name)
        # self.GamePage().goto_contact_us()
        # self.BaseElement().get_snapshot(contact, self.name)
        # self.BaseElement().system_back(1)
        self.GamePage().setting_language()
        self.BaseElement().get_snapshot(language_page_one, self.name)
        self.GamePage().drag_page()
        self.BaseElement().get_snapshot(language_page_two, self.name)
        self.GamePage().setting_close().setting_close()
        return self

    def about_ad(self):
        ad_loading = "广告loading"
        no_ad_toast = "无广告toast"
        self.GamePage().add_tube().add_tube().add_tube()
        self.BaseElement().get_snapshot(ad_loading, self.name)
        self.BaseElement().sleep_time(5)
        self.GamePage().add_tube()
        self.BaseElement().sleep_time(5).get_snapshot(no_ad_toast, self.name)
        return self

    def scoring_guidance(self):
        score_guidance = "评分引导弹窗"
        self.GamePage().get_debug().get_debug().debug_win().game_victory().debug_win().game_victory().debug_win()
        self.BaseElement().get_snapshot(score_guidance, self.name)
        self.GamePage().setting_close().game_victory()
        return self

    def special_pop_up(self):
        """
        评分引导之后为第五关，第五关通关为特殊关卡,特殊关卡的弹窗
        :return:
        """
        special_illustrate = "特殊关卡说明"
        special_page = "特殊关卡页面"
        exit_special_page = "特殊关卡返回弹窗"
        self.GamePage().debug_win().game_victory()
        self.BaseElement().get_snapshot(special_illustrate, self.name)
        self.GamePage().special_play()
        self.BaseElement().get_snapshot(special_page, self.name)
        self.GamePage().game_back()
        self.BaseElement().get_snapshot(exit_special_page, self.name)
        self.GamePage().quit_special()
        return self

    def get_reward(self):
        """
        获得奖励页面截图
        :return:
        """
        reward_page = "奖励页面"
        for i in range(4):
            self.GamePage().debug_win().game_victory()
        self.BaseElement().sleep_time().get_snapshot(reward_page, self.name)
        self.GamePage().reward_page_use()
        return self

    def shop_page(self):
        """
        首页与商店页面截图
        :return:
        """
        game_home = "游戏首页"
        shop_tube = "商店管页面"
        unlock_tube = "未解锁的管toast"
        shop_background = "商店背景页面"
        unlock_background = "未解锁的背景toast"
        shop_ball = "商店球页面"
        unlock_ball = "未解锁的球toast"
        coin_page = "获得金币页面"
        self.GamePage().goto_setting().goto_home()
        self.BaseElement().get_snapshot(game_home, self.name)
        self.HomePage().goto_shop()
        self.BaseElement().get_snapshot(shop_tube, self.name)
        self.ShopPage().lock_tube().get_snapshot(unlock_tube, self.name)
        self.ShopPage().goto_background().get_snapshot(shop_background, self.name)
        self.ShopPage().lock_tube()
        self.BaseElement().get_snapshot(unlock_background, self.name)
        self.ShopPage().goto_ball()
        self.BaseElement().get_snapshot(shop_ball, self.name)
        self.ShopPage().lock_tube()
        self.BaseElement().get_snapshot(unlock_ball, self.name)
        self.ShopPage().get_coins()
        self.BaseElement().get_snapshot(coin_page, self.name)
        self.GamePage().setting_close()
        return self

    def no_level(self):
        no_level_toast = "没有关卡toast"
        self.ShopPage().shop_back_home()
        self.HomePage().get_level_3000().home_goto_game()
        self.GamePage().debug_win().game_victory()
        self.BaseElement().get_snapshot(no_level_toast, self.name)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&", ])
    SortBallLanguage().file_path("英语").policy_page_android().game_guide(). \
        victory_page().setting_page().about_ad().scoring_guidance(). \
        special_pop_up().get_reward().shop_page().no_level()
    # SortBallLanguage().file_path("英语_12mini").no_level()
