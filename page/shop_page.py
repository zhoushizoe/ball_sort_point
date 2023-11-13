# coding = utf-8
# Author: Zoe
# File: shop_page.py
# Time: 2023/10/25 3:10 下午
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from base.base import BaseElement


class ShopPage(BaseElement):
    background_button = Template(r"../picture/shop_page/background_button.png", record_pos=(-0.008, -0.758),
                                 resolution=(1440, 3088))
    unlocked_tube = Template(r"../picture/shop_page/unlocked_tube.png", record_pos=(-0.177, -0.021),
                             resolution=(1440, 3088))
    ball_button = Template(r"../picture/shop_page/ball_button.png", record_pos=(0.311, -0.751), resolution=(1440, 3088))
    get_coins_button = Template(r"../picture/shop_page/get_coins_button.png", record_pos=(0.183, 0.429),
                                resolution=(1440, 3088))
    back_home_button = Template(r"../picture/shop_page/back_home_button.png", record_pos=(-0.382, -0.906),
                                resolution=(1440, 3088))

    def lock_tube(self):
        if exists(self.unlocked_tube):
            self.image_click(self.unlocked_tube)
        else:
            self.image_click([422, 1532])
        return self

    def goto_background(self):
        """
        从管的商店页面到背景商店页面
        :return:
        """
        if exists(self.background_button):
            self.image_click(self.background_button)
        else:
            self.image_click([728, 456])
        self.sleep_time(2)
        return self

    def goto_ball(self):
        """
        进入商店页面的球页面
        :return: 
        """
        if exists(self.ball_button):
            self.image_click(self.ball_button)
        else:
            self.image_click([895, 387])
        self.sleep_time()
        return self

    def get_coins(self):
        """
        点击获得金币弹窗
        :return: 
        """
        if exists(self.get_coins_button):
            self.image_click(self.get_coins_button)
        else:
            self.image_click([965, 2157])
        self.sleep_time()
        return self

    def shop_back_home(self):
        """
        从商店页面回到首页
        :return:
        """
        if exists(self.back_home_button):
            self.image_click(self.back_home_button)
        else:
            self.image_click([150, 254])
        self.sleep_time()
        return self
