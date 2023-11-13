# coding = utf-8
# Author: Zoe
# File: game_page.py
# Time: 2023/10/25 3:07 下午
"""
这里存放一些游戏页面中的通用操作，比如设置页面、胜利页面、开启奖励等
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from base.base import BaseElement
from page.home_page import HomePage


class GamePage(BaseElement):
    next_button = Template(r"../picture/game_page/next_button.png", record_pos=(-0.227, 0.528), resolution=(1440, 3088))
    setting_button = Template(r"../picture/game_page/setting_button.png", record_pos=(-0.404, -0.906),
                              resolution=(1440, 3088))
    contace_us_button = Template(r"../picture/game_page/contace_us_button.png", record_pos=(-0.316, 0.31),
                                 resolution=(1440, 3088))
    language_button = Template(r"../picture/game_page/language_button.png", record_pos=(-0.318, 0.182),
                               resolution=(1440, 3088))
    setting_close_button = Template(r"../picture/game_page/setting_close_button.png", record_pos=(0.341, -0.497),
                                    resolution=(1440, 3088))
    setting_home_button = Template(r"../picture/game_page/setting_home_button.png", record_pos=(-0.31, -0.081),
                                   resolution=(1440, 3088))
    add_tube_button = Template(r"../picture/game_page/add_tube_button.png", record_pos=(0.391, -0.906),
                               resolution=(1440, 3088))
    debug_win_button = Template(r"../picture/game_page/debug_win_button.png", record_pos=(0.355, -0.181),
                                resolution=(1440, 3088))
    special_play_button = Template(r"../picture/game_page/special_play_button.png", target_pos=6,
                                   record_pos=(-0.24, 0.312), resolution=(1440, 3088))
    game_back_button = Template(r"../picture/game_page/game_back_button.png", record_pos=(-0.41, -0.912),
                                resolution=(1440, 3088))
    quit_button = Template(r"../picture/game_page/quit_button.png", record_pos=(-0.224, 0.1), resolution=(1440, 3088))
    reward_use_button = Template(r"../picture/game_page/reward_use_button.png", target_pos=6,
                                 record_pos=(-0.242, 0.307), resolution=(1440, 3088))

    def game_victory(self):
        """
        点击游戏胜利页面的胜利按钮进入下一关
        :return:
        """
        if exists(self.next_button):
            self.image_click(self.next_button)
        else:
            self.image_click([645, 1994])
            self.sleep_time()
        return self

    def goto_setting(self):
        """
        从游戏页面进入设置弹窗
        :return:
        """
        if exists(self.setting_button):
            self.image_click(self.setting_button)
        else:
            self.image_click([133, 260])
        self.sleep_time(2)
        return self

    def goto_contact_us(self):
        """
        点击进入邮箱页面
        :return:
        """
        if exists(self.contace_us_button):
            self.image_click(self.contace_us_button)
        else:
            self.image_click([624, 1989])
        self.sleep_time()
        self.system_back(1)
        return self

    def setting_language(self):
        """
        进入设置页面的多语言页面
        :return:
        """
        if exists(self.language_button):
            self.image_click(self.language_button)
        else:
            self.image_click([578, 1821])
        self.sleep_time()
        return self

    def drag_page(self):
        """
        在设置页面的多语言界面滑动，查看剩余的多语言
        :return:
        """
        self.image_swipe([582, 1376], [565, 439])
        self.sleep_time()
        return self

    def setting_close(self):
        """
        点击设置页面的关闭按钮
        :return:
        """
        if exists(self.setting_close_button):
            self.image_click(self.setting_close_button)
        else:
            self.image_click([1179, 815])
            self.image_click([1191, 699])
        self.sleep_time()
        return self

    def goto_home(self):
        """
        从设置页面到主页
        :return:
        """
        if exists(self.setting_home_button):
            self.image_click(self.setting_home_button)
        else:
            self.image_click([717, 1434])
        self.sleep_time()
        return HomePage

    def add_tube(self):
        """
        点击加管道具
        :return:
        """
        if exists(self.add_tube_button):
            self.image_click(self.add_tube_button)
        else:
            self.image_click([1330, 225])
        return self

    def get_debug(self):
        """
        打开debug与展开debug
        :return:
        """
        self.image_click([640, 228])
        self.sleep_time(1)
        return self

    def debug_win(self):
        """
        点击debug中的胜利按钮
        :return:
        """
        if exists(self.debug_win_button):
            self.image_click(self.debug_win_button)
        else:
            self.image_click([1095, 1087])
        self.sleep_time(4)
        return self

    def debug_goto_normal(self):
        self.image_click([1084, 1198])
        self.sleep_time()
        return self

    def debug_goto_special(self):
        self.image_click([1249, 1198])
        self.sleep_time()
        return self

    def deg_get_level_site(self):
        self.image_click([645, 1377])
        self.sleep_time()
        return self

    def get_normal_ten(self):
        self.image_click([91, 1972])
        self.image_click([1212, 1944])
        self.image_click([1015, 1807])
        return self





    def special_play(self):
        """
        在特殊关卡说明页面点击play，进入特殊关卡
        :return:
        """
        if exists(self.special_play_button):
            self.image_click(self.special_play_button)
        else:
            self.image_click([757, 1972])
        self.sleep_time()
        return self

    def game_back(self):
        """
        弹出退出特殊关卡弹窗
        :return:
        """
        if exists(self.game_back_button):
            self.image_click(self.game_back_button)
        else:
            self.image_click([133, 237])
        self.sleep_time(1)
        return self

    def quit_special(self):
        """
        在特殊关卡退出弹窗点击ok，退出特殊关卡
        :return:
        """
        if exists(self.quit_button):
            self.image_click(self.quit_button)
        else:
            self.image_click([682, 1665])
        self.sleep_time()
        return self

    def reward_page_use(self):
        if exists(self.reward_use_button):
            self.image_click(self.reward_use_button)
        else:
            self.image_click([717, 1983])
        self.sleep_time()
