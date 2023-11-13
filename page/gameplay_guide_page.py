# coding = utf-8
# Author: Zoe
# File: gameplay_guide_page.py
# Time: 2023/10/25 2:56 下午
"""
新手引导页面
"""
from base.base import BaseElement
from base.base_app import SortBallApp
from airtest.core.api import *
from page.game_page import GamePage
from airtest.cli.parser import cli_setup

ST.SAVE_IMAGE = False


class GamePlayGuide(BaseElement, SortBallApp):
    level1_second_tube = Template(r"../picture/guide_page/level1_second_tube.png", record_pos=(0.188, -0.058),
                                  resolution=(1440, 3088))
    level1_first_tube = Template(r"../picture/guide_page/level1_first_tube.png", record_pos=(-0.173, -0.06),
                                 resolution=(1440, 3088))

    def first_guide_step1(self):
        """
        新手引导第一关的第一步
        :return:
        """
        if exists(self.level1_second_tube):
            self.image_click(self.level1_second_tube)
        else:
            self.image_click([814, 1156])
        self.sleep_time()
        return self

    def first_guide_step2(self):
        """
        新手引导第一关的第二步
        :return:游戏胜利页面
        """
        if exists(self.level1_first_tube):
            self.image_click(self.level1_first_tube)
        else:
            self.image_click([354, 1199])
        return GamePage


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    GamePlayGuide().first_guide_step2()