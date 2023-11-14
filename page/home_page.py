# coding = utf-8
# Author: Zoe
# File: home_page.py
# Time: 2023/10/25 3:10 下午
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from base.base import BaseElement
from page.shop_page import ShopPage


class HomePage(BaseElement):
    shop_button = Template(r"../picture/home_page/shop_button.png", record_pos=(0.411, -0.908), resolution=(1440, 3088))
    level_button = Template(r"../picture/home_page/level_button.png", target_pos=6, record_pos=(-0.251, 0.578),
                            resolution=(1440, 3088))

    def goto_shop(self):
        """
        从首页进入商店页面
        :return:
        """
        if exists(self.shop_button):
            self.image_click(self.shop_button)
        else:
            self.image_click([1330, 248])
        self.sleep_time()
        return ShopPage

    def get_level_3000(self):
        """
        糊弄写法,得到3000关
        :return:
        """
        self.image_click([1228, 1396])
        self.sleep_time(1)
        self.image_click([698, 1587])
        self.sleep_time(1)
        self.image_click([909, 2054])
        self.image_click([540, 2767], times=3)
        self.image_click([1243, 2290])
        return self

    def ios_get_level_3000(self):
        self.image_click([1107, 1214])
        self.sleep_time(1)
        self.image_click([636, 1352])
        self.sleep_time(1)
        self.image_click([315, 1948])
        self.image_click([1223, 1979], times=3)
        self.image_click([814, 1797])
        return self

    def home_goto_game(self):
        """
        首页点击进入游戏页面
        :return:
        """
        if exists(self.level_button):
            self.image_click(self.level_button)
        else:
            self.image_click([786, 2365])
        self.sleep_time()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])

    HomePage().ios_get_level_3000()
